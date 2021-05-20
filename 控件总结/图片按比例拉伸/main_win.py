# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QAbstractItemView

from pyqt5_case_code.图片按比例拉伸.main_ui import Ui_MainWindow


class MyMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMain, self).__init__()
        self.setupUi(self)
        self.table_view.clicked.connect(self.handle)
        self.table_view.setEditTriggers(QAbstractItemView.DoubleClicked)

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

    def mouseReleaseEvent(self, ev):
        """鼠标松开事件"""
        print('松开++++鼠标')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyMain()
    main.show()
    sys.exit(app.exec_())

