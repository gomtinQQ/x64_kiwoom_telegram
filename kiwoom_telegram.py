# -*- coding: utf-8 -*-
# 64bit veersion
# ext librarys
# pip3 install PyQt5
# Save as UNICODE UTF-8 signed

import sys
import configparser

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QAxContainer import *
from PyQt5 import uic

from kiwoom.KHOpenApi import *

form_class = uic.loadUiType("main_window.ui")[0]



class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.axWindow = KHOpenApi()

        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

        if self.config.has_section('telegram'):
            self.lineEdit_telegram_token.setText(self.config['telegram']['token'])
            self.lineEdit_telegram_chat_ID.setText(self.config['telegram']['chatID'])
            pass

        self.btn_login.clicked.connect(self.btn_login_Clicked)
        self.btn_logout.clicked.connect(self.btn_logout_Clicked)
        self.btn_start.clicked.connect(self.btn_start_Clicked)
        self.btn_stop.clicked.connect(self.btn_stop_Clicked)

    def btn_login_Clicked(self):
        self.axWindow.CommConnect()

    def btn_logout_Clicked(self):
        self.axWindow.CommTerminate()

    def btn_start_Clicked(self):
        #self.axWindow.CommTerminate()
        write_config = configparser.ConfigParser()
        write_config['telegram'] = {}
        write_config['telegram']['token'] = self.lineEdit_telegram_token.text()
        write_config['telegram']['chatID'] = self.lineEdit_telegram_chat_ID.text()
        with open('config.ini', 'w') as configfile:
            write_config.write(configfile)

    def btn_stop_Clicked(self):
        self.axWindow.CommTerminate()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

