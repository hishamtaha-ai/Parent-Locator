from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RoutesForm(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(466, 741)
        Form.setStyleSheet("QWidget { background-color: #FFFFFF; }")

        # Main layout
        self.mainLayout = QtWidgets.QVBoxLayout(Form)
        self.mainLayout.setContentsMargins(25, 15, 25, 15)
        self.mainLayout.setSpacing(10)

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
        self.backButton.clicked.connect(self.goBackToHome)
        headerLayout.addWidget(self.backButton)
        headerLayout.addStretch()
        self.mainLayout.addLayout(headerLayout)

        # Title
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setStyleSheet("color: rgb(26, 26, 26); font: 75 28pt \"MS Shell Dlg 2\";")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setText("Bus Routes")
        self.mainLayout.addWidget(self.label_title)

        # Subtitle
        self.label_subtitle = QtWidgets.QLabel(Form)
        self.label_subtitle.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color: rgb(100, 100, 100);")
        self.label_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle.setText("اختر الخط المطلوب")
        self.mainLayout.addWidget(self.label_subtitle)

        self.mainLayout.addSpacing(5)

        # ========== قسم الخط الحالي ==========
        self.currentRouteFrame = QtWidgets.QFrame(Form)
        self.currentRouteFrame.setStyleSheet("""
            QFrame {
                background-color: #FFF3E0;
                border: 2px solid #FF9800;
                border-radius: 15px;
                padding: 15px;
            }
        """)
        self.currentRouteFrame.setMinimumHeight(100)

        currentRouteLayout = QtWidgets.QVBoxLayout(self.currentRouteFrame)
        currentRouteLayout.setSpacing(8)

        # عنوان القسم
        currentRouteTitle = QtWidgets.QLabel("خطي الحالي")
        currentRouteTitle.setStyleSheet("font: bold 16pt \"MS Shell Dlg 2\"; color: #FF9800;")
        currentRouteTitle.setAlignment(QtCore.Qt.AlignCenter)
        currentRouteLayout.addWidget(currentRouteTitle)

        # عرض الخط الحالي
        self.currentRouteLabel = QtWidgets.QLabel("خط 3 - مصر الجديدة")
        self.currentRouteLabel.setStyleSheet("font: bold 14pt \"MS Shell Dlg 2\"; color: #1A1A1A;")
        self.currentRouteLabel.setAlignment(QtCore.Qt.AlignCenter)
        currentRouteLayout.addWidget(self.currentRouteLabel)

        # زر تغيير الخط
        self.changeRouteButton = QtWidgets.QPushButton("تغيير الخط")
        self.changeRouteButton.setMinimumSize(QtCore.QSize(0, 40))
        self.changeRouteButton.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 10px;
                border: none;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
            QPushButton:pressed {
                background-color: #E65100;
            }
        """)
        self.changeRouteButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changeRouteButton.clicked.connect(self.goToChangeRoute)
        currentRouteLayout.addWidget(self.changeRouteButton)

        self.mainLayout.addWidget(self.currentRouteFrame)
        self.mainLayout.addSpacing(10)

        # عنوان قائمة الخطوط
        routesListTitle = QtWidgets.QLabel("جميع الخطوط المتاحة")
        routesListTitle.setStyleSheet("font: bold 14pt \"MS Shell Dlg 2\"; color: rgb(26, 26, 26);")
        routesListTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.addWidget(routesListTitle)

        # Scroll Area for routes
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
            QScrollBar::handle:vertical:hover {
                background: #F57C00;
            }
        """)

        # Container widget
        self.scrollWidget = QtWidgets.QWidget()
        self.scrollLayout = QtWidgets.QVBoxLayout(self.scrollWidget)
        self.scrollLayout.setSpacing(12)
        self.scrollLayout.setContentsMargins(0, 0, 0, 0)

        # قائمة الخطوط
        routes = [
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
        ]

        # Create buttons for each route
        self.routeButtons = []
        for route in routes:
            btn = QtWidgets.QPushButton(self.scrollWidget)
            btn.setText(route)
            btn.setMinimumSize(QtCore.QSize(0, 60))
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #FF9800;
                    color: white;
                    font-size: 18px;
                    font-weight: bold;
                    border-radius: 15px;
                    border: 3px solid #FF9800;
                    padding: 15px;
                    text-align: center;
                }
                QPushButton:hover {
                    background-color: white;
                    color: #FF9800;
                    border: 3px solid #FF9800;
                }
                QPushButton:pressed {
                    background-color: #F57C00;
                    color: white;
                }
            """)
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.clicked.connect(lambda checked, r=route: self.goToRouteDetails(r))
            self.scrollLayout.addWidget(btn)
            self.routeButtons.append(btn)

        self.scrollLayout.addStretch()
        self.scrollArea.setWidget(self.scrollWidget)
        self.mainLayout.addWidget(self.scrollArea)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def goBackToHome(self):
        """الرجوع لصفحة Home"""
        from home_page import Ui_HomeForm

        self.homeWindow = QtWidgets.QWidget()
        self.homeUI = Ui_HomeForm()
        self.homeUI.setupUi(self.homeWindow)
        self.homeWindow.show()
        self.Form.close()

    def goToChangeRoute(self):
        """الانتقال لصفحة تغيير الخط"""
        from change_route_request_page import Ui_ChangeRouteRequestForm

        self.changeRouteWindow = QtWidgets.QWidget()
        self.changeRouteUI = Ui_ChangeRouteRequestForm()
        self.changeRouteUI.setupUi(self.changeRouteWindow, self.currentRouteLabel.text())
        self.changeRouteWindow.show()
        self.Form.close()

    def goToRouteDetails(self, route_name):
        """فتح صفحة تفاصيل الخط"""
        from route_details_page import Ui_RouteDetailsForm

        self.detailsWindow = QtWidgets.QWidget()
        self.detailsUI = Ui_RouteDetailsForm()
        self.detailsUI.setupUi(self.detailsWindow, route_name)
        self.detailsWindow.show()
        self.Form.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_RoutesForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())