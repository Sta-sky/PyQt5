import random

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QTableView, QLabel, QPushButton, QHBoxLayout

from util.tools import handle_img


class SetTable:
    def table_init(self):
        self.table_view = QtWidgets.QTableWidget(self)
        self.table_view.setRowCount(10)
        self.table_view.setColumnCount(5)
        self.table_view.setHorizontalHeaderLabels(['工号', '姓名', '年龄', '性别', '职称'])
        self.table_view.setVerticalHeaderLabels(
            ['Mask1', 'Mask2', 'Mask3', 'Mask4', 'Mask5', 'Mask6', 'Mask7', 'Mask8', 'Mask9', 'Mask10'])
        for i in range(10):
            for j in range(5):
                if j == 4:
                    continue
                random_num = random.randint(1, 10000)
                self.table_view.setItem(i, j, QTableWidgetItem(str(random_num)))
        self.table_view.setGeometry(QtCore.QRect(800, 450, 450, 300))
        self.table_view.setObjectName('table_view')
        # 设置表格不可编辑
        self.table_view.setEditTriggers(QTableView.NoEditTriggers)
        # 表格自适应宽高
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        


    # 创建标签的label
        self.label_view_but = QLabel()
        # 设置label的位置
        self.img_btn1 = QPushButton("Table View 格式显示")
        self.img_btn2 = QPushButton("wafer View 格式显示")
        # 初始化一个 垂直 布局管理器
        self.v_lable = QHBoxLayout()
        self.v_lable.addWidget(self.img_btn1)
        self.v_lable.addWidget(self.img_btn2)
        # 将布局管理器加入标签控件中
        self.label_view_but.setLayout(self.v_lable)
        self.label_view_but.setGeometry(QtCore.QRect(0,0,0,30))

        self.img_btn1.clicked.connect(self.img_btn1_Clicked)
        self.img_btn2.clicked.connect(self.img_btn2_Clicked)

    def img_btn1_Clicked(self):
        self.label_view.setPixmap(QPixmap(handle_img(self, '../util/test.jpg')))

    def img_btn2_Clicked(self, info):
        self.label_view.setPixmap(QPixmap(handle_img(self, '../util/test1.png')))