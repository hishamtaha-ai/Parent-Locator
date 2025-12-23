from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime, timedelta
import calendar
import requests

# إعدادات Firebase
FIREBASE_DATABASE_URL = "https://student-bus-sys-default-rtdb.firebaseio.com"


class FirebaseDatabase:
    """مكتبة للتعامل مع Realtime Database"""

    def __init__(self, database_url):
        self.database_url = database_url

    def get_attendance_data(self, student_id):
        """الحصول على بيانات الحضور للطالب"""
        try:
            url = f"{self.database_url}/attendance/{student_id}/.json"
            print(f"🔍 جاري الاتصال بـ: {url}")

            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                print(f"✅ تم استلام البيانات بنجاح")
                print(f"📦 البيانات الخام: {list(data.keys()) if data else 'فارغ'}")

                attendance_records = []

                if data:
                    # البحث في كل المفاتيح
                    for key, value in data.items():
                        print(f"📅 معالجة المفتاح: {key}")

                        # حالة 1: المفتاح هو timestamp (مثل "20251221_002643")
                        if isinstance(value, dict) and 'fullDate' in value:
                            full_date = value.get('fullDate', '')
                            status = value.get('status', 'present')
                            timestamp = value.get('timestamp', 0)

                            print(f"  ✅ سجل timestamp: {key}")
                            print(f"     التاريخ: {full_date}")
                            print(f"     الحالة: {status}")

                            attendance_records.append({
                                'fullDate': full_date,
                                'status': status,
                                'timestamp': timestamp,
                                'key': key
                            })

                        # حالة 2: المفتاح هو تاريخ (مثل "2025-12-21") والقيمة dict فيها records
                        elif isinstance(value, dict) and any('-' in str(k) or '_' in str(k) for k in value.keys()):
                            print(f"  📁 المفتاح {key} يحتوي على سجلات متعددة")

                            # البحث داخل السجلات
                            for record_key, record_data in value.items():
                                if isinstance(record_data, dict):
                                    full_date = record_data.get('fullDate', key)
                                    status = record_data.get('status', 'present')
                                    timestamp = record_data.get('timestamp', 0)

                                    print(f"    ✅ سجل فرعي: {record_key}")
                                    print(f"       التاريخ: {full_date}")
                                    print(f"       الحالة: {status}")

                                    attendance_records.append({
                                        'fullDate': full_date,
                                        'status': status,
                                        'timestamp': timestamp,
                                        'key': record_key
                                    })

                        # حالة 3: المفتاح هو تاريخ والقيمة string أو بسيطة
                        elif '-' in str(key) and len(str(key).split('-')) == 3:
                            print(f"  ℹ️ استخدام المفتاح كتاريخ: {key}")
                            attendance_records.append({
                                'fullDate': key,
                                'status': 'present',
                                'timestamp': 0,
                                'key': key
                            })

                print(f"📊 إجمالي السجلات المستخرجة: {len(attendance_records)}")

                # طباعة كل السجلات للتأكد
                for i, record in enumerate(attendance_records, 1):
                    print(f"  {i}. {record['fullDate']} -> {record['status']}")

                return attendance_records
            else:
                print(f"❌ خطأ في الاستجابة: {response.status_code}")
                return None

        except requests.exceptions.ConnectionError as e:
            print(f"❌ خطأ في الاتصال بالإنترنت: {e}")
            return None
        except Exception as e:
            print(f"❌ خطأ غير متوقع: {e}")
            import traceback
            traceback.print_exc()
            return None




# تهيئة Firebase
firebase_db = FirebaseDatabase(FIREBASE_DATABASE_URL)


