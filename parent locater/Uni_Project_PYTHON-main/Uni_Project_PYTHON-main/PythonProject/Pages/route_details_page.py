from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RouteDetailsForm(object):
    def setupUi(self, Form, route_name):
        self.Form = Form
        self.route_name = route_name

        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(466, 741)
        Form.setStyleSheet("QWidget { background-color: #FFFFFF; }")

        # Main layout
        self.mainLayout = QtWidgets.QVBoxLayout(Form)
        self.mainLayout.setContentsMargins(20, 20, 20, 20)
        self.mainLayout.setSpacing(15)

        # Header with back button
        headerLayout = QtWidgets.QHBoxLayout()

        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setMinimumSize(QtCore.QSize(50, 50))
        self.backButton.setMaximumSize(QtCore.QSize(50, 50))
        self.backButton.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                font-size: 24px;
                font-weight: bold;
                border-radius: 25px;
                border: none;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
            QPushButton:pressed {
                background-color: #E65100;
            }
        """)
        self.backButton.setText("←")
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.clicked.connect(self.goBackToRoutes)
        headerLayout.addWidget(self.backButton)
        headerLayout.addStretch()
        self.mainLayout.addLayout(headerLayout)

        # Title
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setStyleSheet("color: #FF9800; font: 75 24pt 'MS Shell Dlg 2';")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setText(route_name)
        self.label_title.setWordWrap(True)
        self.mainLayout.addWidget(self.label_title)

        self.mainLayout.addSpacing(10)

        # Scroll Area
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background: #F5F5F5;
                width: 8px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #FF9800;
                border-radius: 4px;
            }
        """)

        # Container widget
        self.scrollWidget = QtWidgets.QWidget()
        self.scrollLayout = QtWidgets.QVBoxLayout(self.scrollWidget)
        self.scrollLayout.setSpacing(15)
        self.scrollLayout.setContentsMargins(5, 5, 5, 5)

        # معلومات السائق والحافلة
        self.addInfoSection()

        # جدول محطات الوقوف
        self.addStationsTable()

        self.scrollLayout.addStretch()
        self.scrollArea.setWidget(self.scrollWidget)
        self.mainLayout.addWidget(self.scrollArea)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def addInfoSection(self):
        """إضافة قسم معلومات السائق والحافلة"""
        # بيانات وهمية - استبدلها ببياناتك الحقيقية
        bus_info = self.getBusInfo(self.route_name)

        # Info Card
        infoCard = QtWidgets.QFrame(self.scrollWidget)
        infoCard.setStyleSheet("""
            QFrame {
                background-color: #FFF3E0;
                border-radius: 15px;
                padding: 15px;
            }
        """)
        infoLayout = QtWidgets.QVBoxLayout(infoCard)
        infoLayout.setSpacing(10)

        # معلومات السائق
        driverLabel = QtWidgets.QLabel(infoCard)
        driverLabel.setStyleSheet("font: 16pt 'MS Shell Dlg 2'; color: #1A1A1A; font-weight: bold;")
        driverLabel.setText(f" السائق: {bus_info['driver']}")
        infoLayout.addWidget(driverLabel)

        # رقم الحافلة
        busNumberLabel = QtWidgets.QLabel(infoCard)
        busNumberLabel.setStyleSheet("font: 14pt 'MS Shell Dlg 2'; color: #424242;")
        busNumberLabel.setText(f"🚌 رقم الحافلة: {bus_info['bus_number']}")
        infoLayout.addWidget(busNumberLabel)

        # نوع الحافلة
        busTypeLabel = QtWidgets.QLabel(infoCard)
        busTypeLabel.setStyleSheet("font: 14pt 'MS Shell Dlg 2'; color: #424242;")
        busTypeLabel.setText(f"🔧 نوع الحافلة: {bus_info['bus_type']}")
        infoLayout.addWidget(busTypeLabel)

        # عدد المقاعد
        seatsLabel = QtWidgets.QLabel(infoCard)
        seatsLabel.setStyleSheet("font: 14pt 'MS Shell Dlg 2'; color: #424242;")
        seatsLabel.setText(f"💺 عدد المقاعد: {bus_info['seats']}")
        infoLayout.addWidget(seatsLabel)

        # رقم هاتف السائق
        phoneLabel = QtWidgets.QLabel(infoCard)
        phoneLabel.setStyleSheet("font: 14pt 'MS Shell Dlg 2'; color: #424242;")
        phoneLabel.setText(f"📞 هاتف السائق: {bus_info['phone']}")
        infoLayout.addWidget(phoneLabel)

        self.scrollLayout.addWidget(infoCard)

    def addStationsTable(self):
        """إضافة جدول محطات الوقوف"""
        # عنوان الجدول
        tableTitle = QtWidgets.QLabel(self.scrollWidget)
        tableTitle.setStyleSheet("font: 18pt 'MS Shell Dlg 2'; color: #FF9800; font-weight: bold;")
        tableTitle.setText("⏰ مواعيد المحطات")
        tableTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollLayout.addWidget(tableTitle)

        # إنشاء الجدول
        self.tableWidget = QtWidgets.QTableWidget(self.scrollWidget)

        # بيانات المحطات - استبدلها ببياناتك
        stations_data = self.getStationsData(self.route_name)

        self.tableWidget.setRowCount(len(stations_data))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["المحطة", "وقت الوصول", "ملاحظات"])

        # تنسيق الجدول
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 2px solid #FF9800;
                border-radius: 10px;
                gridline-color: #FFE0B2;
                font-size: 13pt;
            }
            QTableWidget::item {
                padding: 10px;
                border-bottom: 1px solid #FFE0B2;
            }
            QTableWidget::item:selected {
                background-color: #FFE0B2;
                color: #1A1A1A;
            }
            QHeaderView::section {
                background-color: #FF9800;
                color: white;
                padding: 10px;
                border: none;
                font-size: 14pt;
                font-weight: bold;
            }
        """)

        # ملء البيانات
        for row, station in enumerate(stations_data):
            # المحطة
            stationItem = QtWidgets.QTableWidgetItem(station['name'])
            stationItem.setTextAlignment(QtCore.Qt.AlignCenter)
            stationItem.setFlags(stationItem.flags() & ~QtCore.Qt.ItemIsEditable)
            self.tableWidget.setItem(row, 0, stationItem)

            # وقت الوصول
            timeItem = QtWidgets.QTableWidgetItem(station['time'])
            timeItem.setTextAlignment(QtCore.Qt.AlignCenter)
            timeItem.setFlags(timeItem.flags() & ~QtCore.Qt.ItemIsEditable)
            self.tableWidget.setItem(row, 1, timeItem)

            # ملاحظات
            notesItem = QtWidgets.QTableWidgetItem(station['notes'])
            notesItem.setTextAlignment(QtCore.Qt.AlignCenter)
            notesItem.setFlags(notesItem.flags() & ~QtCore.Qt.ItemIsEditable)
            self.tableWidget.setItem(row, 2, notesItem)

        # ضبط عرض الأعمدة
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        # ضبط ارتفاع الصفوف
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setVisible(False)

        # تحديد ارتفاع الجدول
        table_height = (len(stations_data) * 50) + 60  # 60 للـ header
        self.tableWidget.setMinimumHeight(min(table_height, 400))

        self.scrollLayout.addWidget(self.tableWidget)

    def getBusInfo(self, route_name):
        """الحصول على معلومات الحافلة والسائق - بيانات وهمية"""
        # هنا تقدر تربطها بقاعدة بيانات
        bus_data = {
            "خط 1 - القاهرة الجديدة": {
                "driver": "أحمد محمد علي",
                "bus_number": "BUS-101",
                "bus_type": "مرسيدس 2022",
                "seats": "50 مقعد",
                "phone": "01012345678"
            },
            "خط 2 - مدينة نصر": {
                "driver": "محمود حسن",
                "bus_number": "BUS-102",
                "bus_type": "فولفو 2021",
                "seats": "45 مقعد",
                "phone": "01098765432"
            },
            "خط 3 - مصر الجديدة": {
                "driver": "خالد أحمد",
                "bus_number": "BUS-103",
                "bus_type": "مرسيدس 2023",
                "seats": "48 مقعد",
                "phone": "01123456789"
            },
            "خط 4 - التجمع الخامس": {
                "driver": "عمر سعيد",
                "bus_number": "BUS-104",
                "bus_type": "سكانيا 2022",
                "seats": "52 مقعد",
                "phone": "01156789012"
            },
            "خط 5 - المعادي": {
                "driver": "يوسف كمال",
                "bus_number": "BUS-105",
                "bus_type": "فولفو 2023",
                "seats": "46 مقعد",
                "phone": "01187654321"
            },
        }

        # لو الخط مش موجود، نرجع بيانات افتراضية
        return bus_data.get(route_name, {
            "driver": "غير محدد",
            "bus_number": "N/A",
            "bus_type": "غير محدد",
            "seats": "غير محدد",
            "phone": "غير متاح"
        })

    def getStationsData(self, route_name):
        """الحصول على بيانات المحطات - بيانات وهمية"""
        # هنا تقدر تربطها بقاعدة بيانات
        stations = {
            "خط 1 - القاهرة الجديدة": [
                {"name": "🏫 الجامعة", "time": "6:00 ص", "notes": "محطة البداية"},
                {"name": "🏪 سيتي سنتر", "time": "6:15 ص", "notes": "5 دقائق"},
                {"name": "🏥 مستشفى السلام", "time": "6:30 ص", "notes": "5 دقائق"},
                {"name": "🏢 التجمع الأول", "time": "6:45 ص", "notes": "10 دقائق"},
                {"name": "🎯 القاهرة الجديدة", "time": "7:00 ص", "notes": "محطة النهاية"},
            ],
            "خط 2 - مدينة نصر": [
                {"name": "🏫 الجامعة", "time": "6:30 ص", "notes": "محطة البداية"},
                {"name": "🚉 مترو المرج", "time": "6:50 ص", "notes": "5 دقائق"},
                {"name": "🏬 سيتي ستارز", "time": "7:10 ص", "notes": "10 دقائق"},
                {"name": "🎯 مدينة نصر", "time": "7:30 ص", "notes": "محطة النهاية"},
            ],
            "خط 3 - مصر الجديدة": [
                {"name": "🏫 الجامعة", "time": "7:00 ص", "notes": "محطة البداية"},
                {"name": "✈️ مطار القاهرة", "time": "7:20 ص", "notes": "5 دقائق"},
                {"name": "🏛️ المتحف", "time": "7:35 ص", "notes": "5 دقائق"},
                {"name": "🎯 مصر الجديدة", "time": "7:50 ص", "notes": "محطة النهاية"},
            ],
            "خط 4 - التجمع الخامس": [
                {"name": "🏫 الجامعة", "time": "6:00 ص", "notes": "محطة البداية"},
                {"name": "🏪 كايرو فيستيفال", "time": "6:20 ص", "notes": "5 دقائق"},
                {"name": "🏢 التجمع الثالث", "time": "6:40 ص", "notes": "10 دقائق"},
                {"name": "🎯 التجمع الخامس", "time": "7:00 ص", "notes": "محطة النهاية"},
            ],
            "خط 5 - المعادي": [
                {"name": "🏫 الجامعة", "time": "7:30 ص", "notes": "محطة البداية"},
                {"name": "🌉 كوبري 15 مايو", "time": "7:50 ص", "notes": "5 دقائق"},
                {"name": "🏬 كارفور المعادي", "time": "8:10 ص", "notes": "10 دقائق"},
                {"name": "🎯 المعادي", "time": "8:30 ص", "notes": "محطة النهاية"},
            ],
        }

        # لو الخط مش موجود، نرجع محطات افتراضية
        return stations.get(route_name, [
            {"name": "محطة 1", "time": "غير محدد", "notes": "لا توجد معلومات"},
        ])

    def goBackToRoutes(self):
        """الرجوع لصفحة Routes"""
        from routes_page import Ui_RoutesForm

        self.routesWindow = QtWidgets.QWidget()
        self.routesUI = Ui_RoutesForm()
        self.routesUI.setupUi(self.routesWindow)
        self.routesWindow.show()
        self.Form.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_RouteDetailsForm()
    ui.setupUi(Form, "خط 1 - القاهرة الجديدة")
    Form.show()
    sys.exit(app.exec_())