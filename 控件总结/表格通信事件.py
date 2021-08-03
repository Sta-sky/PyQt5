import random
import sys

from PyQt5.QtGui import QColor, QBrush, QFont
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QApplication, QHBoxLayout, QMessageBox


class TableMain(QWidget):
    def __init__(self):
        super(TableMain, self).__init__()
        self.resize(1000, 700)
        self.table_view = QTableWidget()
        self.table_view.setColumnCount(10)
        self.table_view.setRowCount(5)
        for i in range(5):
            for j in range(10):
                num = str(random.randint(1, 10000))
                self.table_view.setItem(i, j, QTableWidgetItem(num))
        # 获取表头内容
        box = QHBoxLayout()
        box.addWidget(self.table_view)
        self.setLayout(box)

        # 表头单击信号
        self.table_view.verticalHeader().sectionClicked.connect(self.handle_col_signal)
        self.table_view.horizontalHeader().sectionClicked.connect(self.handle_row_signal)

        # 单元格数据发生改变触发
        self.table_view.cellChanged.connect(self.change_data_handle)

        # 单机表格中内容触发  clicked、cellClicked、cellPressed作用基本一致,区别clicked不反回行列
        # self.table_view.cellClicked.connect(self.click_once_handle)

        # 双击表格发生触发
        # self.table_view.cellDoubleClicked.connect(self.click_double_handle)

        # 选中单元格发生变化时，返回之前的单元格跟当前选中的单元格
        # self.table_view.currentCellChanged.connect(self.current_pre_table_handle)

        # 返回当前选中行跟之前选中行的对象   currentItemChanged
        # self.table_view.currentItemChanged.connect(self.item_obj_handle)

        # 双击返回单个表格对象  itemClicked
        # self.table_view.itemClicked.connect(self.double_click_handle)

        # 双击返回单个表格对象  itemDoubleClicked
        # self.table_view.itemDoubleClicked.connect(self.double_click_handle)

    def handle_col_signal(self, index):
        QMessageBox.information(self, '展示详情', f'这col是index： {index}', QMessageBox.Yes)

    def handle_row_signal(self, index):
        QMessageBox.warning(self, '警告', f'这是row  index： {index}', QMessageBox.Yes)

    def change_data_handle(self):
        QMessageBox.warning(self, '警告', f'警告', QMessageBox.Yes)

    def click_once_handle(self):
        QMessageBox.warning(self, '警告', f'警告', QMessageBox.Yes)

    def click_double_handle(self):
        QMessageBox.warning(self, '警告', f'警告', QMessageBox.Yes)

    def current_pre_table_handle(self, row, col, pre_row, pre_col):
        QMessageBox.warning(self, '警告', f'我触发了{row, col, pre_row, pre_col}', QMessageBox.Yes)

    def item_obj_handle(self, pre_obj, subfix_obj):
        print(pre_obj, subfix_obj)
        QMessageBox.warning(self, '警告', f'{pre_obj, subfix_obj}', QMessageBox.Yes)

    def double_click_handle(self, obj):
        fond = QFont()
        fond.setFamily('楷体')
        fond.setBold(True)
        fond.setPointSize(12)
        QMessageBox.warning(self, '警告',
                            f'{obj.setBackground(QBrush(QColor(220, 25, 155))), obj.setFont(fond)}',
                            QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableMain()
    main.show()
    sys.exit(app.exec_())















"""
activated(QModelIndex) 当用户激活index指定的项目时，发出信号
cellActivated(int，int) 单元格被激活时，发出信号，并传递(行，列)
cellChanged(int，int) 单元格中的项目数据发生更改时，发出信号，并传递(行，列)
cellClicked(int，int) 单击表格中的单元格，发出信号，并传递(行，列)
cellDoubleClicked(int，int) 双击表格中的单元格，发出信号，并传递(行，列)
cellEntered(int，int) 当鼠标光标进入单元格时，发出信号，并传递(行，列)
cellPressed(int，int) 按下表格中的单元格，发出信号，并传递(行，列)
clicked(QModelIndex) 左键单击鼠标按钮时，发出此信号
currentCellChanged(int，int，int，int) 单元格发生变化，发出信号(当前单元格的行列，先前具有焦点的单元格行列)
currentItemChanged(QTableWidgetItem*，QTableWidgetItem*) 项目发生变化，发出信号(当前项目，先前项目)
doubleClicked(QModelIndex) 双击鼠标按钮时，发出此信号
entered(QModelIndex) 当鼠标光标进入index指定的项目时，发出此信号
iconSizeChanged(QSize) 在视图可见时设置此图标大小时，发出此信号
itemActivated(QTableWidgetItem*) 表中项目被激活时，发出信号，并传递(项目)
itemChanged(QTableWidgetItem*) 表中项目数据发生变化，发出信号，并传递(项目)
itemClicked(QTableWidgetItem*) 单击表中的项目，发出信号，并传递(项目)
itemDoubleClicked(QTableWidgetItem*) 双击表格中的项目，发出信号，并传递(项目)
itemEntered(QTableWidgetItem*) 当鼠标光标进入项目时，发出信号，并传递(项目)
itemPressed(QTableWidgetItem*) 按下表格中的项目，发出信号，并传递(项目)
itemSelectionChanged() 选择发生变化，发出信号
pressed(QModelIndex) 按下鼠标按钮时会发出此信号
viewportEntered() 当鼠标光标进入视图时会发出此信号

"""
