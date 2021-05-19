# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from 控件总结.图片按比例拉伸.label_img_ui import Ui_MainWindow


class MyMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMain, self).__init__()
        self.setupUi(self)
        self.table_view.clicked.connect(self.handle)

    def handle(self):
        index = self.table_view.currentIndex()
        print(index.row(), index.column(), index.data(), index.flags())

    def closeEvent(self, event):
        quitMsgBox = QMessageBox()
        quitMsgBox.setWindowTitle('确认提示')
        quitMsgBox.setText('你确认退出吗？')
        quitMsgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = quitMsgBox.button(QMessageBox.Yes)
        buttonY.setText('确定')
        buttonN = quitMsgBox.button(QMessageBox.No)
        buttonN.setText('取消')
        quitMsgBox.exec_()
        if quitMsgBox.clickedButton() == buttonY:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyMain()
    main.show()
    sys.exit(app.exec_())

