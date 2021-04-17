import random

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QBrush, QColor, QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QTableWidget, QTableWidgetItem, QPushButton, \
    QVBoxLayout, QHBoxLayout, QFrame, QSplitter, QWidget, QTextEdit, QLabel
import sys


class QlabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1250, 750)
        self.setWindowTitle('SEMview')
        self.menu()
        self.handle_table()

    def menu(self):
        """菜单"""
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

    def handle_table(self):
        self.table = QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(3)

        for i in range(4):
            for j in range(3):
                num = random.randint(1, 10000)
                qtable_color = QTableWidgetItem(str(num))
                qtable_color.setBackground(QBrush(QColor(255, 128, 0)))
                qtable_color.setBackground(QBrush(QColor(20, 120, 255)))
                self.table.setItem(i, j, qtable_color)
        self.button = QPushButton()
        self.text = QTextEdit()
        self.text.setText("vfdsbfdsbsf")
        self.label = QLabel()
        # 设置可拉伸
        self.mainlayout = QHBoxLayout(self)
        self.text.setFrameShape(QFrame.StyledPanel)
        self.label.setFrameShape(QFrame.StyledPanel)
        img_obj = QPixmap('./test.jpg')
        img_obj = img_obj.scaledToWidth(640)
        img_obj.scaled(400, 400, aspectRatioMode=Qt.KeepAspectRatio)
        self.label.setPixmap(img_obj)
        self.label.setScaledContents(True)

        self.table.setFrameShape(QFrame.StyledPanel)
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(self.label)
        splitter1.setGeometry(QtCore.QRect(10, 20, 400, 200))

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(self.text)
        splitter2.addWidget(self.table)

        splitter3 = QSplitter(Qt.Horizontal)
        splitter3.addWidget(splitter1)
        splitter3.addWidget(splitter2)

        self.mainlayout.addWidget(splitter3)
        self.setLayout(self.mainlayout)
        

        # 设置默认为降序排列
        self.button.setText('点击排序')
        self.orderType = Qt.DescendingOrder
        self.button.clicked.connect(self.order)


    def order(self):
        if self.orderType == Qt.DescendingOrder:
            self.orderType = Qt.AscendingOrder
        else:
            self.orderType = Qt.DescendingOrder
        self.table.sortItems(2, self.orderType)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    labelDemo = QlabelDemo()
    labelDemo.show()
    sys.exit(app.exec_())
