from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutForm(object):
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
                border-radius: 24px;
                border: 24px solid #ddd;
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
        self.logoCorner.setPixmap(QtGui.QPixmap(
            "C:/Users/fares/Desktop/gui/app-main/Elsewedy-University-of-Technology-Egypt-96010-1698259526-removebg-preview.png"))
        self.logoCorner.setScaledContents(True)
        self.logoCorner.setMaximumSize(QtCore.QSize(120, 120))
        self.logoCorner.setMinimumSize(QtCore.QSize(100, 100))
        self.logoCorner.setObjectName("logoCorner")
        topLayout.addWidget(self.logoCorner)

        self.mainLayout.addLayout(topLayout)

        self.mainLayout.addSpacing(10)

        # App Icon
        appIconLayout = QtWidgets.QHBoxLayout()
        appIconLayout.addStretch()

        self.appIcon = QtWidgets.QLabel(Form)
        self.appIcon.setMinimumSize(QtCore.QSize(100, 100))
        self.appIcon.setMaximumSize(QtCore.QSize(100, 100))
        self.appIcon.setStyleSheet("""
            QLabel {
                background-color: #9C27B0;
                border-radius: 50px;
                font-size: 48px;
                color: white;
            }
        """)
        self.appIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.appIcon.setText("🚌")
        appIconLayout.addWidget(self.appIcon)

        appIconLayout.addStretch()
        self.mainLayout.addLayout(appIconLayout)

        self.mainLayout.addSpacing(10)

        # App Name
        self.appName = QtWidgets.QLabel(Form)
        self.appName.setStyleSheet("color: rgb(26, 26, 26); font: 75 24pt \"MS Shell Dlg 2\";")
        self.appName.setAlignment(QtCore.Qt.AlignCenter)
        self.appName.setText("Bus System")
        self.mainLayout.addWidget(self.appName)

        # Version
        self.versionLabel = QtWidgets.QLabel(Form)
        self.versionLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; color: rgb(100, 100, 100);")
        self.versionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.versionLabel.setText("Version 1.0.0")
        self.mainLayout.addWidget(self.versionLabel)

        self.mainLayout.addSpacing(20)

        # About Container
        aboutContainer = QtWidgets.QWidget(Form)
        aboutContainer.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
                border-radius: 15px;
            }
        """)
        aboutLayout = QtWidgets.QVBoxLayout(aboutContainer)
        aboutLayout.setSpacing(15)
        aboutLayout.setContentsMargins(20, 20, 20, 20)

        # Description
        self.descriptionLabel = QtWidgets.QLabel(aboutContainer)
        self.descriptionLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color: rgb(26, 26, 26);")
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setText(
            "Bus System is a comprehensive transportation management application "
            "designed to help students and staff navigate campus efficiently."
        )
        aboutLayout.addWidget(self.descriptionLabel)

        # Separator
        separator1 = QtWidgets.QFrame(aboutContainer)
        separator1.setFrameShape(QtWidgets.QFrame.HLine)
        separator1.setStyleSheet("background-color: #e0e0e0;")
        separator1.setMaximumHeight(1)
        aboutLayout.addWidget(separator1)

        # Developer Info
        self.developerLabel = QtWidgets.QLabel(aboutContainer)
        self.developerLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color: rgb(26, 26, 26);")
        self.developerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.developerLabel.setText("👨‍💻 Developed by: Fares - Hisham - Youssef - Reem - kamel")
        aboutLayout.addWidget(self.developerLabel)

        # Separator
        separator2 = QtWidgets.QFrame(aboutContainer)
        separator2.setFrameShape(QtWidgets.QFrame.HLine)
        separator2.setStyleSheet("background-color: #e0e0e0;")
        separator2.setMaximumHeight(1)
        aboutLayout.addWidget(separator2)

        # Copyright
        self.copyrightLabel = QtWidgets.QLabel(aboutContainer)
        self.copyrightLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color: rgb(26, 26, 26);")
        self.copyrightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.copyrightLabel.setText("© 2025 Elsewedy University")
        aboutLayout.addWidget(self.copyrightLabel)

        # Separator
        separator3 = QtWidgets.QFrame(aboutContainer)
        separator3.setFrameShape(QtWidgets.QFrame.HLine)
        separator3.setStyleSheet("background-color: #e0e0e0;")
        separator3.setMaximumHeight(1)
        aboutLayout.addWidget(separator3)

        # Contact
        self.contactLabel = QtWidgets.QLabel(aboutContainer)
        self.contactLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color: rgb(26, 26, 26);")
        self.contactLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.contactLabel.setText("📧 Contact: transportation@sut.edu.morocco")
        aboutLayout.addWidget(self.contactLabel)

        self.mainLayout.addWidget(aboutContainer)

        self.mainLayout.addSpacing(20)

        # Action Buttons Container
        buttonsContainer = QtWidgets.QWidget(Form)
        buttonsLayout = QtWidgets.QVBoxLayout(buttonsContainer)
        buttonsLayout.setSpacing(10)

        # Check Updates Button
        self.updateButton = QtWidgets.QPushButton(buttonsContainer)
        self.updateButton.setText("🔄 Check for Updates")
        self.updateButton.setMinimumSize(QtCore.QSize(0, 45))
        self.updateButton.setStyleSheet("""
            QPushButton {
                background-color: #9C27B0;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 10px;
                border: none;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #7B1FA2;
            }
            QPushButton:pressed {
                background-color: #6A1B9A;
            }
        """)
        self.updateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        buttonsLayout.addWidget(self.updateButton)

        # Terms & Conditions Button
        self.termsButton = QtWidgets.QPushButton(buttonsContainer)
        self.termsButton.setText("📄 Terms & Conditions")
        self.termsButton.setMinimumSize(QtCore.QSize(0, 45))
        self.termsButton.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #9C27B0;
                font-size: 14px;
                font-weight: bold;
                border-radius: 10px;
                border: 2px solid #9C27B0;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #f3e5f5;
            }
            QPushButton:pressed {
                background-color: #e1bee7;
            }
        """)
        self.termsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        buttonsLayout.addWidget(self.termsButton)

        # Privacy Policy Button
        self.privacyButton = QtWidgets.QPushButton(buttonsContainer)
        self.privacyButton.setText("🔒 Privacy Policy")
        self.privacyButton.setMinimumSize(QtCore.QSize(0, 45))
        self.privacyButton.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #9C27B0;
                font-size: 14px;
                font-weight: bold;
                border-radius: 10px;
                border: 2px solid #9C27B0;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #f3e5f5;
            }
            QPushButton:pressed {
                background-color: #e1bee7;
            }
        """)
        self.privacyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        buttonsLayout.addWidget(self.privacyButton)

        self.mainLayout.addWidget(buttonsContainer)

        self.mainLayout.addStretch()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def goBackToSettings(self):
        """العودة لصفحة Settings"""
        from settings import Ui_SettingsForm

        self.settingsWindow = QtWidgets.QWidget()
        self.settingsUI = Ui_SettingsForm()
        self.settingsUI.setupUi(self.settingsWindow)
        self.settingsWindow.show()
        self.Form.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "About"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_AboutForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())