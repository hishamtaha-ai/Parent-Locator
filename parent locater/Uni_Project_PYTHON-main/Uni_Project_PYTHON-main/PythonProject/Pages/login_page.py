from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json
from session_manager import SessionManager

# إعدادات Firebase
FIREBASE_DATABASE_URL = "https://student-bus-sys-default-rtdb.firebaseio.com"


class FirebaseDatabase:
    """مكتبة للتعامل مع Realtime Database"""

    def __init__(self, database_url):
        self.database_url = database_url

    def verify_login(self, email, password):
        """التحقق من الإيميل والباسورد من Database مباشرة"""
        url = f"{self.database_url}/students.json"
        response = requests.get(url)

        if response.status_code == 200:
            students = response.json()
            if students:
                # البحث عن المستخدم بالإيميل والباسورد
                for user_id, user_data in students.items():
                    if (user_data.get('mail') == email and
                            str(user_data.get('password')) == password):
                        return {
                            'success': True,
                            'user_id': user_id,
                            'user_data': user_data
                        }

        return {'success': False, 'error': 'Invalid email or password'}


# تهيئة Firebase
firebase_db = FirebaseDatabase(FIREBASE_DATABASE_URL)


class Ui_LoginForm(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(466, 741)
        Form.setStyleSheet("""
            QLineEdit {
                border: 1px solid #E0E0E0;
                border-radius: 12px;
                padding: 8px;
                background-color: #F7F7F7;
            }
            QTextEdit {
                border: 1px solid #E0E0E0;
                border-radius: 12px;
                background-color: #F7F7F7;
                padding: 10px;
                font-size: 15px;
                color: #1A1A1A;
            }
            font-size: 18px;
            font-weight: bold;
        """)

        # Main layout
        self.mainLayout = QtWidgets.QVBoxLayout(Form)
        self.mainLayout.setContentsMargins(30, 20, 30, 20)
        self.mainLayout.setSpacing(15)

        # Top corner logo
        topLayout = QtWidgets.QHBoxLayout()
        self.logoCorner = QtWidgets.QLabel(Form)
        self.logoCorner.setText("")
        try:
            self.logoCorner.setPixmap(QtGui.QPixmap(
                "C:/Users/fares/Desktop/gui/app-main/Elsewedy-University-of-Technology-Egypt-96010-1698259526-removebg-preview.png"))
            self.logoCorner.setScaledContents(True)
        except:
            pass
        self.logoCorner.setMaximumSize(QtCore.QSize(120, 120))
        self.logoCorner.setMinimumSize(QtCore.QSize(100, 100))
        self.logoCorner.setObjectName("logoCorner")
        topLayout.addWidget(self.logoCorner)
        topLayout.addStretch()
        self.mainLayout.addLayout(topLayout)

        self.mainLayout.addStretch(1)

        # Title 1
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setStyleSheet("color: rgb(26, 26, 26); font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.mainLayout.addWidget(self.label_2)

        # Title 2
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\"; color: rgb(26, 26, 26);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.mainLayout.addWidget(self.label_3)

        self.mainLayout.addSpacing(20)

        # Email field
        self.textEdit = QtWidgets.QLineEdit(Form)
        self.textEdit.setMaximumSize(QtCore.QSize(700, 51))
        self.textEdit.setMinimumSize(QtCore.QSize(200, 51))
        self.textEdit.setStyleSheet(
            "background-color: rgb(244, 244, 244); border: 1px solid #E0E0E0; border-radius: 12px; padding: 8px; font-size: 15px;")
        self.textEdit.setObjectName("textEdit")
        self.mainLayout.addWidget(self.textEdit)

        # Password field with toggle button
        passwordLayout = QtWidgets.QHBoxLayout()
        self.textEdit_2 = QtWidgets.QLineEdit(Form)
        self.textEdit_2.setMaximumSize(QtCore.QSize(700, 51))
        self.textEdit_2.setMinimumSize(QtCore.QSize(200, 51))
        self.textEdit_2.setStyleSheet(
            "background-color: rgb(244, 244, 244); border: 1px solid #E0E0E0; border-radius: 12px; padding: 8px; padding-right: 45px; font-size: 15px;")
        self.textEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.returnPressed.connect(self.goToHomePage)

        self.togglePasswordButton = QtWidgets.QPushButton(Form)
        self.togglePasswordButton.setMaximumSize(QtCore.QSize(40, 40))
        self.togglePasswordButton.setMinimumSize(QtCore.QSize(40, 40))
        self.togglePasswordButton.setStyleSheet(
            "QPushButton { background-color: transparent; border: none; font-size: 18px; } QPushButton:hover { background-color: rgba(0, 0, 0, 0.05); border-radius: 20px; }")
        self.togglePasswordButton.setText("👁")
        self.togglePasswordButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.togglePasswordButton.setObjectName("togglePasswordButton")
        self.togglePasswordButton.clicked.connect(self.togglePasswordVisibility)

        passwordLayout.addWidget(self.textEdit_2)
        passwordLayout.addWidget(self.togglePasswordButton)
        passwordLayout.setContentsMargins(0, 0, 0, 0)
        passwordLayout.setSpacing(-45)
        self.mainLayout.addLayout(passwordLayout)

        # Error message label
        self.errorLabel = QtWidgets.QLabel(Form)
        self.errorLabel.setStyleSheet("color: red; font-size: 12px;")
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setWordWrap(True)
        self.errorLabel.setObjectName("errorLabel")
        self.errorLabel.hide()
        self.mainLayout.addWidget(self.errorLabel)

        self.mainLayout.addSpacing(10)

        # Login button
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(700, 50))
        self.pushButton.setStyleSheet(
            "QPushButton { background-color: #F0682E; color: white; font-size: 28px; font-weight: bold; border-radius: 18px; padding: 6px 14px; border:2px solid #F0682E } QPushButton:pressed { background-color: #d95724; padding-left: 8px; padding-top: 8px; } QPushButton:disabled { background-color: #CCCCCC; border-color: #CCCCCC; }")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.goToHomePage)
        self.mainLayout.addWidget(self.pushButton)

        self.mainLayout.addStretch(2)

        # Footer text
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet(
            "font: 10pt \"MS Shell Dlg 2\"; color: rgb(87, 59, 131); text-decoration: underline;")
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setObjectName("label_4")
        self.label_4.mousePressEvent = lambda event: self.goToSignupPage()
        self.mainLayout.addWidget(self.label_4)

        self.mainLayout.addStretch(1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def togglePasswordVisibility(self):
        if self.textEdit_2.echoMode() == QtWidgets.QLineEdit.Password:
            self.textEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.togglePasswordButton.setText("🙈")
        else:
            self.textEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
            self.togglePasswordButton.setText("👁")

    def showError(self, message):
        """عرض رسالة خطأ"""
        self.errorLabel.setText(message)
        self.errorLabel.show()
        QtCore.QTimer.singleShot(5000, self.errorLabel.hide)

    def goToHomePage(self):
        """التحقق من البيانات والانتقال لصفحة الـ Home"""
        email = self.textEdit.text().strip()
        password = self.textEdit_2.text().strip()

        # التحقق من إدخال البيانات
        if not email or not password:
            self.showError("⚠️ Please enter both email and password")
            return

        # تعطيل الزر أثناء المعالجة
        self.pushButton.setEnabled(False)
        self.pushButton.setText("Loading...")
        self.errorLabel.hide()

        try:
            # التحقق من البيانات مباشرة من Database
            result = firebase_db.verify_login(email, password)

            if result['success']:
                # تسجيل دخول ناجح
                user_id = result['user_id']  # Card UID
                user_data = result['user_data']

                print(f"✅ Login successful!")
                print(f"   Card UID: {user_id}")
                print(f"   Name: {user_data.get('name')}")
                print(f"   Code: {user_data.get('code')}")
                print(f"   Email: {user_data.get('mail')}")

                # ✅ حفظ البيانات في Session
                session = SessionManager()
                session.set_user_data(
                    card_uid=user_id,
                    student_code=user_data.get('code', ''),
                    name=user_data.get('name', ''),
                    email=user_data.get('mail', ''),
                    password=password
                )

                # الانتقال للصفحة الرئيسية
                from home_page import Ui_HomeForm

                self.homeWindow = QtWidgets.QWidget()
                self.homeUI = Ui_HomeForm()
                self.homeUI.setupUi(self.homeWindow)
                self.homeWindow.show()
                self.Form.close()
            else:
                self.showError("❌ Invalid email or password")
                self.pushButton.setEnabled(True)
                self.pushButton.setText("Login")

        except Exception as e:
            error_message = str(e)
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
            self.showError(f"❌ Connection error: {error_message}")
            self.pushButton.setEnabled(True)
            self.pushButton.setText("Login")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.textEdit.setPlaceholderText(_translate("Form", "Email"))
        self.textEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Login"))
        self.label_2.setText(_translate("Form", "ElSewedy University Of Polytechnic Egypt"))
        self.label_3.setText(_translate("Form", "Bus System Locator"))
        self.label_4.setText(_translate("Form", "Don't have an account? Sign up"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())