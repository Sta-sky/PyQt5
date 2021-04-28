# -*- coding: utf-8 -*-

'''
    【简介】
	PyQT5中 单元格里面放控件

'''

import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QLine, Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView,
                             QComboBox, QPushButton, QTextEdit, QDialog, QLineEdit, QRadioButton, QCheckBox,
                             QCommandLinkButton, QMessageBox, QInputDialog, QLabel)


class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(430, 300)
        conLayout = QHBoxLayout()  # 创建水平布局文件
        self.tableWidget = QTableWidget()  # 创建一个列表
        self.tableWidget.setRowCount(4)  # 设置行数
        self.tableWidget.setColumnCount(3)  # 设置列数
        conLayout.addWidget(self.tableWidget)  # 添加列表到布局

        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])  # 设置水平表头

        newItem = QTableWidgetItem("张三")  # 添加张三 到（0，0）
        self.tableWidget.setItem(0, 0, newItem)

        self.del_Box = QPushButton('')  # 新建一个下拉组件
        self.label = QPushButton('')  # 新建一个下拉组件
        op = QtWidgets.QGraphicsOpacityEffect()
        # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        op.setOpacity(0)
        self.label.setGraphicsEffect(op)
        self.label.setStyleSheet(''' text-align : center;
                                    background-color : LightCoral;
                                    height : 10px;
                                    font : 13px;''')

        self.del_Box.setMaximumSize(20, 20)
        self.label.setMaximumSize(20, 20)
        icon6 = QIcon()
        icon6.addFile(u"../SemViewUI/images/\u62a5\u544a.png", QSize(), QIcon.Normal, QIcon.Off)
        self.del_Box.setIcon(icon6)
        self.del_Box.setFlat(True)
        self.label.lower()
        widget = QtWidgets.QWidget()
        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.label)
        hLayout.addWidget(self.del_Box)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)

        self.tableWidget.setCellWidget(0, 1, widget)  # 添加下拉组件到列表（0，1）
        info = QTableWidgetItem('3443453425342543')
        info.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.tableWidget.setItem(0, 1, info)
        self.tableWidget.cellClicked.connect(self.handle_table)
        self.del_Box.clicked.connect(self.jump_text)
        self.setLayout(conLayout)

    def comboxSelect(self, index):
        print("combox select index", index)

    def butClick(self):
        print("button click")

    def jump_text(self):
        val, flag = QInputDialog.getText(self, '注释信息', "请输入注释信息", QLineEdit.Normal, 'None')
        print(flag)
        if flag:
            self.echo_info()
        else:
            self.echo_waring()

    def echo_info(self):
        QMessageBox.information(self, "提示", "注释保存成功", QMessageBox.Yes)

    def echo_waring(self):
        QMessageBox.warning(
            self,
            "警告",
            "动作执行失败",
            QMessageBox.Yes)

    def handle_table(self, row, col):
        print(row, col)
        print('fdbgfd')
        content = self.tableWidget.item(row, col).text()
        print(content)
        print(f'当前点击了 ： {row, col} -- 内容为 {content}',)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())
