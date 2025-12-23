/*
 * ESP32 RFID Attendance System with GPS (Neo-7M) and Firebase
 * يسجل الحضور مع الموقع الجغرافي في Firebase
 */

#include <Wire.h>
#include <Adafruit_GFX.h> // oled
#include <Adafruit_SSD1306.h> // oled
#include <SPI.h>
#include <MFRC522.h>
#include <WiFi.h>
#include <Firebase_ESP_Client.h>
#include "addons/TokenHelper.h"
#include "addons/RTDBHelper.h"
#include <NTPClient.h>
#include <WiFiUdp.h>
#include <TinyGPS++.h>
#include <HardwareSerial.h>

// Pin Definitions
#define RED_LED 26
#define GREEN_LED 27
#define BUZZER 25

// RFID Pins
#define RST_PIN 4
#define SS_PIN 5

// GPS Pins - استخدام Serial2
#define GPS_RX 16  // RX من ESP32 يوصل على TX من GPS
#define GPS_TX 17  // TX من ESP32 يوصل على RX من GPS

// OLED pins
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// RFID
MFRC522 rfid(SS_PIN, RST_PIN);

// GPS
TinyGPSPlus gps;
HardwareSerial gpsSerial(2); // استخدام Serial2

// WiFi Credentials
const char* ssid = "FaresLaptob";
const char* password = "123123123";

// Firebase Configuration
#define API_KEY "AIzaSyCkpgL5COmyUhXrf55TzambAFyTqXL23NQ"
#define DATABASE_URL "https://student-bus-sys-default-rtdb.firebaseio.com/"
#define USER_EMAIL "esp32@student.com"
#define USER_PASSWORD "123456789"

// Firebase Objects
FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;

// NTP Client for Time
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org", 7200, 60000); // UTC+2 for Egypt

bool signupOK = false;

// GPS Data
double currentLat = 0.0;
double currentLng = 0.0;
bool gpsFixed = false;
void setup() {
  Serial.begin(115200);
  Serial.println("ESP32 RFID + GPS Attendance System Starting...");
  
  // Initialize GPS Serial
  gpsSerial.begin(9600, SERIAL_8N1, GPS_RX, GPS_TX);
  Serial.println("GPS Serial initialized at 9600 baud");
  
  // Initialize Pins
  pinMode(RED_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  
  digitalWrite(RED_LED, LOW);
  digitalWrite(GREEN_LED, LOW);
  digitalWrite(BUZZER, LOW);
  
  // Initialize I2C for OLED
  Wire.begin(21, 22);
  
  // Initialize OLED
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("OLED Failed!");
  } else {
    Serial.println("OLED OK!");
    display.clearDisplay();
    display.setTextSize(1);
    display.setTextColor(SSD1306_WHITE);
    display.setCursor(0, 0);
    display.println("System Starting");
    display.display();
  }
  
  // Initialize SPI for RFID
  SPI.begin(18, 19, 23, 5);
  rfid.PCD_Init();
  Serial.println("RFID OK!");
  
  // Connect to WiFi
  connectToWiFi();
  
  // Initialize Firebase
  initFirebase();
  
  // Initialize Time Client
  timeClient.begin();
  
  displayMessage("System", "Ready!");
  delay(2000);
  
  // Wait for GPS fix
  Serial.println("\nWaiting for GPS fix...");
  displayMessage("GPS", "Searching...");
}

void loop() {
  // تحديث بيانات GPS
  updateGPS();
  
  // تحديث الوقت
  timeClient.update();
  
  // عرض رسالة الانتظار مع حالة GPS
  display.clearDisplay();
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println("RFID Attendance");
  display.println("___________________");
  
  // عرض حالة GPS
  if (gpsFixed) {
    display.print("GPS: OK ");
    display.print(gps.satellites.value());
    display.println(" sats");
    display.print("Lat: ");
    display.println(currentLat, 6);
    display.print("Lng: ");
    display.println(currentLng, 6);
  } else {
    display.println("GPS: Searching...");
    display.print("Sats: ");
    display.println(gps.satellites.value());
  }
  
  display.println("");
  display.setTextSize(1);
  display.println("Scan Card");
  display.display();
  
  // التحقق من وجود كارت RFID
  if (rfid.PICC_IsNewCardPresent() && rfid.PICC_ReadCardSerial()) {
    String uid = getCardUID();
    Serial.print("Card Detected: ");
    Serial.println(uid);
    
    // التحقق من الطالب وتسجيل الحضور مع الموقع
    checkStudentAndRecord(uid);
    
    rfid.PICC_HaltA();
    rfid.PCD_StopCrypto1();
    
    delay(3000);
  }
  
  delay(100);
}

