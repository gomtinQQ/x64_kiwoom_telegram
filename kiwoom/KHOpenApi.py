# -*- coding: utf-8 -*-

import sys
from PyQt5.QAxContainer import QAxWidget


class KHOpenApi(object):
    """description of class"""
    def __init__(self):
        super().__init__()
        if sys.maxsize > 2**32:
            prog_id = "KHOPENAPI64.KHOpenAPICtrl.1"
        else:
            prog_id = "KHOPENAPI.KHOpenAPICtrl.1"

        self.ocx = QAxWidget(prog_id)

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")
    def CommTerminate(self):
        self.ocx.dynamicCall("CommTerminate()")

