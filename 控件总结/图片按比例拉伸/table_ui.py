from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QTableView, QHeaderView


class MyTable(QTableView):
    def __init__(self, parent):
        super(MyTable, self).__init__()
        self.parent = parent
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

    def mousePressEvent(self, event):
        """鼠标按下事件"""
        if event.button() == Qt.LeftButton:
            print('鼠标左键点击')
        if event.button() == Qt.RightButton:
            print('鼠标右键点击')
        elif event.button() == Qt.MidButton:
            print('鼠标中键点击')

    def mouseMoveEvent(self, e):
        """ 鼠标按下移动事件"""
        print('移动鼠标')

    def mouseReleaseEvent(self, ev):
        """鼠标松开事件"""
        print('松开鼠标')

    def focusInEvent(self, e):
        """聚焦窗口事件"""
        print('窗口焦点聚焦')

    def focusOutEvent(self, ev):
        """从窗口移出，失去聚焦事件"""
        print('窗口焦点消失')

    def enterEvent(self, a0):
        """鼠标进入组件事件"""
        print('进入组件')

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        print(event.key())
        print(Qt.Key_Up)
        print('按下键盘')

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.isAutoRepeat():
            pass
        else:
            print('释放键盘')

