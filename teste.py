from PyQt5 import QtWidgets, uic
from add_client import NewClientWindow
import sys
from time import sleep

class  UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('template/main_window.ui', self)
        self.init_interface()

    
    def init_interface(self):
        self.showMaximized()
        self.open_dialog()

    def open_dialog(self):
        dialog = NewClientWindow().__init__()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    app.exec_()


# self.actionFechar_Janela.triggered.connect(open_dialog)