from PyQt5 import QtWidgets, uic

class  SystemLoginScreen(QtWidgets.QDialog):
    def __init__(self):
        super(SystemLoginScreen, self).__init__()
        uic.loadUi('template/login_screen.ui', self)
        self.show()