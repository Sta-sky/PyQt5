# encoding:utf8
import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class WinDow(QWidget):

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
        # self.setMouseTracking(True)
        self.setCursor(self.cursor)
        # 设置无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.8)

        self.close_btn = QPushButton(self)
        self.close_btn.resize(self.close_btn.width(), self.close_btn.height())
        self.close_btn.setText('关闭')
        self.close_btn.setStyleSheet('border: 0px; background-color: red')

        self.max_btn = QPushButton(self)
        self.max_btn.resize(self.max_btn.width(), self.max_btn.height())
        self.max_btn.setText('最大化')
        self.max_btn.setStyleSheet('border: 0px; background-color: red')

        self.mix_btn = QPushButton(self)
        self.mix_btn.resize(self.mix_btn.width(), self.mix_btn.height())
        self.mix_btn.setText('最小化')
        self.mix_btn.setStyleSheet('border: 0px; background-color: red')

        self.max_btn.clicked.connect(self.handle_max)
        self.mix_btn.clicked.connect(self.handle_mix)
        self.close_btn.clicked.connect(self.handle_close)
        self.move_flag = False

    def handle_max(self):
        if self.isMaximized():
            self.showNormal()
            self.max_btn.setText('最大化')
        else:
            self.showMaximized()
            self.max_btn.setText('恢复')

    def handle_mix(self):
        self.showMinimized()

    def handle_close(self):
        self.close()

    def resizeEvent(self, event):
        try:
            self_x = self.width()
            self.btn_close_w = self.close_btn.width()
            self.btn_max_w = self.max_btn.width()
            self.btn_min_w = self.mix_btn.width()
            self.close_btn.move(self_x - self.btn_close_w, 5)
            self.max_btn.move(self_x - self.btn_close_w - self.btn_max_w, 5)
            self.mix_btn.move(self_x - self.btn_close_w - self.btn_min_w - self.btn_max_w, 5)
        except Exception as e:
            print(e)

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
    ex = WinDow()
    ex.show()
    app.exec_()