void updateGPS() {
  // قراءة بيانات GPS
  while (gpsSerial.available() > 0) {
    char c = gpsSerial.read();
    if (gps.encode(c)) {
      // تحديث الإحداثيات إذا كانت صالحة
      if (gps.location.isValid()) {
        currentLat = gps.location.lat();
        currentLng = gps.location.lng();
        gpsFixed = true;
      }
    }
  }
  
  // التحقق من صلاحية البيانات
  if (millis() > 5000 && gps.charsProcessed() < 10) {
    Serial.println("WARNING: No GPS data received. Check wiring!");
  }
}

void connectToWiFi() {
  Serial.println("\n==========================");
  Serial.println("Connecting to WiFi...");
  Serial.println("SSID: " + String(ssid));
  Serial.println("==========================");
  displayMessage("WiFi", "Connecting...");
  
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 30) {
    delay(500);
    Serial.print(".");
    attempts++;
  }
  Serial.println();
  
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("WiFi Connected Successfully!");
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
    Serial.println("==========================\n");
    
    displayMessage("WiFi", "Connected!");
    successBeep();
    delay(1000);
  } else {
    Serial.println("WiFi Connection FAILED!");
    Serial.println("Please check SSID and Password");
    Serial.println("==========================\n");
    
    displayMessage("WiFi", "Failed!");
    errorBeep();
    delay(3000);
    
    Serial.println("Restarting ESP32...");
    delay(1000);
    ESP.restart();
  }
}

void initFirebase() {
  Serial.println("==========================");
  Serial.println("Initializing Firebase...");
  Serial.println("==========================");
  displayMessage("Firebase", "Connecting...");
  
  config.api_key = API_KEY;
  config.database_url = DATABASE_URL;
  
  auth.user.email = USER_EMAIL;
  auth.user.password = USER_PASSWORD;
  
  config.token_status_callback = tokenStatusCallback;
  
  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);
  
  Serial.println("Waiting for Firebase Authentication...");
  int attempts = 0;
  while (!Firebase.ready() && attempts < 30) {
    delay(500);
    Serial.print(".");
    attempts++;
  }
  Serial.println();
  
  if (Firebase.ready()) {
    signupOK = true;
    Serial.println("Firebase Connected Successfully!");
    Serial.println("==========================\n");
    
    displayMessage("Firebase", "Connected!");
    successBeep();
    delay(1000);
  } else {
    Serial.println("Firebase Connection FAILED!");
    Serial.println("Check your API_KEY, DATABASE_URL, EMAIL, and PASSWORD");
    Serial.println("==========================\n");
    
    displayMessage("Firebase", "Failed!");
    errorBeep();
    delay(2000);
    
    ESP.restart();
  }
}

String getCardUID() {
  String uid = "";
  for (byte i = 0; i < rfid.uid.size; i++) {
    uid += String(rfid.uid.uidByte[i], HEX);
  }
  uid.toUpperCase();
  return uid;
}

