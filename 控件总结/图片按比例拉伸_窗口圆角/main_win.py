# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainterPath, QPainter, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QAbstractItemView
from main_ui import Ui_MainWindow


class MyMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.table_view.clicked.connect(self.handle_click)
        self.table_view.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.border_width = 8
        self.move_flag = False
        self.drag_start_pos = None
        self.window_start_pos = None

    def handle_click(self, index):
        print(f"Clicked: Row {index.row()}, Column {index.column()}, Data: {index.data()}")

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, '退出确认', '确定要退出吗？',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制阴影
        path = QPainterPath()
        path.addRoundedRect(QRectF(10, 10, self.width() - 20, self.height() - 20), 10, 10)
        painter.fillPath(path, QBrush(QColor(220, 220, 220, 50)))

        # 绘制白色背景
        painter.setBrush(QBrush(Qt.white))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(QRectF(9, 9, self.width() - 18, self.height() - 18), 10, 10)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.move_flag = True
            self.drag_start_pos = event.globalPos()
            self.window_start_pos = self.pos()

    def mouseMoveEvent(self, event):
        if self.move_flag and event.buttons() & Qt.LeftButton:
            if self.drag_start_pos and self.window_start_pos:
                delta = event.globalPos() - self.drag_start_pos
                new_pos = self.window_start_pos + delta
                self.move(new_pos)

    def mouseReleaseEvent(self, event):
        self.move_flag = False
        self.drag_start_pos = None
        self.window_start_pos = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMain()
    window.show()
    sys.exit(app.exec_())