class Ui_AttendanceForm(object):
    def setupUi(self, Form, user_id="6380F32F", student_code="250104330"):
        self.Form = Form
        self.user_id = user_id  # حفظ الـ user_id (cardUID)
        self.student_code = student_code  # حفظ الـ student code
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(500, 800)
        Form.setStyleSheet("QWidget { background-color: #FFFFFF; }")

        # بيانات الحضور - سيتم تحميلها من Firebase
        self.attendanceData = {}

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
                background-color: #2196F3;
                color: white;
                font-size: 20px;
                font-weight: bold;
                border-radius: 20px;
                border: none;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:pressed {
                background-color: #0D47A1;
            }
        """)
        self.backButton.setText("←")
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.clicked.connect(self.goBackHome)
        topLayout.addWidget(self.backButton)

        topLayout.addStretch()

        self.logoCorner = QtWidgets.QLabel(Form)
        self.logoCorner.setText("")
        try:
            self.logoCorner.setPixmap(QtGui.QPixmap(
                "C:/Users/fares/Desktop/gui/app-main/Elsewedy-University-of-Technology-Egypt-96010-1698259526-removebg-preview.png"))
            self.logoCorner.setScaledContents(True)
        except:
            pass
        self.logoCorner.setMaximumSize(QtCore.QSize(80, 80))
        self.logoCorner.setMinimumSize(QtCore.QSize(60, 60))
        topLayout.addWidget(self.logoCorner)

        self.mainLayout.addLayout(topLayout)

        # Title
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setStyleSheet("color: rgb(26, 26, 26); font: 75 28pt \"MS Shell Dlg 2\";")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setText("📋 حضور الطالب")
        self.mainLayout.addWidget(self.label_title)

        # Subtitle
        self.label_subtitle = QtWidgets.QLabel(Form)
        self.label_subtitle.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; color: rgb(100, 100, 100);")
        self.label_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle.setText("سجل الحضور والغياب")
        self.mainLayout.addWidget(self.label_subtitle)

        # Statistics
        self.statsLayout = QtWidgets.QHBoxLayout()

        self.presentLabel = QtWidgets.QLabel(Form)
        self.presentLabel.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            font-size: 14pt;
            font-weight: bold;
            padding: 15px;
            border-radius: 10px;
        """)
        self.presentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsLayout.addWidget(self.presentLabel)

        self.absentLabel = QtWidgets.QLabel(Form)
        self.absentLabel.setStyleSheet("""
            background-color: #F44336;
            color: white;
            font-size: 14pt;
            font-weight: bold;
            padding: 15px;
            border-radius: 10px;
        """)
        self.absentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsLayout.addWidget(self.absentLabel)

        self.mainLayout.addLayout(self.statsLayout)

        self.mainLayout.addSpacing(10)

        # Month Navigation
        monthNavLayout = QtWidgets.QHBoxLayout()

        self.prevMonthBtn = QtWidgets.QPushButton(Form)
        self.prevMonthBtn.setText("◀")
        self.prevMonthBtn.setMaximumWidth(50)
        self.prevMonthBtn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-size: 18px;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover { background-color: #1976D2; }
        """)
        self.prevMonthBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prevMonthBtn.clicked.connect(self.prevMonth)
        monthNavLayout.addWidget(self.prevMonthBtn)

        self.currentMonthLabel = QtWidgets.QLabel(Form)
        self.currentMonthLabel.setStyleSheet("font: bold 18pt \"MS Shell Dlg 2\"; color: #2196F3;")
        self.currentMonthLabel.setAlignment(QtCore.Qt.AlignCenter)
        monthNavLayout.addWidget(self.currentMonthLabel)

        self.nextMonthBtn = QtWidgets.QPushButton(Form)
        self.nextMonthBtn.setText("▶")
        self.nextMonthBtn.setMaximumWidth(50)
        self.nextMonthBtn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-size: 18px;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover { background-color: #1976D2; }
        """)
        self.nextMonthBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextMonthBtn.clicked.connect(self.nextMonth)
        monthNavLayout.addWidget(self.nextMonthBtn)

        self.mainLayout.addLayout(monthNavLayout)

        # Calendar Grid
        self.calendarWidget = QtWidgets.QTableWidget(Form)
        self.calendarWidget.setColumnCount(7)
        self.calendarWidget.setHorizontalHeaderLabels(
            ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت"])
        self.calendarWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.calendarWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.calendarWidget.verticalHeader().setVisible(False)
        self.calendarWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.calendarWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.calendarWidget.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 2px solid #2196F3;
                border-radius: 10px;
                gridline-color: #E0E0E0;
            }
            QHeaderView::section {
                background-color: #2196F3;
                color: white;
                font-weight: bold;
                font-size: 12pt;
                padding: 8px;
                border: none;
            }
        """)
        self.mainLayout.addWidget(self.calendarWidget)

        # Action Buttons
        buttonLayout = QtWidgets.QHBoxLayout()

        self.showAbsentBtn = QtWidgets.QPushButton(Form)
        self.showAbsentBtn.setText("📍 عرض أيام الغياب")
        self.showAbsentBtn.setMinimumHeight(50)
        self.showAbsentBtn.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover { background-color: #D32F2F; }
            QPushButton:pressed { background-color: #B71C1C; }
        """)
        self.showAbsentBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.showAbsentBtn.clicked.connect(self.showAbsentDays)
        buttonLayout.addWidget(self.showAbsentBtn)

        self.refreshBtn = QtWidgets.QPushButton(Form)
        self.refreshBtn.setText("🔄 تحديث")
        self.refreshBtn.setMinimumHeight(50)
        self.refreshBtn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover { background-color: #1976D2; }
            QPushButton:pressed { background-color: #0D47A1; }
        """)
        self.refreshBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refreshBtn.clicked.connect(self.refreshCalendar)
        buttonLayout.addWidget(self.refreshBtn)

        self.mainLayout.addLayout(buttonLayout)

        # Initialize calendar
        self.currentDate = datetime.now()

        # تحميل البيانات من Firebase
        self.loadAttendanceFromFirebase()

        QtCore.QMetaObject.connectSlotsByName(Form)

    def loadAttendanceFromFirebase(self):
        """تحميل بيانات الحضور من Firebase"""
        try:
            # جلب البيانات من Firebase
            attendance_records = firebase_db.get_attendance_data(self.user_id)

            if attendance_records:
                # تحويل البيانات إلى التنسيق المطلوب
                # استخدام dict لضمان أن كل تاريخ يظهر مرة واحدة فقط
                self.attendanceData = {}

                # ترتيب السجلات حسب timestamp (الأحدث أولاً)
                sorted_records = sorted(
                    attendance_records,
                    key=lambda x: x.get('timestamp', 0)
                )

                for record in sorted_records:
                    # الحصول على التاريخ الكامل
                    full_date = record.get('fullDate', '')
                    status = record.get('status', 'present')
                    timestamp = record.get('timestamp', 0)

                    if full_date:
                        # تحويل التاريخ من أي فورمات إلى YYYY-MM-DD
                        normalized_date = self.normalize_date(full_date)

                        if normalized_date:
                            # تحديث الحالة (آخر سجل هو الصحيح)
                            self.attendanceData[normalized_date] = status
                            print(f"📅 {normalized_date}: {status} (أصلي: {full_date})")

                print(f"✅ تم تحميل {len(self.attendanceData)} يوم فريد")
                print(f"📋 البيانات النهائية:")
                for date, status in sorted(self.attendanceData.items()):
                    print(f"   {date} -> {status}")
            else:
                print("⚠️ لا توجد بيانات حضور")
                self.attendanceData = {}

        except Exception as e:
            print(f"❌ خطأ في تحميل البيانات: {e}")
            import traceback
            traceback.print_exc()
            self.attendanceData = {}

        # تحديث التقويم والإحصائيات
        self.updateCalendar()
        self.updateStats()

    def normalize_date(self, date_str):
        """تحويل التاريخ من أي فورمات إلى YYYY-MM-DD"""
        try:
            # إزالة أي مسافات
            date_str = str(date_str).strip()

            print(f"🔍 محاولة تحويل التاريخ: '{date_str}'")

            # محاولة التعامل مع فورمات YYYY-MM-DD (صحيح بالفعل)
            if '-' in date_str:
                parts = date_str.split('-')
                if len(parts) == 3:
                    # تحديد إذا كان YYYY-MM-DD أو DD-MM-YYYY
                    try:
                        # لو الجزء الأول سنة (4 أرقام أو أكبر من 31)
                        if len(parts[0]) == 4 or int(parts[0]) > 31:
                            # YYYY-MM-DD
                            year, month, day = parts
                            normalized = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
                            print(f"✅ تحويل من YYYY-MM-DD: {date_str} -> {normalized}")
                            return normalized
                        else:
                            # DD-MM-YYYY
                            day, month, year = parts
                            normalized = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
                            print(f"✅ تحويل من DD-MM-YYYY: {date_str} -> {normalized}")
                            return normalized
                    except ValueError as e:
                        print(f"⚠️ خطأ في تحويل الأجزاء: {e}")

            # محاولة التعامل مع فورمات DD/MM/YYYY
            if '/' in date_str:
                parts = date_str.split('/')
                if len(parts) == 3:
                    day, month, year = parts
                    normalized = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
                    print(f"✅ تحويل من DD/MM/YYYY: {date_str} -> {normalized}")
                    return normalized

            # محاولة استخدام datetime.strptime
            for fmt in ['%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y', '%Y/%m/%d']:
                try:
                    dt = datetime.strptime(date_str, fmt)
                    normalized = dt.strftime('%Y-%m-%d')
                    print(f"✅ تحويل باستخدام strptime ({fmt}): {date_str} -> {normalized}")
                    return normalized
                except:
                    continue

            # لو مش معروف الفورمات، ارجع التاريخ كما هو
            print(f"⚠️ فشل تحويل التاريخ: {date_str}")
            return date_str

        except Exception as e:
            print(f"❌ خطأ في تحويل التاريخ {date_str}: {e}")
            return None

    def updateCalendar(self):
        """تحديث التقويم بالشهر الحالي"""
        year = self.currentDate.year
        month = self.currentDate.month

        print(f"\n📅 تحديث التقويم: {year}-{month:02d}")
        print(f"📋 البيانات المتاحة: {list(self.attendanceData.keys())}")

        # Update month label
        monthNames = ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو",
                      "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"]
        self.currentMonthLabel.setText(f"{monthNames[month - 1]} {year}")

        # Get calendar for month
        cal = calendar.monthcalendar(year, month)
        self.calendarWidget.setRowCount(len(cal))

        # تحديد اليوم الحالي
        today = datetime.now()
        is_current_month = (year == today.year and month == today.month)

        for row, week in enumerate(cal):
            for col, day in enumerate(week):
                item = QtWidgets.QTableWidgetItem()

                if day == 0:
                    item.setText("")
                    item.setBackground(QtGui.QColor("#F5F5F5"))
                else:
                    item.setText(str(day))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)

                    # تحديد تاريخ اليوم
                    date_str = f"{year}-{month:02d}-{day:02d}"

                    print(f"🔍 فحص التاريخ: {date_str}")
                    print(f"   موجود في البيانات؟ {date_str in self.attendanceData}")

                    # تحديد إذا كان اليوم في الماضي أو المستقبل
                    day_date = datetime(year, month, day)
                    is_past = day_date < today.replace(hour=0, minute=0, second=0, microsecond=0)
                    is_today = (day == today.day and is_current_month)
                    is_future = day_date > today

                    # تحديد اللون حسب الحضور
                    if date_str in self.attendanceData:
                        status = self.attendanceData[date_str]
                        print(f"✅ تم العثور على: {date_str} -> {status}")

                        if status == "present":
                            item.setBackground(QtGui.QColor("#4CAF50"))  # أخضر للحضور
                            item.setForeground(QtGui.QColor("white"))
                        elif status == "absent":
                            item.setBackground(QtGui.QColor("#F44336"))  # أحمر للغياب
                            item.setForeground(QtGui.QColor("white"))

                        font = item.font()
                        font.setBold(True)
                        font.setPointSize(14)
                        item.setFont(font)

                    # لو مش مسجل حضور
                    else:
                        # الأيام الماضية (بدون حضور) = غياب (أحمر)
                        if is_past:
                            item.setBackground(QtGui.QColor("#F44336"))  # أحمر للغياب
                            item.setForeground(QtGui.QColor("white"))
                            font = item.font()
                            font.setBold(True)
                            font.setPointSize(12)
                            item.setFont(font)
                            print(f"   ❌ يوم ماضي بدون حضور -> غياب")

                        # اليوم الحالي
                        elif is_today:
                            item.setBackground(QtGui.QColor("#BBDEFB"))  # أزرق فاتح
                            font = item.font()
                            font.setBold(True)
                            font.setPointSize(12)
                            item.setFont(font)
                            print(f"   📍 اليوم الحالي")

                        # الأيام المستقبلية
                        elif is_future:
                            item.setBackground(QtGui.QColor("white"))  # أبيض عادي
                            print(f"   ⏳ يوم مستقبلي")

                        # أي حالة تانية (يوم عادي)
                        else:
                            item.setBackground(QtGui.QColor("white"))

                self.calendarWidget.setItem(row, col, item)
    def updateStats(self):
        """تحديث إحصائيات الحضور والغياب"""
        present_count = sum(1 for status in self.attendanceData.values() if status == "present")
        absent_count = sum(1 for status in self.attendanceData.values() if status == "absent")

        self.presentLabel.setText(f"✓ حضور: {present_count} يوم")
        self.absentLabel.setText(f"✗ غياب: {absent_count} يوم")

    def prevMonth(self):
        """الشهر السابق"""
        if self.currentDate.month == 1:
            self.currentDate = self.currentDate.replace(year=self.currentDate.year - 1, month=12)
        else:
            self.currentDate = self.currentDate.replace(month=self.currentDate.month - 1)
        self.updateCalendar()

    def nextMonth(self):
        """الشهر التالي"""
        if self.currentDate.month == 12:
            self.currentDate = self.currentDate.replace(year=self.currentDate.year + 1, month=1)
        else:
            self.currentDate = self.currentDate.replace(month=self.currentDate.month + 1)
        self.updateCalendar()

    def refreshCalendar(self):
        """تحديث التقويم"""
        self.currentDate = datetime.now()
        self.loadAttendanceFromFirebase()  # إعادة تحميل البيانات من Firebase
        QtWidgets.QMessageBox.information(self.Form, "تحديث", "تم تحديث البيانات بنجاح!")

    def showAbsentDays(self):
        """عرض قائمة بأيام الغياب"""
        absent_days = [date for date, status in self.attendanceData.items() if status == "absent"]

        if absent_days:
            absent_list = "\n".join([f"• {date}" for date in sorted(absent_days)])
            message = f"أيام الغياب ({len(absent_days)} يوم):\n\n{absent_list}"
        else:
            message = "لا توجد أيام غياب مسجلة!"

        msg_box = QtWidgets.QMessageBox(self.Form)
        msg_box.setWindowTitle("أيام الغياب")
        msg_box.setText(message)
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: white;
            }
            QLabel {
                font-size: 12pt;
                color: #333;
            }
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-weight: bold;
                padding: 8px 20px;
                border-radius: 5px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        msg_box.exec_()

    def goBackHome(self):
        """العودة للصفحة الرئيسية"""
        try:
            from home_page import Ui_HomeForm
            self.homeWindow = QtWidgets.QWidget()
            self.homeUI = Ui_HomeForm()
            self.homeUI.setupUi(self.homeWindow)
            self.homeWindow.show()
            self.Form.close()
        except ImportError:
            QtWidgets.QMessageBox.warning(self.Form, "خطأ", "لا يمكن العودة للصفحة الرئيسية")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_AttendanceForm()
    ui.setupUi(Form, user_id="6380F32F", student_code="250104330")
    Form.show()
    sys.exit(app.exec_())