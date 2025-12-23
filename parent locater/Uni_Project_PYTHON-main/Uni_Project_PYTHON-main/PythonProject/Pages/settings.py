from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsForm(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(466, 741)
        Form.setStyleSheet("QWidget { background-color: #FFFFFF; }")

        # Main layout
        self.mainLayout = QtWidgets.QVBoxLayout(Form)
        self.mainLayout.setContentsMargins(30, 20, 30, 20)
        self.mainLayout.setSpacing(15)

        # Top corner logo with back button
        topLayout = QtWidgets.QHBoxLayout()

        # Back button
        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setText("← Back")
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
        self.backButton.clicked.connect(self.goBackToHome)
        topLayout.addWidget(self.backButton)

        topLayout.addStretch()

        self.logoCorner = QtWidgets.QLabel(Form)
        self.logoCorner.setText("")
        self.logoCorner.setPixmap(QtGui.QPixmap(
            "C:/Users/fares/Desktop/gui/app-main/Elsewedy-University-of-Technology-Egypt-96010-1698259526-removebg-preview.png"))
        self.logoCorner.setScaledContents(True)
        self.logoCorner.setMaximumSize(QtCore.QSize(120, 120))
        self.logoCorner.setMinimumSize(QtCore.QSize(100, 100))
        self.logoCorner.setObjectName("logoCorner")
        topLayout.addWidget(self.logoCorner)

        self.mainLayout.addLayout(topLayout)

        self.mainLayout.addStretch(1)

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

        self.mainLayout.addSpacing(30)

        # Settings Buttons Grid Layout
        buttonsLayout = QtWidgets.QGridLayout()
        buttonsLayout.setSpacing(20)

        # Button 1 - Profile
        self.button1 = QtWidgets.QPushButton(Form)
        self.button1.setMinimumSize(QtCore.QSize(180, 180))
        self.button1.setMaximumSize(QtCore.QSize(200, 200))
        self.button1.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 20px;
                font-weight: bold;
                border-radius: 20px;
                border: 3px solid #4CAF50;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: white;
                color: #4CAF50;
                border: 3px solid #4CAF50;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
                color: white;
                padding-left: 5px;
                padding-top: 5px;
            }
        """)
        self.button1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.goToProfilePage)
        buttonsLayout.addWidget(self.button1, 0, 0, QtCore.Qt.AlignCenter)

        # Button 2 - Notifications
        self.button2 = QtWidgets.QPushButton(Form)
        self.button2.setMinimumSize(QtCore.QSize(180, 180))
        self.button2.setMaximumSize(QtCore.QSize(200, 200))
        self.button2.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-size: 20px;
                font-weight: bold;
                border-radius: 20px;
                border: 3px solid #2196F3;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: white;
                color: #2196F3;
                border: 3px solid #2196F3;
            }
            QPushButton:pressed {
                background-color: #1976D2;
                color: white;
                padding-left: 5px;
                padding-top: 5px;
            }
        """)
        self.button2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button2.setObjectName("button2")
        self.button2.clicked.connect(self.goToNotificationsPage)
        buttonsLayout.addWidget(self.button2, 0, 1, QtCore.Qt.AlignCenter)

        # Button 3 - Language
        self.button3 = QtWidgets.QPushButton(Form)
        self.button3.setMinimumSize(QtCore.QSize(180, 180))
        self.button3.setMaximumSize(QtCore.QSize(200, 200))
        self.button3.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                font-size: 20px;
                font-weight: bold;
                border-radius: 20px;
                border: 3px solid #FF9800;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: white;
                color: #FF9800;
                border: 3px solid #FF9800;
            }
            QPushButton:pressed {
                background-color: #F57C00;
                color: white;
                padding-left: 5px;
                padding-top: 5px;
            }
        """)
        self.button3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button3.setObjectName("button3")
        self.button3.clicked.connect(self.goToLanguagePage)
        buttonsLayout.addWidget(self.button3, 1, 0, QtCore.Qt.AlignCenter)

        # Button 4 - About
        self.button4 = QtWidgets.QPushButton(Form)
        self.button4.setMinimumSize(QtCore.QSize(180, 180))
        self.button4.setMaximumSize(QtCore.QSize(200, 200))
        self.button4.setStyleSheet("""
            QPushButton {
                background-color: #9C27B0;
                color: white;
                font-size: 20px;
                font-weight: bold;
                border-radius: 20px;
                border: 3px solid #9C27B0;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: white;
                color: #9C27B0;
                border: 3px solid #9C27B0;
            }
            QPushButton:pressed {
                background-color: #7B1FA2;
                color: white;
                padding-left: 5px;
                padding-top: 5px;
            }
        """)
        self.button4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button4.setObjectName("button4")
        self.button4.clicked.connect(self.goToAboutPage)
        buttonsLayout.addWidget(self.button4, 1, 1, QtCore.Qt.AlignCenter)

        self.mainLayout.addLayout(buttonsLayout)
        self.mainLayout.addStretch(2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def goBackToHome(self):
        """العودة لصفحة Home"""
        from home_page import Ui_HomeForm

        self.homeWindow = QtWidgets.QWidget()
        self.homeUI = Ui_HomeForm()
        self.homeUI.setupUi(self.homeWindow)
        self.homeWindow.show()
        self.Form.close()

    def goToProfilePage(self):
        """الانتقال لصفحة Profile"""
        from profile_page import Ui_ProfileForm

        self.profileWindow = QtWidgets.QWidget()
        self.profileUI = Ui_ProfileForm()
        self.profileUI.setupUi(self.profileWindow)
        self.profileWindow.show()
        self.Form.close()

    def goToNotificationsPage(self):
        """الانتقال لصفحة Notifications"""
        from Notfications import Ui_NotificationsForm

        self.notificationsWindow = QtWidgets.QWidget()
        self.notificationsUI = Ui_NotificationsForm()
        self.notificationsUI.setupUi(self.notificationsWindow)
        self.notificationsWindow.show()
        self.Form.close()

    def goToLanguagePage(self):
        """الانتقال لصفحة Language"""
        from language_page import Ui_LanguageForm

        self.languageWindow = QtWidgets.QWidget()
        self.languageUI = Ui_LanguageForm()
        self.languageUI.setupUi(self.languageWindow)
        self.languageWindow.show()
        self.Form.close()

    def goToAboutPage(self):
        """الانتقال لصفحة About"""
        from about_page import Ui_AboutForm

        self.aboutWindow = QtWidgets.QWidget()
        self.aboutUI = Ui_AboutForm()
        self.aboutUI.setupUi(self.aboutWindow)
        self.aboutWindow.show()
        self.Form.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Settings"))
        self.label_title.setText(_translate("Form", "Settings"))
        self.label_subtitle.setText(_translate("Form", "Customize Your Experience"))
        self.button1.setText(_translate("Form", "👤\n\nProfile"))
        self.button2.setText(_translate("Form", "🔔\n\nNotifications"))
        self.button3.setText(_translate("Form", "🌐\n\nLanguage"))
        self.button4.setText(_translate("Form", "ℹ️\n\nAbout"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_SettingsForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())