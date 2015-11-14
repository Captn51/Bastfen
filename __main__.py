# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from bastfen import Bastfen


app = QApplication(sys.argv)
b = Bastfen()
b.show()
sys.exit(app.exec_())

