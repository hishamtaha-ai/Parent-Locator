from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NotificationsForm(object):
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
        self.backButton.setText("←")
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

        # Notifications Settings Container
        settingsContainer = QtWidgets.QWidget(Form)
        settingsContainer.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
                border-radius: 15px;
            }
        """)
        settingsLayout = QtWidgets.QVBoxLayout(settingsContainer)
        settingsLayout.setSpacing(20)
        settingsLayout.setContentsMargins(20, 20, 20, 20)

        # Bus Arrival Notifications
        busArrivalLayout = QtWidgets.QHBoxLayout()
        self.busArrivalLabel = QtWidgets.QLabel(settingsContainer)
        self.busArrivalLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; color: rgb(26, 26, 26);")
        self.busArrivalLabel.setText("🚌 Bus Arrival")
        busArrivalLayout.addWidget(self.busArrivalLabel)
        busArrivalLayout.addStretch()

        self.busArrivalSwitch = QtWidgets.QCheckBox(settingsContainer)
        self.busArrivalSwitch.setStyleSheet("""
            QCheckBox::indicator {
                width: 50px;
                height: 25px;
            }
            QCheckBox::indicator:unchecked {
                background-color: #ccc;
                border-radius: 12px;
            }
            QCheckBox::indicator:checked {
                background-color: #2196F3;
                border-radius: 12px;
            }
        """)
        self.busArrivalSwitch.setChecked(True)
        busArrivalLayout.addWidget(self.busArrivalSwitch)
        settingsLayout.addLayout(busArrivalLayout)

        # Route Updates Notifications
        routeUpdatesLayout = QtWidgets.QHBoxLayout()
        self.routeUpdatesLabel = QtWidgets.QLabel(settingsContainer)
        self.routeUpdatesLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; color: rgb(26, 26, 26);")
        self.routeUpdatesLabel.setText("🗺️ Route Updates")
        routeUpdatesLayout.addWidget(self.routeUpdatesLabel)
        routeUpdatesLayout.addStretch()

        self.routeUpdatesSwitch = QtWidgets.QCheckBox(settingsContainer)
        self.routeUpdatesSwitch.setStyleSheet("""
            QCheckBox::indicator {
                width: 50px;
                height: 25px;
            }
            QCheckBox::indicator:unchecked {
                background-color: #ccc;
                border-radius: 12px;
            }
            QCheckBox::indicator:checked {
                background-color: #2196F3;
                border-radius: 12px;
            }
        """)
        self.routeUpdatesSwitch.setChecked(True)
        routeUpdatesLayout.addWidget(self.routeUpdatesSwitch)
        settingsLayout.addLayout(routeUpdatesLayout)

        # Schedule Changes Notifications
        scheduleChangesLayout = QtWidgets.QHBoxLayout()
        self.scheduleChangesLabel = QtWidgets.QLabel(settingsContainer)
        self.scheduleChangesLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; color: rgb(26, 26, 26);")
        self.scheduleChangesLabel.setText("📅 Schedule Changes")
        scheduleChangesLayout.addWidget(self.scheduleChangesLabel)
        scheduleChangesLayout.addStretch()

        self.scheduleChangesSwitch = QtWidgets.QCheckBox(settingsContainer)
        self.scheduleChangesSwitch.setStyleSheet("""
            QCheckBox::indicator {
                width: 50px;
                height: 25px;
            }
            QCheckBox::indicator:unchecked {
                background-color: #ccc;
                border-radius: 12px;
            }
            QCheckBox::indicator:checked {
                background-color: #2196F3;
                border-radius: 12px;
            }
        """)
        self.scheduleChangesSwitch.setChecked(False)
        scheduleChangesLayout.addWidget(self.scheduleChangesSwitch)
        settingsLayout.addLayout(scheduleChangesLayout)

        # Delays Notifications
        delaysLayout = QtWidgets.QHBoxLayout()
        self.delaysLabel = QtWidgets.QLabel(settingsContainer)
        self.delaysLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; color: rgb(26, 26, 26);")
        self.delaysLabel.setText("⚠️ Delays & Alerts")
        delaysLayout.addWidget(self.delaysLabel)
        delaysLayout.addStretch()

        self.delaysSwitch = QtWidgets.QCheckBox(settingsContainer)
        self.delaysSwitch.setStyleSheet("""
            QCheckBox::indicator {
                width: 50px;
                height: 25px;
            }
            QCheckBox::indicator:unchecked {
                background-color: #ccc;
                border-radius: 12px;
            }
            QCheckBox::indicator:checked {
                background-color: #2196F3;
                border-radius: 12px;
            }
        """)
        self.delaysSwitch.setChecked(True)
        delaysLayout.addWidget(self.delaysSwitch)
        settingsLayout.addLayout(delaysLayout)

        # Push Notifications
        pushLayout = QtWidgets.QHBoxLayout()
        self.pushLabel = QtWidgets.QLabel(settingsContainer)
        self.pushLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; color: rgb(26, 26, 26);")
        self.pushLabel.setText("🔔 Push Notifications")
        pushLayout.addWidget(self.pushLabel)
        pushLayout.addStretch()

        self.pushSwitch = QtWidgets.QCheckBox(settingsContainer)
        self.pushSwitch.setStyleSheet("""
            QCheckBox::indicator {
                width: 50px;
                height: 25px;
            }
            QCheckBox::indicator:unchecked {
                background-color: #ccc;
                border-radius: 12px;
            }
            QCheckBox::indicator:checked {
                background-color: #2196F3;
                border-radius: 12px;
            }
        """)
        self.pushSwitch.setChecked(True)
        pushLayout.addWidget(self.pushSwitch)
        settingsLayout.addLayout(pushLayout)

        # Email Notifications
        emailLayout = QtWidgets.QHBoxLayout()
        self.emailLabel = QtWidgets.QLabel(settingsContainer)
        self.emailLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; color: rgb(26, 26, 26);")
        self.emailLabel.setText("📧 Email Notifications")
        emailLayout.addWidget(self.emailLabel)
        emailLayout.addStretch()

        self.emailSwitch = QtWidgets.QCheckBox(settingsContainer)
        self.emailSwitch.setStyleSheet("""
            QCheckBox::indicator {
                width: 50px;
                height: 25px;
            }
            QCheckBox::indicator:unchecked {
                background-color: #ccc;
                border-radius: 12px;
            }
            QCheckBox::indicator:checked {
                background-color: #2196F3;
                border-radius: 12px;
            }
        """)
        self.emailSwitch.setChecked(False)
        emailLayout.addWidget(self.emailSwitch)
        settingsLayout.addLayout(emailLayout)

        self.mainLayout.addWidget(settingsContainer)

        self.mainLayout.addSpacing(20)

        # Save Button
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setText("Save Preferences")
        self.saveButton.setMinimumSize(QtCore.QSize(0, 50))
        self.saveButton.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 10px;
                border: none;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:pressed {
                background-color: #1565C0;
            }
        """)
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainLayout.addWidget(self.saveButton)

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
        Form.setWindowTitle(_translate("Form", "Notifications"))
        self.label_title.setText(_translate("Form", "Notifications"))
        self.label_subtitle.setText(_translate("Form", "Manage Your Alerts"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_NotificationsForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())