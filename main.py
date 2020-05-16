from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from add_client import NewClientWindow
from system_login import SystemLoginScreen
import sys

class  UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('template/main_window.ui', self)
        self.init_interface()

    
    def init_interface(self):
        self.setWindowTitle('CellFire App')
        #self.statusBar().showMessage('CellFire App - Home')

        #self.button_teste = self.findChild(QPushButton, 'pushButton')
        #self.button_teste.clicked.connect(self.button_pressed)
        self.showMaximized()
        self.system_user_login()


    def open_dialog(self):
        dialog = NewClientWindow()
        dialog.__init__()

    
    def button_pressed(self):
        msg = QMessageBox.warning(self, 'Message Box', 'Deseja realmente abrir esta janela?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        
        if msg == QMessageBox.Yes:
            self.open_dialog()

    
    def system_user_login(self):
        login_screen = SystemLoginScreen()
        login_screen.__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UI()
    app.exec_()

