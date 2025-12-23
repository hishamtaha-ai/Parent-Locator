from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeForm(object):
    def setupUi(self, Form):
        self.Form = Form  # حفظ reference للـ Form
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(466, 741)
        Form.setStyleSheet("QWidget { background-color: #FFFFFF; }")

        # Main layout
        self.mainLayout = QtWidgets.QVBoxLayout(Form)
        self.mainLayout.setContentsMargins(30, 20, 30, 20)
        self.mainLayout.setSpacing(15)

        # Top corner logo
        topLayout = QtWidgets.QHBoxLayout()
        self.logoCorner = QtWidgets.QLabel(Form)
        self.logoCorner.setText("")
        self.logoCorner.setPixmap(QtGui.QPixmap(
            "C:/Users/fares/Desktop/gui/app-main/Elsewedy-University-of-Technology-Egypt-96010-1698259526-removebg-preview.png"))
        self.logoCorner.setScaledContents(True)
        self.logoCorner.setMaximumSize(QtCore.QSize(120, 120))
        self.logoCorner.setMinimumSize(QtCore.QSize(100, 100))
        self.logoCorner.setObjectName("logoCorner")
        topLayout.addWidget(self.logoCorner)
        topLayout.addStretch()
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

        # Buttons Grid Layout
        buttonsLayout = QtWidgets.QGridLayout()
        buttonsLayout.setSpacing(20)

        # Button 1 - Map
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
        self.button1.clicked.connect(self.goToMapPage)  # ربط زر Map
        buttonsLayout.addWidget(self.button1, 0, 0, QtCore.Qt.AlignCenter)

        # Button 2 - Schedule
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
        self.button2.clicked.connect(self.goToSchedulePage)  # ربط زر Schedule
        buttonsLayout.addWidget(self.button2, 0, 1, QtCore.Qt.AlignCenter)

        # Button 3 - Routes
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
        self.button3.clicked.connect(self.goToRoutesPage)  # ربط زر Routes
        buttonsLayout.addWidget(self.button3, 1, 0, QtCore.Qt.AlignCenter)

        # Button 4 - Settings
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
        self.button4.clicked.connect(self.goToSettingsPage)  # ربط زر Settings
        buttonsLayout.addWidget(self.button4, 1, 1, QtCore.Qt.AlignCenter)

        self.mainLayout.addLayout(buttonsLayout)
        self.mainLayout.addStretch(2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def goToMapPage(self):
        """الانتقال لصفحة Map"""
        from map import Ui_MapForm

        self.mapWindow = QtWidgets.QWidget()
        self.mapUI = Ui_MapForm()
        self.mapUI.setupUi(self.mapWindow)
        self.mapWindow.show()
        self.Form.close()

    def goToSchedulePage(self):
        """الانتقال لصفحة Schedule"""
        from attendance_page import Ui_AttendanceForm

        self.scheduleWindow = QtWidgets.QWidget()
        self.scheduleUI = Ui_AttendanceForm()
        self.scheduleUI.setupUi(self.scheduleWindow)
        self.scheduleWindow.show()
        self.Form.close()

    def goToRoutesPage(self):
        """الانتقال لصفحة Routes"""
        from routes_page import Ui_RoutesForm

        self.routesWindow = QtWidgets.QWidget()
        self.routesUI = Ui_RoutesForm()
        self.routesUI.setupUi(self.routesWindow)
        self.routesWindow.show()
        self.Form.close()

    def goToSettingsPage(self):
        """الانتقال لصفحة Settings"""
        from settings import Ui_SettingsForm

        self.settingsWindow = QtWidgets.QWidget()
        self.settingsUI = Ui_SettingsForm()
        self.settingsUI.setupUi(self.settingsWindow)
        self.settingsWindow.show()
        self.Form.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Home"))
        self.label_title.setText(_translate("Form", "Home"))
        self.label_subtitle.setText(_translate("Form", "Welcome to Bus System"))
        self.button1.setText(_translate("Form", "🗺️\n\nMap"))
        self.button2.setText(_translate("Form", "📝\n\nAttendance"))
        self.button3.setText(_translate("Form", "🚌\n\nRoutes"))
        self.button4.setText(_translate("Form", "⚙️\n\nSettings"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_HomeForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())