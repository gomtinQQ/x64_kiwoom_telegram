

# 64bit veersion
# ext librarys
# pip3 install PyQt5
# Save as UNICODE UTF-8 signed

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QAxContainer import *
from PyQt5 import uic

form_class = uic.loadUiType("main_window.ui")[0]

class Kiwoom():
    def __init__(self):
        super().__init__()
        if sys.maxsize > 2**32:
            prog_id = "KHOPENAPI64.KHOpenAPICtrl.1"
        else:
            prog_id = "KHOPENAPI.KHOpenAPICtrl.1"

        self.ocx = QAxWidget(prog_id)

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.axWindow = Kiwoom()
        self.btn_login.clicked.connect(self.btn_login_Clicked)


    def btn_login_Clicked(self):
        self.axWindow.CommConnect()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

