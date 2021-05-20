from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QTableView, QHeaderView


class MyTable(QTableView):
    def __init__(self, parent):
        super(MyTable, self).__init__(parent)
        self.init_table()

    def init_table(self):
        # 设置模型
        self.model = QStandardItemModel(4, 5)
        # 设置表头
        self.model.setHorizontalHeaderLabels(['id', 'name', 'age', 'sex'])
        self.model.setVerticalHeaderLabels(['张三', '里斯', '王五', '赵六', '黄芪'])
        self.move(20, 20)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setModel(self.model)

    def tabletEvent(self, info: QtGui.QTabletEvent) -> None:
        print(info)
        print(info.button())

    def resizeEvent(self, e: QtGui.QResizeEvent) -> None:
        pass

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        print(event.key())
        print(Qt.Key_Up)
        print('按下键盘')

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.isAutoRepeat():
            pass
        else:
            print('释放-=---键盘')

    def mouseReleaseEvent(self, ev):
        """鼠标松开事件"""
        print('松开+---]]]]--+鼠标')
