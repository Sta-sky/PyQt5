import random

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QTableView, QLabel, QPushButton, QHBoxLayout, QApplication
from SemView.data import col_list, table_data, row_num_list
from util.tools import set_font


class SetTable:
    def table_init(self):
        # 创建表格
        self.table_view = QtWidgets.QTableWidget(self)
        self.table_view.setRowCount(10)
        self.table_view.setColumnCount(5)
        self.table_view.setHorizontalHeaderLabels(col_list)
        self.table_view.setGeometry(QtCore.QRect(800, 450, 450, 300))
        self.table_view.setVerticalHeaderLabels(row_num_list)
        self.table_view.setObjectName('table_view')
        table_data(self.table_view)
        # 设置表格不可编辑
        self.table_view.setEditTriggers(QTableView.NoEditTriggers)
        # 表格自适应宽高
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view.setStyleSheet(
            '''QWidget{min-height: 20px; font-size:10pt;border-radius:3px;background-color:rgb(240,248,255);color: rgb(0,0,0)}'''
        )
        
        # item = QTextEdit()
        # self.table_view.setCellWidget(2, 2, item)
        item = QTableWidgetItem("test")
        self.table_view.setItem(2, 2, item)

    # 创建标签的label
        self.label_view_but = QLabel()
        # 设置label的位置
        self.table_btn1 = QPushButton("Table View 格式显示")
        self.table_btn2 = QPushButton("wafer View 格式显示")
        
        # 初始化一个 垂直 布局管理器
        self.v_lable = QHBoxLayout()
        self.v_lable.addWidget(self.table_btn1)
        self.v_lable.addWidget(self.table_btn2)
        
        # 将布局管理器加入标签控件中
        self.label_view_but.setLayout(self.v_lable)
        self.label_view_but.setGeometry(QtCore.QRect(0,0,0,30))
        
        # 添加排序按钮
        self.tab_bnt_sort = QLabel()
        self.tab_bnt_sort.setFont(set_font())
        self.tab_sort_click1 = QPushButton("降序排列")
        self.tab_sort_click2 = QPushButton("升序排列")
        self.tab_sort_click3 = QPushButton("恢复原始数据")
        self.sort_btn_boxloyout = QHBoxLayout()
        sort_list_but = [self.tab_sort_click1, self.tab_sort_click2, self.tab_sort_click3]
        [self.sort_btn_boxloyout.addWidget(sort_item) for sort_item in sort_list_but]
        self.tab_bnt_sort.setLayout(self.sort_btn_boxloyout)
        [item.setStyleSheet('background-color:lightblue') for item in sort_list_but]
        self.tab_bnt_sort.setGeometry(QtCore.QRect(0, 0, 0, 50))

    def keyPressEvent(self, event):
        res = None
        try:
            # 这里event.key（）显示的是按键的编码
            print("按下：" + str(event.key()))
            # 举例，这里Qt.Key_A注意虽然字母大写，但按键事件对大小写不敏感
            if (event.key() == Qt.Key_Escape):
                res = '测试：ESC'
            elif (event.key() == Qt.Key_A):
                res = '测试：A'
            elif (event.key() == Qt.Key_1):
                res = '测试：1'
            elif (event.key() == Qt.Key_Enter):
                res = '测试：Enter'
            elif (event.key() == Qt.Key_Space):
                res = '测试：Space'
            elif (event.key() == Qt.Key_Tab):
                res = '测试：Table'
            # 当需要组合键时，要很多种方式，这里举例为“shift+单个按键”，也可以采用shortcut、或者pressSequence的方法。
            elif (event.key() == Qt.Key_P):
                if QApplication.keyboardModifiers() == Qt.ShiftModifier:
                    res = "shift + p"
            elif (event.key() == Qt.Key_O) and QApplication.keyboardModifiers() == Qt.ShiftModifier:
                res = "shift + o"
            else:
                res = f'结果： {event.key()}'
        except Exception as e:
            pass
        finally:
            self.text_edit.setText(res)

    # 响应鼠标事件
    def mousePressEvent(self, event):
        res = None
        try:
            if event.button() == Qt.LeftButton:
                res = "鼠标左键点击"
            elif event.button() == Qt.RightButton:
                res = "鼠标右键点击"
            elif event.button() == Qt.MidButton:
                res = "鼠标中键点击"
        except Exception as e:
            pass
        finally:
            self.text_edit.setText(res)