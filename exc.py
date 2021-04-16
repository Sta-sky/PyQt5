from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush
from PyQt5.QtWidgets import QComboBox, QFrame, QTableWidget, QTableWidgetItem, QHeaderView


class SetTable:
    def ui_init(self, BaseForm):
        BaseForm.setWindowTitle("SetView")
        # BaseForm.resize(1500, 1000)
        BaseForm.setGeometry(QtCore.QRect(100, 100, 1300, 800))
        # 设置字体
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        BaseForm.setFont(font)
        BaseForm.setAutoFillBackground(False)

        self.table_view = QtWidgets.QTableWidget(BaseForm)
        self.table_view.setRowCount(10)
        self.table_view.setColumnCount(5)
        self.table_view.setHorizontalHeaderLabels(['工号', '姓名', '年龄', '性别', '职称'])
        self.table_view.setVerticalHeaderLabels(
            ['Mask1', 'Mask2', 'Mask3', 'Mask4', 'Mask5', 'Mask6', 'Mask7', 'Mask8', 'Mask9', 'Mask10'])
        self.table_view.setGeometry(QtCore.QRect(750, 450, 500, 300))
        self.table_view.setObjectName('table_view')

        # 表格自适应宽高
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.retranslateUi(BaseForm)
        QtCore.QMetaObject.connectSlotsByName(BaseForm)

    def retranslateUi(self, dataBaseForm):
        _translate = QtCore.QCoreApplication.translate
        dataBaseForm.setWindowTitle(_translate("dataBaseForm", "TableView数据库视图-liangfu"))
















#
# from PyQt5 import QtCore
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont, QBrush
# from PyQt5.QtWidgets import QComboBox, QFrame, QTableWidget, QTableWidgetItem
#
#
# class SetTable:
#     def ui_init(self, BaseForm):
#         self.table = QTableWidget(2, 5)
#         self.table.setHorizontalHeaderLabels(['工号', '姓名', '年龄', '性别', '职称'])
#         self.table.setVerticalHeaderLabels(['Mask1', 'Mask2'])
#         # self.table.setEditTriggers(Qself.tableWidget.NoEditTriggers)  # 设置表格不可编辑
#         self.table.setSelectionBehavior(QTableWidget.SelectColumns)
#         self.table.setSelectionMode(QTableWidget.SingleSelection)
#         self.table.setGeometry(QtCore.QRect(10, 80, 300, 350))
#
#         for index in range(self.table.columnCount()):
#             headItem = self.table.horizontalHeaderItem(index)
#             headItem.setFont(QFont("song", 12, QFont.Bold))
#             headItem.setForeground(QBrush(Qt.gray))
#             headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
#
#         self.table.setColumnWidth(4, 100)
#         self.table.setRowHeight(0, 40)
#         # self.table.setFrameShape(QFrame.HLine)  # 设定样式
#         # self.table.setShowGrid(False)  # 取消网格线
#         # self.table.verticalHeader().setVisible(False)  # 隐藏垂直表头
#
#         self.table.setItem(0, 0, QTableWidgetItem("001"))
#         self.table.setItem(0, 1, QTableWidgetItem("Tom"))
#         genderComb = QComboBox()
#         genderComb.addItem("男性")
#         genderComb.addItem("女性")
#         genderComb.setCurrentIndex(0)
#         self.table.setCellWidget(0, 2, genderComb)
#         self.table.setItem(0, 3, QTableWidgetItem("30"))
#         self.table.setItem(0, 4, QTableWidgetItem("产品经理"))
#
#         self.table.setItem(1, 0, QTableWidgetItem("005"))
#         self.table.setItem(1, 1, QTableWidgetItem("Kitty"))
#         genderComb = QComboBox()
#         genderComb.addItem("男性")
#         genderComb.addItem("女性")
#         genderComb.setCurrentIndex(1)
#         self.table.setCellWidget(1, 2, genderComb)
#         self.table.setItem(1, 3, QTableWidgetItem("24"))
#         self.table.setItem(1, 4, QTableWidgetItem("程序猿安慰师"))
#
#         row_count = self.table.rowCount()
#         self.table.insertRow(row_count)
#
#         # 允许右键产生菜单
#         self.table.setContextMenuPolicy(Qt.CustomContextMenu)
#         # 将右键菜单绑定槽函数
#         # self.table.customContextMenuRequested.connect(Menu())
#
#
# #
# # def Menu(pos):
# #     row_num = -1
# #     for i in self.self.table.selectionModel().selection().indexes():
# #         row_num = i.row()
# #     # 表格中只有两行数据，所以只在前两行支持右键弹出菜单
# #     if row_num < 2:
# #         menu = QMenu()
# #         item1 = menu.addAction(u'选项1')
# #         item2 = menu.addAction(u'选项2')
# #         item3 = menu.addAction(u'选项3')
# #         action = menu.exec_(self.self.table.mapToGlobal(pos))

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication



class MyMainView(QMainWindow, SetTable):
    def __init__(self):
        super().__init__()
        self.ui_init(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    objs = MyMainView()
    objs.show()
    app.exec_()