void checkStudentAndRecord(String cardUID) {
  if (!signupOK) {
    Serial.println("ERROR: Firebase not connected!");
    displayMessage("Error", "No Firebase");
    errorBeep();
    return;
  }
  
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("ERROR: WiFi disconnected during operation!");
    displayMessage("Error", "WiFi Lost");
    errorBeep();
    delay(2000);
    
    Serial.println("Attempting to reconnect WiFi...");
    WiFi.disconnect();
    delay(100);
    WiFi.begin(ssid, password);
    
    int attempts = 0;
    while (WiFi.status() != WL_CONNECTED && attempts < 20) {
      delay(500);
      Serial.print(".");
      attempts++;
    }
    
    if (WiFi.status() == WL_CONNECTED) {
      Serial.println("\nWiFi reconnected!");
    } else {
      Serial.println("\nWiFi reconnection failed. Restarting...");
      delay(1000);
      ESP.restart();
    }
    return;
  }
  
  Serial.println("\n--- Checking Student ---");
  displayMessage("Checking", "Please wait..");
  
  String path = "/students/" + cardUID;
  
  String studentName = "";
  if (Firebase.RTDB.getString(&fbdo, path + "/name")) {
    if (fbdo.dataType() == "string") {
      studentName = fbdo.stringData();
    }
  } else {
    Serial.println("Firebase Read Error or Student Not Found");
    Serial.println("Error: " + fbdo.errorReason());
  }
  
  String studentCode = "";
  if (Firebase.RTDB.getString(&fbdo, path + "/code")) {
    if (fbdo.dataType() == "string") {
      studentCode = fbdo.stringData();
    }
  }
  
  String studentID = "";
  if (Firebase.RTDB.getString(&fbdo, path + "/id")) {
    if (fbdo.dataType() == "string") {
      studentID = fbdo.stringData();
    }
  }
  
  if (studentName != "" && studentName.length() > 0) {
    Serial.println("\n=========================");
    Serial.println("STUDENT FOUND!");
    Serial.println("=========================");
    Serial.println("Name: " + studentName);
    Serial.println("Code: " + studentCode);
    Serial.println("ID: " + studentID);
    
    // طباعة معلومات GPS
    if (gpsFixed) {
      Serial.println("\nGPS Location:");
      Serial.print("Latitude: ");
      Serial.println(currentLat, 6);
      Serial.print("Longitude: ");
      Serial.println(currentLng, 6);
      Serial.print("Satellites: ");
      Serial.println(gps.satellites.value());
      Serial.print("Altitude: ");
      Serial.print(gps.altitude.meters());
      Serial.println(" m");
      Serial.print("Speed: ");
      Serial.print(gps.speed.kmph());
      Serial.println(" km/h");
    } else {
      Serial.println("\nGPS: No Fix Yet");
    }
    Serial.println("=========================\n");
    
    time_t epochTime = timeClient.getEpochTime();
    struct tm *ptm = gmtime((time_t *)&epochTime);
    
    int day = ptm->tm_mday;
    int month = ptm->tm_mon + 1;
    int year = ptm->tm_year + 1900;
    int hour = ptm->tm_hour;
    int minute = ptm->tm_min;
    int second = ptm->tm_sec;
    
    String currentDate = getCurrentDate();
    String currentTime = getCurrentTime();
    
    Serial.println("Current Date: " + currentDate);
    Serial.println("Current Time: " + currentTime);
    
    String timestamp = String(year) + String(month < 10 ? "0" : "") + String(month) + 
                      String(day < 10 ? "0" : "") + String(day) + "_" +
                      String(hour < 10 ? "0" : "") + String(hour) + 
                      String(minute < 10 ? "0" : "") + String(minute) + 
                      String(second < 10 ? "0" : "") + String(second);
    
    String attendancePath = "/attendance/" + cardUID + "/" + timestamp;
    
    Serial.println("\nSaving to Firebase...");
    Serial.println("Path: " + attendancePath);
    
    bool saveSuccess = true;
    
    // حفظ بيانات الطالب
    if (!Firebase.RTDB.setString(&fbdo, attendancePath + "/studentName", studentName)) {
      Serial.println("✗ Failed to save studentName: " + fbdo.errorReason());
      saveSuccess = false;
    } else {
      Serial.println("✓ studentName saved");
    }
    
    Firebase.RTDB.setString(&fbdo, attendancePath + "/studentCode", studentCode);
    Firebase.RTDB.setString(&fbdo, attendancePath + "/studentID", studentID);
    Firebase.RTDB.setString(&fbdo, attendancePath + "/cardUID", cardUID);
    
    // حفظ التاريخ والوقت
    Firebase.RTDB.setInt(&fbdo, attendancePath + "/year", year);
    Firebase.RTDB.setInt(&fbdo, attendancePath + "/month", month);
    Firebase.RTDB.setInt(&fbdo, attendancePath + "/day", day);
    Firebase.RTDB.setString(&fbdo, attendancePath + "/fullDate", currentDate);
    
    Firebase.RTDB.setInt(&fbdo, attendancePath + "/hour", hour);
    Firebase.RTDB.setInt(&fbdo, attendancePath + "/minute", minute);
    Firebase.RTDB.setInt(&fbdo, attendancePath + "/second", second);
    Firebase.RTDB.setString(&fbdo, attendancePath + "/fullTime", currentTime);
    
    Firebase.RTDB.setString(&fbdo, attendancePath + "/status", "present");
    Firebase.RTDB.setInt(&fbdo, attendancePath + "/timestamp", epochTime);
    
    // حفظ بيانات GPS
    if (gpsFixed) {
      Firebase.RTDB.setDouble(&fbdo, attendancePath + "/location/latitude", currentLat);
      Firebase.RTDB.setDouble(&fbdo, attendancePath + "/location/longitude", currentLng);
      Firebase.RTDB.setInt(&fbdo, attendancePath + "/location/satellites", gps.satellites.value());
      Firebase.RTDB.setDouble(&fbdo, attendancePath + "/location/altitude", gps.altitude.meters());
      Firebase.RTDB.setDouble(&fbdo, attendancePath + "/location/speed", gps.speed.kmph());
      Firebase.RTDB.setString(&fbdo, attendancePath + "/location/status", "fixed");
      
      // إنشاء رابط Google Maps
      String mapsLink = "https://www.google.com/maps?q=" + String(currentLat, 6) + "," + String(currentLng, 6);
      Firebase.RTDB.setString(&fbdo, attendancePath + "/location/mapsLink", mapsLink);
      
      Serial.println("✓ GPS location saved");
      Serial.println("✓ Google Maps: " + mapsLink);
    } else {
      Firebase.RTDB.setString(&fbdo, attendancePath + "/location/status", "no_fix");
      Serial.println("⚠ GPS location not available");
    }
    
    if (saveSuccess) {
      Serial.println("\n✓✓✓ All data saved successfully! ✓✓✓");
    } else {
      Serial.println("\n⚠ Some data failed to save, but continuing...");
    }
    
    // عرض على الشاشة
    display.clearDisplay();
    display.setTextSize(1);
    display.setCursor(0, 0);
    display.println("Welcome!");
    display.println("---------------");
    display.setTextSize(1);
    display.println(studentName);
    display.println("");
    display.print(day);
    display.print("/");
    display.print(month);
    display.print(" ");
    display.print(hour);
    display.print(":");
    if(minute < 10) display.print("0");
    display.println(minute);
    
    if (gpsFixed) {
      display.println("");
      display.print("GPS: ");
      display.print(currentLat, 4);
      display.print(",");
      display.println(currentLng, 4);
    } else {
      display.println("");
      display.println("GPS: No Fix");
    }
    display.display();
    
    digitalWrite(GREEN_LED, HIGH);
    successBeep();
    delay(3000);
    digitalWrite(GREEN_LED, LOW);
    
    Serial.println("\n=========================");
    Serial.println("ATTENDANCE RECORDED!");
    Serial.println("=========================");
    Serial.println("Ready for next card...\n");
    
  } else {
    Serial.println("Student name is empty - Not registered");
    studentNotFound(cardUID);
  }
}

