import random

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QTableWidget, QTableWidgetItem, QPushButton, \
    QVBoxLayout, QHBoxLayout, QFrame, QSplitter
import sys


class QlabelDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1250, 750)
        self.setWindowTitle('SEMview')
        self.addStretch(1)
        self.menu()

        self.mainlayout = QHBoxLayout(self)
        self.right_top = QFrame()
        self.right_top.setFrameShape(QFrame.StyledPanel)
        self.right_botm = QFrame()
        self.right_botm.setFrameShape(QFrame.Box)
        self.left_box = QFrame()
        self.left_box.setFrameShape(QFrame.StyledPanel)
        self.left_box.setLineWidth(100)
        self.splitter1 = QSplitter(Qt.Horizontal)
        self.splitter1.addWidget(self.right_top)
        self.splitter2 = QSplitter(Qt.Vertical)
        self.splitter2.addWidget(self.left_box)
        self.splitter2.addWidget(self.right_botm)
        self.splitter3 = QSplitter(Qt.Horizontal)
        self.splitter3.addWidget(self.splitter1)
        self.splitter3.addWidget(self.splitter2)


        self.lable = QTableWidget(self.right_botm)
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



    def menu(self):
        self.action = QAction(self)
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
