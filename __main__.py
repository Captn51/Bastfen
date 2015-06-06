# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from bastfen import Bastfen

app = QtWidgets.QApplication(sys.argv)
b = Bastfen()
b.show()
sys.exit(app.exec_())

