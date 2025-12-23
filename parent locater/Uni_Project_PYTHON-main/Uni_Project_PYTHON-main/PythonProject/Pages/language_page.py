from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LanguageForm(object):
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

        self.mainLayout.addSpacing(20)

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

        # Language Selection Container
        languageContainer = QtWidgets.QWidget(Form)
        languageContainer.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
                border-radius: 15px;
            }
        """)
        languageLayout = QtWidgets.QVBoxLayout(languageContainer)
        languageLayout.setSpacing(15)
        languageLayout.setContentsMargins(20, 20, 20, 20)

        # Radio Button Style
        radioStyle = """
            QRadioButton {
                font: 14pt "MS Shell Dlg 2";
                color: rgb(26, 26, 26);
                padding: 10px;
            }
            QRadioButton::indicator {
                width: 25px;
                height: 25px;
            }
            QRadioButton::indicator:unchecked {
                border: 2px solid #ccc;
                border-radius: 12px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                border: 2px solid #FF9800;
                border-radius: 12px;
                background-color: #FF9800;
            }
        """

        # English
        self.englishRadio = QtWidgets.QRadioButton(languageContainer)
        self.englishRadio.setText("🇬🇧 English")
        self.englishRadio.setStyleSheet(radioStyle)
        self.englishRadio.setChecked(True)
        languageLayout.addWidget(self.englishRadio)

        # Separator
        separator1 = QtWidgets.QFrame(languageContainer)
        separator1.setFrameShape(QtWidgets.QFrame.HLine)
        separator1.setStyleSheet("background-color: #e0e0e0;")
        separator1.setMaximumHeight(1)
        languageLayout.addWidget(separator1)

        # Arabic
        self.arabicRadio = QtWidgets.QRadioButton(languageContainer)
        self.arabicRadio.setText("🇪🇬 العربية (Arabic)")
        self.arabicRadio.setStyleSheet(radioStyle)
        languageLayout.addWidget(self.arabicRadio)

        # Separator
        separator2 = QtWidgets.QFrame(languageContainer)
        separator2.setFrameShape(QtWidgets.QFrame.HLine)
        separator2.setStyleSheet("background-color: #e0e0e0;")
        separator2.setMaximumHeight(1)
        languageLayout.addWidget(separator2)

        # French
        self.frenchRadio = QtWidgets.QRadioButton(languageContainer)
        self.frenchRadio.setText("🇫🇷 Français (French)")
        self.frenchRadio.setStyleSheet(radioStyle)
        languageLayout.addWidget(self.frenchRadio)

        # Separator
        separator3 = QtWidgets.QFrame(languageContainer)
        separator3.setFrameShape(QtWidgets.QFrame.HLine)
        separator3.setStyleSheet("background-color: #e0e0e0;")
        separator3.setMaximumHeight(1)
        languageLayout.addWidget(separator3)

        # Spanish
        self.spanishRadio = QtWidgets.QRadioButton(languageContainer)
        self.spanishRadio.setText("🇪🇸 Español (Spanish)")
        self.spanishRadio.setStyleSheet(radioStyle)
        languageLayout.addWidget(self.spanishRadio)

        # Separator
        separator4 = QtWidgets.QFrame(languageContainer)
        separator4.setFrameShape(QtWidgets.QFrame.HLine)
        separator4.setStyleSheet("background-color: #e0e0e0;")
        separator4.setMaximumHeight(1)
        languageLayout.addWidget(separator4)

        # German
        self.germanRadio = QtWidgets.QRadioButton(languageContainer)
        self.germanRadio.setText("🇩🇪 Deutsch (German)")
        self.germanRadio.setStyleSheet(radioStyle)
        languageLayout.addWidget(self.germanRadio)

        self.mainLayout.addWidget(languageContainer)

        self.mainLayout.addSpacing(20)

        # Info Label
        self.infoLabel = QtWidgets.QLabel(Form)
        self.infoLabel.setText("ℹ️ App will restart to apply language changes")
        self.infoLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color: rgb(100, 100, 100);")
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.addWidget(self.infoLabel)

        self.mainLayout.addSpacing(10)

        # Apply Button
        self.applyButton = QtWidgets.QPushButton(Form)
        self.applyButton.setText("Apply Language")
        self.applyButton.setMinimumSize(QtCore.QSize(0, 50))
        self.applyButton.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 10px;
                border: none;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
            QPushButton:pressed {
                background-color: #E65100;
            }
        """)
        self.applyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainLayout.addWidget(self.applyButton)

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
        Form.setWindowTitle(_translate("Form", "Language"))
        self.label_title.setText(_translate("Form", "Language"))
        self.label_subtitle.setText(_translate("Form", "Choose Your Preferred Language"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_LanguageForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())