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
        self.setCursor(self.cursor)
        self.setMouseTracking(True)
        self.start_x = 0
        self.start_y = 0
        self.move_flag = False

    def mouseDoubleClickEvent(self, QMouseEvent):
        pass

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.move_flag = True
            self.start_x = event.x()
            self.start_y = event.y()

    def mouseMoveEvent(self, event):  # 重写移动事件
        if self.move_flag:
            label_x = event.globalPos().x()
            label_y = event.globalPos().y()
            start = label_x - self.start_x
            end = label_y - self.start_y
            self.move(start, end)
        else:
            label_x = event.localPos().x()
            label_y = event.localPos().y()
            self.label.move(label_x, label_y)

    def mouseReleaseEvent(self, QMouseEvent):
        self.move_flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageWithMouseControl()
    ex.show()
    app.exec_()
