# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class Ui_Message(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(118, 90)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 541, 111))
        # self.frame.setStyleSheet("background-image: url(:/img/messageback.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 110, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: transparent;\n"
                                 "fontsize: 30px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "显示信息"))

# import img_rc


# 定义一个可移动无边框3s提示消息界面
class MessageWindow(Qt.QMainWindow):
    def __init__(self, parent=None):
        Qt.QWidget.__init__(self, parent)
        self.ui = Ui_Message()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        QtCore.QTimer().singleShot(3000, self.close)
        self.show()

    def mousePressEvent(self, event):
        # 定义鼠标点击事件
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        # 定义鼠标移动事件
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def setMessage(self, message):
        self.ui.label.setText(message)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = MessageWindow()
    login.setMessage("我爱中国")
    sys.exit(app.exec())

