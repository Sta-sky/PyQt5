from IPython.external.qt_for_kernel import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt, QPoint
from PyQt5.QtGui import QPixmap, QPainter, QResizeEvent
from PyQt5.QtWidgets import QLabel


class MyLabel(QLabel):
    def __init__(self, parent):
        super(MyLabel, self).__init__(parent)
        self.setObjectName(u"label")
        self.setMinimumSize(QSize(200, 300))
        self.pixmap = QPixmap('./25.jpg')
        self.point = QPoint(0, 0)

    def init_img(self, path):
        self.pixmap = QPixmap(path)
        if self.pixmap.isNull():
            print("Error: Failed to load image")
            return
        self.update_scale()
        self.update()

    def update_scale(self):
        if self.pixmap.isNull():
            return
        p_size = self.pixmap.size()
        r_size = self.size()
        scale = min(r_size.width() / p_size.width(), r_size.height() / p_size.height())
        new_size = QSize(int(p_size.width() * scale), int(p_size.height() * scale))
        self.scale_img = self.pixmap.scaled(new_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.update_scale()
        super().resizeEvent(event)
        self.update()

    def paintEvent(self, event):
        if self.scale_img.isNull():
            return
        painter = QPainter(self)
        painter.drawPixmap(self.point, self.scale_img)

    def draw_img(self, painter):
        painter.drawPixmap(self.point, self.scale_img)

    def wheelEvent(self, wheel: QtGui.QWheelEvent) -> None:
        val = wheel.angleDelta().y()
        if val > 0:
            print(' 滑轮 up ')
            width = self.width() + 20
        else:
            print('滑轮 down')
            print(self.width())
            width = self.width() - 20
        self.setMinimumWidth(width)

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


