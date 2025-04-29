from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("事件消息的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        btn = QPushButton(self)
        btn.setText("info")
        btn.setMinimumSize(100, 30)  # 设置按钮的最小大小

        btn1 = QPushButton(self)
        btn1.setText("info1")
        btn1.setMinimumSize(100, 30)  # 设置按钮的最小大小

        btn2 = QPushButton(self)
        btn2.setText("info")
        btn2.setMinimumSize(100, 30)  # 设置按钮的最小大小

        btn3 = QPushButton(self)
        btn3.setText("info1")
        btn3.setMinimumSize(100, 30)  # 设置按钮的最小大小

        layout.addWidget(btn)
        layout.addWidget(btn1)

        layout1.addWidget(btn2)
        layout1.addWidget(btn3)


        layout2.addLayout(layout)
        layout2.addLayout(layout1)


        self.setLayout(layout2)  # 将布局设置为父窗口的布局

    def showEvent(self, QShowEvent):
        print("窗口被展示了出来")

    def closeEvent(self, QCloseEvent):
        print("窗口被关闭了")


    def moveEvent(self, QMoveEvent):
        print("窗口被移动了")

    def resizeEvent(self, QResizeEvent):
        print("窗口改变了尺寸大小")

    def enterEvent(self, QEvent):
        print("鼠标进来了")
        self.setStyleSheet("background-color: yellow;")

    def leaveEvent(self, QEvent):
        print("鼠标移开了")
        self.setStyleSheet("background-color: green;")


    def mousePressEvent(self, QMouseEvent):
        print("鼠标被按下")

    def mouseReleaseEvent(self, QMouseEvent):
        print("鼠标被释放")

    def mouseDoubleClickEvent(self, QMouseEvent):
        print("鼠标双击")

    def mouseMoveEvent(self, QMouseEvent):
        print("鼠标移动了")

    def keyPressEvent(self, QKeyEvent):
        print("键盘上某一个按键被按下了")

    def keyReleaseEvent(self, QKeyEvent):
        print("键盘上某一个按键被释放了")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())