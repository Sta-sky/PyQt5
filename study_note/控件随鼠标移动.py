# encoding:utf8
import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ImageWithMouseControl(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(700, 500)
        self.parent = parent
        self.img = QPixmap(os.path.realpath('test3.jpg'))
        self.label = QLabel(self)
        self.label.setFixedSize(300, 300)
        self.scaled_img = self.img.scaled(self.size())
        self.scaled_1 = self.img.scaled(QSize(10, 10))
        self.label.setPixmap(self.scaled_img)
        self.cursor = QCursor(self.scaled_1)
        self.setMouseTracking(True)
        self.setCursor(self.cursor)

    def mouseMoveEvent(self, event):  # 重写移动事件
        label_x = event.localPos().x()
        label_y = event.localPos().y()
        self.label.move(label_x, label_y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageWithMouseControl()
    ex.show()
    app.exec_()
