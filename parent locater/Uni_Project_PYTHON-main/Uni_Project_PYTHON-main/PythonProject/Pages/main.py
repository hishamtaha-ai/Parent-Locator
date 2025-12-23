import sys
from PyQt5 import QtWidgets
from login_page import Ui_LoginForm

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # بدء التطبيق من صفحة Login
    loginWindow = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(loginWindow)
    loginWindow.show()

    sys.exit(app.exec_())