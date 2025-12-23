from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import requests


class Ui_MapForm(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(466, 741)
        Form.setStyleSheet("QWidget { background-color: #FFFFFF; }")

        # Firebase configuration
        self.firebase_url = "https://student-bus-sys-default-rtdb.firebaseio.com"
        self.latest_location = None
        self.bus_routes = {}

        # Main layout
        self.mainLayout = QtWidgets.QVBoxLayout(Form)
        self.mainLayout.setContentsMargins(30, 20, 30, 20)
        self.mainLayout.setSpacing(15)

        # Top bar with back button and logo
        topLayout = QtWidgets.QHBoxLayout()

        # Back button
        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setMinimumSize(QtCore.QSize(40, 40))
        self.backButton.setMaximumSize(QtCore.QSize(40, 40))
        self.backButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 20px;
                font-weight: bold;
                border-radius: 20px;
                border: none;
            }
            QPushButton:hover {
                background-color: #3d8b40;
            }
            QPushButton:pressed {
                background-color: #2E7D32;
            }
        """)
        self.backButton.setText("←")
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.clicked.connect(self.goBackHome)
        topLayout.addWidget(self.backButton)

        topLayout.addStretch()

        self.logoCorner = QtWidgets.QLabel(Form)
        self.logoCorner.setText("")
        self.logoCorner.setPixmap(QtGui.QPixmap(
            "C:/Users/fares/Desktop/gui/app-main/Elsewedy-University-of-Technology-Egypt-96010-1698259526-removebg-preview.png"))
        self.logoCorner.setScaledContents(True)
        self.logoCorner.setMaximumSize(QtCore.QSize(80, 80))
        self.logoCorner.setMinimumSize(QtCore.QSize(60, 60))
        topLayout.addWidget(self.logoCorner)

        self.mainLayout.addLayout(topLayout)

        # Title
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setStyleSheet("color: rgb(26, 26, 26); font: 75 28pt \"MS Shell Dlg 2\";")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.mainLayout.addWidget(self.label_title)

        # Subtitle
        self.label_subtitle = QtWidgets.QLabel(Form)
        self.label_subtitle.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; color: rgb(100, 100, 100);")
        self.label_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle.setObjectName("label_subtitle")
        self.mainLayout.addWidget(self.label_subtitle)

        self.mainLayout.addSpacing(10)

        # Current Route Display (مكتوب فيه الخط الحالي)
        self.currentRouteLabel = QtWidgets.QLabel(Form)
        self.currentRouteLabel.setStyleSheet("""
            QLabel {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #4CAF50, stop:1 #8BC34A);
                color: white;
                padding: 15px;
                border-radius: 12px;
                font-size: 16pt;
                font-weight: bold;
                border: 3px solid #2E7D32;
            }
        """)
        self.currentRouteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentRouteLabel.setText("🚌 الخط الحالي: لم يتم الاختيار")
        self.mainLayout.addWidget(self.currentRouteLabel)

        self.mainLayout.addSpacing(10)

        # Map Display Area (clickable)
        self.mapDisplay = QtWidgets.QPushButton(Form)
        self.mapDisplay.setStyleSheet("""
            QPushButton {
                background-color: #E8F5E9;
                border: 3px solid #4CAF50;
                border-radius: 15px;
                font-size: 16pt;
                color: #4CAF50;
            }
            QPushButton:hover {
                background-color: #C8E6C9;
                border: 3px solid #2E7D32;
            }
            QPushButton:pressed {
                background-color: #A5D6A7;
            }
        """)
        self.mapDisplay.setText("🗺️\n\nMap View\n\n(Click to Open)")
        self.mapDisplay.setMinimumSize(QtCore.QSize(0, 250))
        self.mapDisplay.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mapDisplay.clicked.connect(self.openGoogleMaps)
        self.mainLayout.addWidget(self.mapDisplay)

        # Location info display
        self.locationInfo = QtWidgets.QLabel(Form)
        self.locationInfo.setStyleSheet("""
            QLabel {
                background-color: #F5F5F5;
                padding: 12px;
                border-radius: 10px;
                font-size: 10pt;
                color: #333;
            }
        """)
        self.locationInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.locationInfo.setWordWrap(True)
        self.locationInfo.setText("📍 Loading bus routes...")
        self.mainLayout.addWidget(self.locationInfo)

        # Bus Route selector
        routeLayout = QtWidgets.QHBoxLayout()
        routeLabel = QtWidgets.QLabel("🚌 اختر الخط:")
        routeLabel.setStyleSheet("font-size: 14pt; font-weight: bold; color: #333;")
        routeLabel.setMinimumWidth(110)

        self.routeCombo = QtWidgets.QComboBox()
        self.routeCombo.setStyleSheet("""
            QComboBox {
                padding: 12px;
                border: 3px solid #4CAF50;
                border-radius: 10px;
                font-size: 13pt;
                font-weight: bold;
                background-color: white;
                color: #2E7D32;
            }
            QComboBox:focus {
                border: 3px solid #2E7D32;
            }
            QComboBox::drop-down {
                border: none;
                width: 30px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 8px solid #4CAF50;
            }
        """)
        self.routeCombo.currentIndexChanged.connect(self.onRouteChanged)
        routeLayout.addWidget(routeLabel)
        routeLayout.addWidget(self.routeCombo)
        self.mainLayout.addLayout(routeLayout)

        # Buttons Layout
        buttonsLayout = QtWidgets.QHBoxLayout()
        buttonsLayout.setSpacing(10)

        # Open Maps Button
        self.openMapsButton = QtWidgets.QPushButton(Form)
        self.openMapsButton.setMinimumSize(QtCore.QSize(0, 50))
        self.openMapsButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 15px;
                font-weight: bold;
                border-radius: 10px;
                border: none;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #3d8b40;
            }
            QPushButton:pressed {
                background-color: #2E7D32;
            }
            QPushButton:disabled {
                background-color: #CCCCCC;
                color: #888888;
            }
        """)
        self.openMapsButton.setText("🗺️ Open Route Location")
        self.openMapsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.openMapsButton.clicked.connect(self.openGoogleMaps)
        self.openMapsButton.setEnabled(False)
        buttonsLayout.addWidget(self.openMapsButton)

        # Refresh Button
        self.refreshButton = QtWidgets.QPushButton(Form)
        self.refreshButton.setMinimumSize(QtCore.QSize(0, 50))
        self.refreshButton.setMaximumSize(QtCore.QSize(100, 50))
        self.refreshButton.setStyleSheet("""
            QPushButton {
                background-color: #8BC34A;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 10px;
                border: none;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #7CB342;
            }
            QPushButton:pressed {
                background-color: #689F38;
            }
        """)
        self.refreshButton.setText("🔄")
        self.refreshButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refreshButton.clicked.connect(self.loadBusRoutes)
        buttonsLayout.addWidget(self.refreshButton)

        self.mainLayout.addLayout(buttonsLayout)

        # Info Label
        self.infoLabel = QtWidgets.QLabel(Form)
        self.infoLabel.setStyleSheet("""
            QLabel {
                background-color: #E8F5E9;
                padding: 10px;
                border-radius: 8px;
                font-size: 10pt;
                color: #2E7D32;
            }
        """)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setText("📍 اختر خط الباص لعرض الموقع على الخريطة")
        self.mainLayout.addWidget(self.infoLabel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Load data when form opens
        self.loadBusRoutes()

    def loadBusRoutes(self):
        """تحميل خطوط الباصات من Firebase"""
        try:
            # Get all attendance records
            response = requests.get(f"{self.firebase_url}/attendance.json")

            if response.status_code == 200:
                data = response.json()

                if data:
                    # Clear combo box
                    self.routeCombo.clear()
                    self.bus_routes = {}

                    # Group records by student (assuming each student represents a route)
                    route_locations = {}

                    for card_uid, timestamps in data.items():
                        # Get latest record for this card
                        latest_timestamp = max(timestamps.keys())
                        record = timestamps[latest_timestamp]

                        # Check if record has valid location
                        if 'location' in record and record['location'].get('status') == 'fixed':
                            student_name = record.get('studentName', 'Unknown')
                            student_code = record.get('studentCode', card_uid[:8])

                            # Create route name
                            route_name = f"خط {student_code} - {student_name}"

                            # Store route data
                            route_locations[route_name] = {
                                'location': record['location'],
                                'student_name': student_name,
                                'student_code': student_code,
                                'date': record.get('fullDate', ''),
                                'time': record.get('fullTime', ''),
                                'card_uid': card_uid
                            }

                    if route_locations:
                        # Sort routes by name
                        sorted_routes = sorted(route_locations.keys())

                        # Add routes to combo box
                        self.routeCombo.addItem("-- اختر الخط --")
                        for route_name in sorted_routes:
                            self.routeCombo.addItem(route_name)
                            self.bus_routes[route_name] = route_locations[route_name]

                        self.locationInfo.setText(
                            f"✅ تم تحميل {len(route_locations)} خط\n"
                            f"اختر خط من القائمة لعرض الموقع"
                        )
                        self.locationInfo.setStyleSheet("""
                            QLabel {
                                background-color: #E8F5E9;
                                padding: 12px;
                                border-radius: 10px;
                                font-size: 10pt;
                                color: #2E7D32;
                            }
                        """)
                    else:
                        self.locationInfo.setText("⚠️ لا توجد خطوط بمواقع GPS متاحة")
                        self.locationInfo.setStyleSheet("""
                            QLabel {
                                background-color: #FFF3E0;
                                padding: 12px;
                                border-radius: 10px;
                                font-size: 10pt;
                                color: #E65100;
                            }
                        """)
                else:
                    self.locationInfo.setText("📭 لا توجد سجلات حضور في قاعدة البيانات")

        except Exception as e:
            self.locationInfo.setText(f"❌ خطأ في تحميل البيانات:\n{str(e)}")
            self.locationInfo.setStyleSheet("""
                QLabel {
                    background-color: #FFEBEE;
                    padding: 12px;
                    border-radius: 10px;
                    font-size: 10pt;
                    color: #C62828;
                }
            """)

    def onRouteChanged(self, index):
        """عند اختيار خط مختلف"""
        if index > 0 and self.routeCombo.count() > 0:
            selected_route = self.routeCombo.currentText()

            if selected_route in self.bus_routes:
                route_data = self.bus_routes[selected_route]
                location = route_data['location']

                # Update latest location
                self.latest_location = location

                # Update current route label
                self.currentRouteLabel.setText(f"🚌 الخط الحالي: {selected_route}")
                self.currentRouteLabel.setStyleSheet("""
                    QLabel {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                            stop:0 #2E7D32, stop:1 #4CAF50);
                        color: white;
                        padding: 15px;
                        border-radius: 12px;
                        font-size: 16pt;
                        font-weight: bold;
                        border: 3px solid #1B5E20;
                    }
                """)

                if location and location.get('status') == 'fixed':
                    lat = location.get('latitude')
                    lng = location.get('longitude')
                    satellites = location.get('satellites', 0)
                    altitude = location.get('altitude', 0)
                    speed = location.get('speed', 0)

                    # Update location info
                    self.locationInfo.setText(
                        f"📍 تفاصيل الموقع:\n\n"
                        f"Lat: {lat:.6f} | Lng: {lng:.6f}\n"
                        f"🛰️ {satellites} أقمار | ⛰️ {altitude:.1f}m | 🚗 {speed:.1f}km/h"
                    )
                    self.locationInfo.setStyleSheet("""
                        QLabel {
                            background-color: #E8F5E9;
                            padding: 12px;
                            border-radius: 10px;
                            font-size: 10pt;
                            color: #2E7D32;
                            font-weight: bold;
                        }
                    """)

                    # Update map display
                    self.mapDisplay.setText(
                        f"🗺️\n\n"
                        f"Map View\n"
                        f"{route_data['student_name']}\n\n"
                        f"{lat:.4f}, {lng:.4f}\n\n"
                        f"(Click to Open)"
                    )

                    # Enable button
                    self.openMapsButton.setEnabled(True)

                    # Update info label
                    self.infoLabel.setText(
                        f"✅ الخط: {selected_route}\n"
                        f"📅 آخر تحديث: {route_data['date']} {route_data['time']}"
                    )
        else:
            # Reset if no route selected
            self.currentRouteLabel.setText("🚌 الخط الحالي: لم يتم الاختيار")
            self.currentRouteLabel.setStyleSheet("""
                QLabel {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                        stop:0 #4CAF50, stop:1 #8BC34A);
                    color: white;
                    padding: 15px;
                    border-radius: 12px;
                    font-size: 16pt;
                    font-weight: bold;
                    border: 3px solid #2E7D32;
                }
            """)
            self.latest_location = None
            self.openMapsButton.setEnabled(False)
            self.mapDisplay.setText("🗺️\n\nMap View\n\n(Select a route first)")
            self.infoLabel.setText("📍 اختر خط الباص لعرض الموقع على الخريطة")

    def openGoogleMaps(self):
        """فتح خرائط جوجل بالموقع"""
        if self.latest_location and self.latest_location.get('status') == 'fixed':
            # Get coordinates
            lat = self.latest_location.get('latitude')
            lng = self.latest_location.get('longitude')

            # Check if there's a pre-saved maps link
            maps_link = self.latest_location.get('mapsLink')

            if maps_link:
                # Use the saved link
                webbrowser.open(maps_link)
            else:
                # Create new Google Maps link
                maps_url = f"https://www.google.com/maps?q={lat},{lng}"
                webbrowser.open(maps_url)

            # Update info
            route_name = self.routeCombo.currentText()
            self.infoLabel.setText(
                f"✅ تم فتح موقع {route_name}\n"
                f"في خرائط جوجل: {lat:.6f}, {lng:.6f}"
            )
            self.infoLabel.setStyleSheet("""
                QLabel {
                    background-color: #E8F5E9;
                    padding: 10px;
                    border-radius: 8px;
                    font-size: 10pt;
                    color: #2E7D32;
                    font-weight: bold;
                }
            """)
        else:
            # No location available
            self.infoLabel.setText("⚠️ لا يوجد موقع GPS متاح للخط المختار")
            self.infoLabel.setStyleSheet("""
                QLabel {
                    background-color: #FFF3E0;
                    padding: 10px;
                    border-radius: 8px;
                    font-size: 10pt;
                    color: #E65100;
                }
            """)

    def goBackHome(self):
        """العودة للصفحة الرئيسية"""
        from home_page import Ui_HomeForm

        self.homeWindow = QtWidgets.QWidget()
        self.homeUI = Ui_HomeForm()
        self.homeUI.setupUi(self.homeWindow)
        self.homeWindow.show()
        self.Form.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Bus Routes - GPS Location"))
        self.label_title.setText(_translate("Form", "🗺️ خطوط الباصات"))
        self.label_subtitle.setText(_translate("Form", "Bus Routes GPS Tracking"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_MapForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())