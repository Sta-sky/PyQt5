# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author:       Sz
   WeChat:       百川一页
-------------------------------------------------
"""
__author__ = 'Sz'

from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("社会我顺哥,人狠话不多")
window.resize(500, 500)
window.move(400, 200)

label = QLabel(window)
label.setText("Hello Sz")
label.move(200, 200)

window.show()

sys.exit(app.exec_())
