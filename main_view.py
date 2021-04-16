import os
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from set_label import SetLabel
from set_table import SetTable
from set_text import SetText


class MyMainView(QMainWindow, SetTable, SetLabel, SetText):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SetView")
        # 设置字体
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setGeometry(QtCore.QRect(100, 100, 1300, 800))
        self.table_init(self)
        self.label_init(self)
        self.text_init(self)

        # 表格点击事件
        self.table_view.cellClicked.connect(self.handle_signal)


    def handle_signal(self, row, col):
        info= None
        try:
            content = self.table_view.item(row, col).text()
            info = f"""
             <font color='red' size='10'><red>
            行信息为 {str(row)}, <br>
            行信息为 {str(col)} <br>
            内容为 {str(content)}
             </font>
            """
            if row == 1 and col == 1:
                self.label_view.setPixmap(QPixmap('./test1.png'))
            if row == 1 and col == 2:
                self.label_view.setPixmap(QPixmap('./test3.jpG'))
            if row == 1 and col == 3:
                self.label_view.setPixmap(QPixmap('./test2.jpg'))
        except Exception as e:
            print(f'行信息为 {str(row)}')
            print(f'行信息为 {str(col)}')
            print('内容为 None')
            info = f"""
            <font color='red' size='3'><red>
            行信息为 {str(row)}, \n
            行信息为 {str(col)} \n
            内容为 None
            </font>
            """
        finally:
            self.textedit.setHtml(info)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    objs = MyMainView()
    objs.show()
    app.exec_()
