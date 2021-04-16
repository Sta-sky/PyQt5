import random

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QTableWidget, QTableWidgetItem, QPushButton, \
    QVBoxLayout
import sys


class QlabelDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.action = QAction(self)
        self.setGeometry(QtCore.QRect(100, 200, 500, 600))
        self.action.setStatusTip("我来了")
        exitAction1 = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction1.setShortcut('Ctrl+Q')

        exitAction2 = QAction(QIcon('exit.png'), '&Edit', self)
        exitAction2.setShortcut('Ctrl+l')

        exitAction1.setStatusTip('Exit application')
        exitAction2.setStatusTip('Edit application')
        exitAction1.triggered.connect(qApp.quit)
        self.statusBar()
        self.menubar = self.menuBar()
        filemenu = self.menubar.addMenu('&file')
        filemenu.addAction(exitAction1)
        filemenu.addAction(exitAction2)

        self.lable = QTableWidget(self)
        self.lable.setRowCount(4)
        self.lable.setColumnCount(3)
        self.lable.setGeometry(QtCore.QRect(10, 20, 300, 200))
        for i in range(4):
            for j in range(3):
                num = random.randint(1, 10000)
                qtable_color = QTableWidgetItem(str(num))
                qtable_color.setBackground(QBrush(QColor(255, 128, 0)))
                qtable_color.setBackground(QBrush(QColor(20, 120, 255)))
                self.lable.setItem(i, j, qtable_color)
        self.button = QPushButton(self)
        self.button.setGeometry(QtCore.QRect(50, 250, 100, 30))
        self.button.setText('点击排序')
        # 设置默认为降序排列
        self.button.clicked.connect(self.order)
        self.orderType = Qt.DescendingOrder

    def order(self):
        if self.orderType == Qt.DescendingOrder:
            self.orderType = Qt.AscendingOrder
        else:
            self.orderType = Qt.DescendingOrder
        self.lable.sortItems(2, self.orderType)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    labelDemo = QlabelDemo()
    labelDemo.show()
    sys.exit(app.exec_())
