# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainterPath, QPainter, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QAbstractItemView

from 控件总结.图片按比例拉伸_窗口圆角.main_ui import Ui_MainWindow


class MyMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMain, self).__init__()
        self.setupUi(self)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.table_view.clicked.connect(self.handle)
        self.table_view.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.border_width = 8
        self.start_x = 0
        self.start_y = 0

    def handle(self):
        index = self.table_view.currentIndex()
        print(index.row(), index.column(), index.data(), index.flags())

    def closeEvent(self, event):
        quitMsgBox = QMessageBox()
        quitMsgBox.setWindowTitle('确认提示')
        quitMsgBox.setText('你确认退出吗？')
        quitMsgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = quitMsgBox.button(QMessageBox.Yes)
        buttonY.setText('确定')
        buttonN = quitMsgBox.button(QMessageBox.No)
        buttonN.setText('取消')
        quitMsgBox.exec_()
        if quitMsgBox.clickedButton() == buttonY:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        print(event.key())
        print(Qt.Key_Up)
        print('按下键盘')

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.isAutoRepeat():
            pass
        else:
            print('释放键盘')


    def paintEvent(self, event):
        """ 圆角窗口 """
        # 阴影
        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        pat = QPainter(self)
        pat.setRenderHint(pat.Antialiasing)
        pat.fillPath(path, QBrush(Qt.white))
        color = QColor(192, 192, 192, 50)
        for i in range(10):
            i_path = QPainterPath()
            i_path.setFillRule(Qt.WindingFill)
            ref = QRectF(10 - i, 10 - i, self.width() - (10 - i) * 2, self.height() - (10 - i) * 2)
            # i_path.addRect(ref)
            i_path.addRoundedRect(ref, self.border_width, self.border_width)
            color.setAlpha(150 - i ** 0.5 * 50)
            pat.setPen(color)
            pat.drawPath(i_path)
        # 圆角
        pat2 = QPainter(self)
        pat2.setRenderHint(pat2.Antialiasing)  # 抗锯齿
        pat2.setBrush(Qt.white)
        pat2.setPen(Qt.transparent)
        rect = self.rect()
        rect.setLeft(9)
        rect.setTop(9)
        rect.setWidth(rect.width() - 9) # 控制水平偏移量
        rect.setHeight(rect.height() - 9) # 控制竖直偏移量
        pat2.drawRoundedRect(rect, 10, 10) # 控制圆角锐度

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
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.move_flag = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyMain()
    main.show()
    sys.exit(app.exec_())

