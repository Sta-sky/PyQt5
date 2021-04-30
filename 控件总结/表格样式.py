import random
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QTableWidget, QTableWidgetItem, QApplication, \
    QHeaderView, QMessageBox


class Mian(QWidget):
    def __init__(self):
        super(Mian, self).__init__()
        self.resize(1000, 700)
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(4)
        row = ['1', '2', '3', '4']
        col = ['name', 'age', 'sex', 'hobi']
        self.tableWidget.setHorizontalHeaderLabels(col)
        self.tableWidget.setVerticalHeaderLabels(row)

        # 自动分配宽高
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 可手动调整宽高
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

        # 固定宽高
        # self.tableWidget.verticalHeader().setVisible(False)
        # self.tableWidget.horizontalHeader().setVisible(False)

        # 显示下方水平的进度条
        # self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        # 隐藏竖直进度条
        # self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # 自适应填充
        # self.tableWidget.horizontalHeader().setStretchLastSection(True)

        # 去掉边框
        # self.tableWidget.setShowGrid(False)

        # 获取表格的行头 列头
        # row_header = self.tableWidget.verticalHeaderItem(row).text()
        # col_header = self.tableWidget.horizontalHeaderItem(col).text()

        res = self.tableWidget.item(1, 1)
        print(res)
        for i in range(4):
            for j in range(5):
                num = random.randint(1, 10000)
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(num)))
        box = QHBoxLayout()
        box.addWidget(self.tableWidget)
        self.setLayout(box)
        self.tableWidget.clicked.connect(self.handle)

    def handle(self):
        try:
            res = self.tableWidget.isSortingEnabled()
            if not res:
                self.tableWidget.setSortingEnabled(True)
            QMessageBox.information(self, '提示', f'{res}', QMessageBox.Ok)
        except Exception as e:
            print('进来了')
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mian()
    window.show()
    sys.exit(app.exec_())
