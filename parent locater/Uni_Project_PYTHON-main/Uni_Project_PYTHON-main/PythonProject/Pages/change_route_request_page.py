from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangeRouteRequestForm(object):
    def setupUi(self, Form, current_route=""):
        self.Form = Form
        self.current_route = current_route
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(466, 741)
        Form.setStyleSheet("QWidget { background-color: #FFFFFF; }")

        # Main layout
        self.mainLayout = QtWidgets.QVBoxLayout(Form)
        self.mainLayout.setContentsMargins(30, 20, 30, 20)
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
        self.label_title.setStyleSheet("color: rgb(26, 26, 26); font: 75 28pt \"MS Shell Dlg 2\";")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setText("طلب تغيير الخط")
        self.mainLayout.addWidget(self.label_title)

        # Subtitle
        self.label_subtitle = QtWidgets.QLabel(Form)
        self.label_subtitle.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color: rgb(100, 100, 100);")
        self.label_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle.setText("املأ البيانات المطلوبة")
        self.mainLayout.addWidget(self.label_subtitle)

        self.mainLayout.addSpacing(20)

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
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: #FF9800;
                border-radius: 5px;
            }
        """)

        # Container widget
        self.scrollWidget = QtWidgets.QWidget()
        self.formLayout = QtWidgets.QVBoxLayout(self.scrollWidget)
        self.formLayout.setSpacing(20)
        self.formLayout.setContentsMargins(0, 0, 0, 0)

        # Style for input fields
        inputStyle = """
            QLineEdit {
                background-color: #F5F5F5;
                border: 2px solid #E0E0E0;
                border-radius: 10px;
                padding: 15px;
                font-size: 14pt;
                color: #1A1A1A;
            }
            QLineEdit:focus {
                border: 2px solid #FF9800;
                background-color: #FFFFFF;
            }
        """

        comboStyle = """
            QComboBox {
                background-color: #F5F5F5;
                border: 2px solid #E0E0E0;
                border-radius: 10px;
                padding: 15px;
                font-size: 14pt;
                color: #1A1A1A;
            }
            QComboBox:focus {
                border: 2px solid #FF9800;
                background-color: #FFFFFF;
            }
            QComboBox::drop-down {
                border: none;
                width: 30px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 8px solid #FF9800;
                margin-right: 10px;
            }
        """

        labelStyle = "font: bold 12pt \"MS Shell Dlg 2\"; color: rgb(26, 26, 26);"

        # كود الطالب
        label_student_code = QtWidgets.QLabel("كود الطالب *")
        label_student_code.setStyleSheet(labelStyle)
        self.formLayout.addWidget(label_student_code)

        self.input_student_code = QtWidgets.QLineEdit()
        self.input_student_code.setPlaceholderText("أدخل كود الطالب")
        self.input_student_code.setStyleSheet(inputStyle)
        self.input_student_code.setMinimumHeight(50)
        self.formLayout.addWidget(self.input_student_code)

        # الاسم الكامل
        label_full_name = QtWidgets.QLabel("الاسم الكامل *")
        label_full_name.setStyleSheet(labelStyle)
        self.formLayout.addWidget(label_full_name)

        self.input_full_name = QtWidgets.QLineEdit()
        self.input_full_name.setPlaceholderText("أدخل الاسم الكامل")
        self.input_full_name.setStyleSheet(inputStyle)
        self.input_full_name.setMinimumHeight(50)
        self.formLayout.addWidget(self.input_full_name)

        # رقم الهاتف
        label_phone = QtWidgets.QLabel("رقم الهاتف *")
        label_phone.setStyleSheet(labelStyle)
        self.formLayout.addWidget(label_phone)

        self.input_phone = QtWidgets.QLineEdit()
        self.input_phone.setPlaceholderText("01xxxxxxxxx")
        self.input_phone.setStyleSheet(inputStyle)
        self.input_phone.setMinimumHeight(50)
        self.formLayout.addWidget(self.input_phone)

        # البريد الإلكتروني
        label_email = QtWidgets.QLabel("البريد الإلكتروني *")
        label_email.setStyleSheet(labelStyle)
        self.formLayout.addWidget(label_email)

        self.input_email = QtWidgets.QLineEdit()
        self.input_email.setPlaceholderText("example@university.edu")
        self.input_email.setStyleSheet(inputStyle)
        self.input_email.setMinimumHeight(50)
        self.formLayout.addWidget(self.input_email)

        # الخط الحالي (غير قابل للتعديل)
        label_current_route = QtWidgets.QLabel("الخط الحالي")
        label_current_route.setStyleSheet(labelStyle)
        self.formLayout.addWidget(label_current_route)

        self.input_current_route = QtWidgets.QLineEdit()
        self.input_current_route.setText(current_route)
        self.input_current_route.setReadOnly(True)
        self.input_current_route.setStyleSheet("""
            QLineEdit {
                background-color: #E0E0E0;
                border: 2px solid #BDBDBD;
                border-radius: 10px;
                padding: 15px;
                font-size: 14pt;
                color: #757575;
            }
        """)
        self.input_current_route.setMinimumHeight(50)
        self.formLayout.addWidget(self.input_current_route)

        # الخط الجديد المطلوب
        label_new_route = QtWidgets.QLabel("الخط الجديد المطلوب *")
        label_new_route.setStyleSheet(labelStyle)
        self.formLayout.addWidget(label_new_route)

        self.combo_new_route = QtWidgets.QComboBox()
        self.combo_new_route.addItems([
            "اختر الخط الجديد",
            "خط 1 - القاهرة الجديدة",
            "خط 2 - مدينة نصر",
            "خط 3 - مصر الجديدة",
            "خط 4 - التجمع الخامس",
            "خط 5 - المعادي",
            "خط 6 - المقطم",
            "خط 7 - حلوان",
            "خط 8 - الشروق",
            "خط 9 - الرحاب",
            "خط 10 - مدينتي"
        ])
        self.combo_new_route.setStyleSheet(comboStyle)
        self.combo_new_route.setMinimumHeight(50)
        self.formLayout.addWidget(self.combo_new_route)

        # سبب التغيير
        label_reason = QtWidgets.QLabel("سبب طلب التغيير *")
        label_reason.setStyleSheet(labelStyle)
        self.formLayout.addWidget(label_reason)

        self.input_reason = QtWidgets.QTextEdit()
        self.input_reason.setPlaceholderText("اكتب سبب طلب تغيير الخط...")
        self.input_reason.setStyleSheet("""
            QTextEdit {
                background-color: #F5F5F5;
                border: 2px solid #E0E0E0;
                border-radius: 10px;
                padding: 15px;
                font-size: 12pt;
                color: #1A1A1A;
            }
            QTextEdit:focus {
                border: 2px solid #FF9800;
                background-color: #FFFFFF;
            }
        """)
        self.input_reason.setMinimumHeight(120)
        self.formLayout.addWidget(self.input_reason)

        self.formLayout.addSpacing(20)

        # زر الإرسال
        self.submitButton = QtWidgets.QPushButton("إرسال الطلب")
        self.submitButton.setMinimumSize(QtCore.QSize(0, 60))
        self.submitButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 18px;
                font-weight: bold;
                border-radius: 15px;
                border: none;
            }
            QPushButton:hover {
                background-color: #45A049;
            }
            QPushButton:pressed {
                background-color: #388E3C;
            }
        """)
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitButton.clicked.connect(self.submitRequest)
        self.formLayout.addWidget(self.submitButton)

        self.formLayout.addStretch()
        self.scrollArea.setWidget(self.scrollWidget)
        self.mainLayout.addWidget(self.scrollArea)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def goBackToRoutes(self):
        """الرجوع لصفحة Routes"""
        from routes_page import Ui_RoutesForm

        self.routesWindow = QtWidgets.QWidget()
        self.routesUI = Ui_RoutesForm()
        self.routesUI.setupUi(self.routesWindow)
        self.routesWindow.show()
        self.Form.close()

    def submitRequest(self):
        """إرسال طلب التغيير"""
        # التحقق من المدخلات
        student_code = self.input_student_code.text().strip()
        full_name = self.input_full_name.text().strip()
        phone = self.input_phone.text().strip()
        email = self.input_email.text().strip()
        new_route = self.combo_new_route.currentText()
        reason = self.input_reason.toPlainText().strip()

        if not student_code:
            self.showMessage("خطأ", "يرجى إدخال كود الطالب")
            return

        if not full_name:
            self.showMessage("خطأ", "يرجى إدخال الاسم الكامل")
            return

        if not phone:
            self.showMessage("خطأ", "يرجى إدخال رقم الهاتف")
            return

        if not email:
            self.showMessage("خطأ", "يرجى إدخال البريد الإلكتروني")
            return

        if new_route == "اختر الخط الجديد":
            self.showMessage("خطأ", "يرجى اختيار الخط الجديد")
            return

        if not reason:
            self.showMessage("خطأ", "يرجى كتابة سبب طلب التغيير")
            return

        # هنا يمكنك إضافة كود لحفظ الطلب في قاعدة البيانات
        self.showMessage("نجح", "تم إرسال طلبك بنجاح!\nسيتم مراجعته والرد عليك قريباً")

        # الرجوع لصفحة Routes بعد الإرسال
        self.goBackToRoutes()

    def showMessage(self, title, message):
        """عرض رسالة للمستخدم"""
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: white;
            }
            QMessageBox QLabel {
                font-size: 12pt;
                color: #1A1A1A;
            }
            QPushButton {
                background-color: #FF9800;
                color: white;
                font-size: 12pt;
                font-weight: bold;
                border-radius: 5px;
                padding: 8px 20px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
        """)
        msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_ChangeRouteRequestForm()
    ui.setupUi(Form, "خط 3 - مصر الجديدة")
    Form.show()
    sys.exit(app.exec_())