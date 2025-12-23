from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from session_manager import SessionManager


class Ui_ProfileForm(object):
    def setupUi(self, Form):
        self.Form = Form

        # ✅ الحصول على البيانات من Session بدلاً من Parameters
        session = SessionManager()
        self.card_uid = session.get_card_uid()
        self.user_email = session.get_email()
        self.student_name = session.get_name()

        print(f"\n📋 تحميل صفحة Profile:")
        print(f"   Card UID: {self.card_uid}")
        print(f"   Email: {self.user_email}")
        print(f"   Name: {self.student_name}\n")

        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(466, 600)
        Form.setStyleSheet("QWidget { background-color: #FFFFFF; }")

        # Firebase URL
        self.FIREBASE_URL = "https://student-bus-sys-default-rtdb.firebaseio.com"

        # Main layout
        self.mainLayout = QtWidgets.QVBoxLayout(Form)
        self.mainLayout.setContentsMargins(30, 20, 30, 20)
        self.mainLayout.setSpacing(10)

        # Top corner logo with back button
        topLayout = QtWidgets.QHBoxLayout()

        # Back button
        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setText("← رجوع")
        self.backButton.setMaximumSize(QtCore.QSize(100, 40))
        self.backButton.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                color: #333;
                font-size: 14px;
                border-radius: 8px;
                border: 2px solid #ddd;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
                border: 2px solid #bbb;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.clicked.connect(self.goBackToSettings)
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

        self.mainLayout.addSpacing(10)

        # Profile Picture
        profilePicLayout = QtWidgets.QHBoxLayout()
        profilePicLayout.addStretch()

        self.profilePicLabel = QtWidgets.QLabel(Form)
        self.profilePicLabel.setMinimumSize(QtCore.QSize(100, 100))
        self.profilePicLabel.setMaximumSize(QtCore.QSize(100, 100))
        self.profilePicLabel.setStyleSheet("""
            QLabel {
                background-color: #4CAF50;
                border-radius: 50px;
                font-size: 42px;
                color: white;
            }
        """)
        self.profilePicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.profilePicLabel.setText("🔐")
        profilePicLayout.addWidget(self.profilePicLabel)

        profilePicLayout.addStretch()
        self.mainLayout.addLayout(profilePicLayout)

        self.mainLayout.addSpacing(5)

        # Title
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setStyleSheet("color: rgb(26, 26, 26); font: 75 24pt \"MS Shell Dlg 2\";")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setText("🔒 تغيير كلمة المرور")
        self.mainLayout.addWidget(self.label_title)

        # Subtitle
        self.label_subtitle = QtWidgets.QLabel(Form)
        self.label_subtitle.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color: rgb(100, 100, 100);")
        self.label_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle.setText("قم بتغيير كلمة المرور الخاصة بك")
        self.mainLayout.addWidget(self.label_subtitle)

        self.mainLayout.addSpacing(15)

        # Profile Info Container
        infoContainer = QtWidgets.QWidget(Form)
        infoContainer.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
                border-radius: 15px;
            }
        """)
        infoLayout = QtWidgets.QVBoxLayout(infoContainer)
        infoLayout.setSpacing(12)
        infoLayout.setContentsMargins(20, 15, 20, 15)

        # Current Email (Read-only)
        self.currentEmailLabel = QtWidgets.QLabel(infoContainer)
        self.currentEmailLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color: rgb(100, 100, 100);")
        self.currentEmailLabel.setText("📧 الإيميل")
        infoLayout.addWidget(self.currentEmailLabel)

        self.currentEmailDisplay = QtWidgets.QLabel(infoContainer)
        self.currentEmailDisplay.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 2px solid #ddd;
                border-radius: 8px;
                padding: 10px;
                font-size: 12pt;
                color: #666;
            }
        """)
        self.currentEmailDisplay.setText(self.user_email if self.user_email else "لا يوجد")
        infoLayout.addWidget(self.currentEmailDisplay)

        infoLayout.addSpacing(10)

        # New Password Field
        self.passwordLabel = QtWidgets.QLabel(infoContainer)
        self.passwordLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color: rgb(100, 100, 100);")
        self.passwordLabel.setText("🔒 كلمة مرور جديدة")
        infoLayout.addWidget(self.passwordLabel)

        self.passwordEdit = QtWidgets.QLineEdit(infoContainer)
        self.passwordEdit.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid #ddd;
                border-radius: 8px;
                padding: 10px;
                font-size: 12pt;
                color: #333;
            }
            QLineEdit:focus {
                border: 2px solid #4CAF50;
            }
        """)
        self.passwordEdit.setPlaceholderText("أدخل كلمة المرور الجديدة")
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        infoLayout.addWidget(self.passwordEdit)

        # Confirm New Password
        self.confirmPasswordLabel = QtWidgets.QLabel(infoContainer)
        self.confirmPasswordLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color: rgb(100, 100, 100);")
        self.confirmPasswordLabel.setText("🔒 تأكيد كلمة المرور")
        infoLayout.addWidget(self.confirmPasswordLabel)

        self.confirmPasswordEdit = QtWidgets.QLineEdit(infoContainer)
        self.confirmPasswordEdit.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid #ddd;
                border-radius: 8px;
                padding: 10px;
                font-size: 12pt;
                color: #333;
            }
            QLineEdit:focus {
                border: 2px solid #4CAF50;
            }
        """)
        self.confirmPasswordEdit.setPlaceholderText("أعد إدخال كلمة المرور")
        self.confirmPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        infoLayout.addWidget(self.confirmPasswordEdit)

        self.mainLayout.addWidget(infoContainer)

        self.mainLayout.addSpacing(15)

        # Save Button
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setText("💾 حفظ كلمة المرور الجديدة")
        self.saveButton.setMinimumSize(QtCore.QSize(0, 50))
        self.saveButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 10px;
                border: none;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveButton.clicked.connect(self.saveChanges)
        self.mainLayout.addWidget(self.saveButton)

        self.mainLayout.addStretch()

        QtCore.QMetaObject.connectSlotsByName(Form)

    def saveChanges(self):
        """حفظ كلمة المرور الجديدة في Firebase"""
        new_password = self.passwordEdit.text().strip()
        confirm_password = self.confirmPasswordEdit.text().strip()

        if not new_password:
            QtWidgets.QMessageBox.warning(
                self.Form,
                "تنبيه",
                "⚠️ يجب إدخال كلمة المرور الجديدة!"
            )
            return

        if new_password != confirm_password:
            QtWidgets.QMessageBox.warning(
                self.Form,
                "خطأ",
                "❌ كلمة المرور غير متطابقة!"
            )
            return

        if len(new_password) < 3:
            QtWidgets.QMessageBox.warning(
                self.Form,
                "خطأ",
                "❌ كلمة المرور يجب أن تكون 3 أحرف على الأقل!"
            )
            return

        reply = QtWidgets.QMessageBox.question(
            self.Form,
            "تأكيد",
            "هل أنت متأكد من تغيير كلمة المرور؟",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            success = self.updatePassword(new_password)

            if success:
                # ✅ تحديث كلمة المرور في Session أيضاً
                session = SessionManager()
                user_data = session.get_user_data()
                session.set_user_data(
                    card_uid=user_data['card_uid'],
                    student_code=user_data['student_code'],
                    name=user_data['name'],
                    email=user_data['email'],
                    password=new_password
                )

                QtWidgets.QMessageBox.information(
                    self.Form,
                    "نجاح",
                    "✅ تم تحديث كلمة المرور بنجاح!"
                )
                self.passwordEdit.clear()
                self.confirmPasswordEdit.clear()
            else:
                QtWidgets.QMessageBox.critical(
                    self.Form,
                    "خطأ",
                    "❌ فشل التحديث. حاول مرة أخرى!"
                )

    def updatePassword(self, new_password):
        """تحديث كلمة المرور في Firebase"""
        try:
            password_url = f"{self.FIREBASE_URL}/students/{self.card_uid}/password.json"
            response = requests.put(password_url, json=new_password, timeout=10)

            if response.status_code == 200:
                print("✅ تم تحديث كلمة المرور في Firebase")
                return True
            else:
                print(f"❌ فشل تحديث كلمة المرور: {response.text}")
                return False

        except Exception as e:
            print(f"❌ خطأ في التحديث: {e}")
            import traceback
            traceback.print_exc()
            return False

    def goBackToSettings(self):
        """العودة لصفحة Settings"""
        try:
            from settings import Ui_SettingsForm

            self.settingsWindow = QtWidgets.QWidget()
            self.settingsUI = Ui_SettingsForm()
            self.settingsUI.setupUi(self.settingsWindow)
            self.settingsWindow.show()
            self.Form.close()
        except ImportError:
            QtWidgets.QMessageBox.warning(self.Form, "خطأ", "لا يمكن فتح صفحة الإعدادات")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_ProfileForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())