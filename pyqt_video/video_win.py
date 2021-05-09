# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtMultimediaWidgets import QVideoWidget

from utils import echo


class myVideoWidget(QVideoWidget):
    doubleClickedItem = pyqtSignal(str)  # 创建双击信号
    wheelItem = pyqtSignal(str)  # 创建双击信号

    def __init__(self, parent=None):
        super(QVideoWidget, self).__init__(parent)

    def mouseDoubleClickEvent(self, QMouseEvent):  # 双击事件
        self.doubleClickedItem.emit("double clicked")
        
    def wheelEvent(self, wheelEvent):
        try:
            voice_res = str(wheelEvent.angleDelta())
            res = tuple(eval(voice_res.replace('PyQt5.QtCore.QPoint', '')))
            res = str(res[-1])
            self.wheelItem.emit(f'{res}')
        except Exception as e:
            echo(self, str(e))