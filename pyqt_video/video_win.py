# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtMultimediaWidgets import QVideoWidget

from utils import echo


class myVideoWidget(QVideoWidget):
    doubleClickedItem = pyqtSignal(str)  # 创建双击信号
    wheelItem = pyqtSignal(str)  # 创建鼠标滚轮信号
    mouseclick = pyqtSignal(str)  # 创建鼠标单击信号

    def __init__(self, parent=None):
        super(QVideoWidget, self).__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground, False)

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
            
    def mousePressEvent(self,  event: QMouseEvent) -> None:
        info = 'None'
        if event.button() == Qt.LeftButton:
            info = '鼠标左键点击'
        elif event.button() == Qt.RightButton:
            info = '鼠标右键点击'
        elif event.button() == Qt.MidButton:
            info = '鼠标中键点击'
        self.mouseclick.emit(info)
        