void studentNotFound(String cardUID) {
  Serial.println("\n=========================");
  Serial.println("STUDENT NOT FOUND!");
  Serial.println("Card UID: " + cardUID);
  Serial.println("This card is not registered in the system");
  Serial.println("=========================\n");
  
  display.clearDisplay();
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println("Access Denied!");
  display.println("---------------");
  display.setCursor(0, 25);
  display.println("Card not");
  display.println("registered");
  display.println("");
  display.print("ID: ");
  display.println(cardUID);
  display.display();
  
  digitalWrite(RED_LED, HIGH);
  errorBeep();
  delay(3000);
  digitalWrite(RED_LED, LOW);
  
  Serial.println("Ready for next card...\n");
}

String getCurrentDate() {
  time_t epochTime = timeClient.getEpochTime();
  struct tm *ptm = gmtime((time_t *)&epochTime);
  
  int day = ptm->tm_mday;
  int month = ptm->tm_mon + 1;
  int year = ptm->tm_year + 1900;
  
  String date = String(year) + "-" + 
                (month < 10 ? "0" : "") + String(month) + "-" + 
                (day < 10 ? "0" : "") + String(day);
  return date;
}

String getCurrentTime() {
  return timeClient.getFormattedTime();
}

void successBeep() {
  digitalWrite(BUZZER, HIGH);
  delay(100);
  digitalWrite(BUZZER, LOW);
  delay(50);
  digitalWrite(BUZZER, HIGH);
  delay(100);
  digitalWrite(BUZZER, LOW);
}

void errorBeep() {
  digitalWrite(BUZZER, HIGH);
  delay(800);
  digitalWrite(BUZZER, LOW);
}

void displayMessage(String line1, String line2) {
  display.clearDisplay();
  display.setTextSize(2);
  display.setCursor(0, 10);
  display.println(line1);
  display.setCursor(0, 35);
  display.println(line2);
  display.display();
}
//rfid :
//sda -> g5
//sck -> g18
//mosi -> g23
//miso -> g19
//irq -> no pin 
//gnd -> gnd 
//rst -> g4
//3.3v -> 3v3
//oled display : 
//gnd -> gnd 
//vcc -> 3v3
//scl -> g22
//sda -> g21

//buzzer : 
//+ -> g25
//- -> gnd
//neo-7m-0-000 gps : 
//pps -> no pin
//rxd -> g17
//txd -> g16
//gnd -> gnd 
//vvc -> 5v
//green lamp -> 
//- -> gnd 
//+ -> g27
//red lamp ->
//- -> gnd 
//+ -> g26