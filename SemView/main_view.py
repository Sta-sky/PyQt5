import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFrame, QSplitter, QHBoxLayout, QWidget

from SemView.set_label import SetLabel
from SemView.set_table import SetTable
from SemView.set_text import SetText
from util.tools import handle_img, set_font


class MyMainView(QWidget, SetTable, SetLabel, SetText):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SetView")
        # 设置字体
        font = set_font()
        if font:
            self.setFont(font)
        self.setAutoFillBackground(False)
        self.setGeometry(QtCore.QRect(125, 125, 1700, 900))
        self.table_init()
        self.label_init()
        self.text_init()
        self.init_ui()
    
    def init_ui(self):
        """
        初始化界面框
        """
        self.table_view.setFrameShape(QFrame.StyledPanel)
        self.label_view.setFrameShape(QFrame.StyledPanel)
        self.text_view.setFrameShape(QFrame.StyledPanel)
        
        # 初始化横向布局管理器
        self.mainlayout = QHBoxLayout(self)
        
        # 将label 图片框加入spltter1  内部垂直
        splitter1 = QSplitter(Qt.Vertical)
        splitter1.addWidget(self.label_view)
        
        # splitter2 为内部垂直垂直
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(self.text_view)
        splitter2.addWidget(self.table_view)
        splitter2.addWidget(self.label_view_but)

        # splitter3 为内部水平，  将slitter1， splitter2 加入3中， 1，2构成水平排布方式，
        splitter3 = QSplitter(Qt.Horizontal)
        splitter3.addWidget(splitter1)
        splitter3.addWidget(splitter2)
     
        # 将spltter3 加入布局管理器中，
        self.mainlayout.addWidget(splitter3)
        # 将布局管理器加入 主界面中
        self.setLayout(self.mainlayout)
        
        # 初始化框中信息
        self.text_edit.setText("请点击表格查看详细数据")

        # 表格点击事件
        self.table_view.cellClicked.connect(self.handle_signal)

    def handle_signal(self, row, col):
        info= None
        try:
            content = self.table_view.item(row, col).text()
            info = f"""<font color='red' size='10'><red>行信息为 {str(row)}, <br>
                    行信息为 {str(col)} <br>内容为 {str(content)}</font>"""
            print(info)
            if row == 1 and col == 1:
                img_obj = handle_img(self, '../util/test1.png')
                self.label_view.setPixmap(QPixmap(img_obj))
            elif row == 1 and col == 2:
                img_obj = handle_img(self, '../util/test3.jpg')
                self.label_view.setPixmap(QPixmap(img_obj))
            elif row == 1 and col == 3:
                img_obj = handle_img(self, '../util/test2.jpg')
                self.label_view.setPixmap(QPixmap(img_obj))
            else:
                img_obj = handle_img(self, '../util/test4.jpg')
                self.label_view.setPixmap(QPixmap(img_obj))
        except Exception as e:
            print(e)
            print(f'行信息为 {str(row)}')
            print(f'行信息为 {str(col)}')
            print('内容为 None')
            info = f"""<font color='red' size='3'><red>行信息为 {str(row)},
                    \n行信息为 {str(col)} \n    内容为 None </font>"""
            self.label_view.setText("当前数据无图片可显示")
        finally:
            self.text_edit.setHtml(info)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    objs = MyMainView()
    objs.show()
    app.exec_()
