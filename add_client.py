from PyQt5 import QtWidgets, uic

class  NewClientWindow(QtWidgets.QDialog):
    def __init__(self):
        super(NewClientWindow, self).__init__()
        uic.loadUi('template/dialog_cadastro_cliente.ui', self)
        self.show()

