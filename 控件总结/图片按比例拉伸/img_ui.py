from IPython.external.qt_for_kernel import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt, QPoint
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QLabel


class MyLabel(QLabel):
    def __init__(self, parent):
        super(MyLabel, self).__init__()
        self.parent = parent
        self.setObjectName(u"label")
        self.setMinimumSize(QSize(200, 300))
        self.pixmap = QPixmap('./25.jpg')
        self.point = QPoint(0, 0)

    def init_img(self, path):
        self.pixmap = QPixmap(path)
        self.scale_img = self.pixmap.scaled(self.pixmap.size())
        self.setPixmap(self.scale_img)
        self.resizeEvent('test')

    def resizeEvent(self, info: QtGui.QResizeEvent) -> None:
        r_width = self.width()
        r_height = self.height()
        p_width = self.pixmap.width()
        p_height = self.pixmap.height()
        t_width = r_width / p_width
        t_heigth = r_height / p_height
        if t_width > t_heigth:
            scale = t_heigth
        else:
            scale = t_width
        qsize = QSize(p_width * scale, p_height * scale)
        self.scale_img = self.pixmap.scaled(qsize, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        """绘图"""
        painter = QPainter()
        painter.begin(self)
        self.draw_img(painter)
        painter.end()

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
