from PyQt5.QtWidgets import *
import sys


# 第一种  在信号槽中实例化子窗口
# 第二种   在__init__中实例化子窗口


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        button = QPushButton("弹出子窗", self)
        button.clicked.connect(self.show_child)

    def show_child(self):
        self.child_window = Child()
        self.child_window.show()


class Child(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是子窗口啊")


# 运行主窗口
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit(app.exec_())

# class Main(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("主窗口")
#         button = QPushButton("弹出子窗", self)
#         button.clicked.connect(self.show_child)
#         self.child_window = Child()
#
#     def show_child(self):
#         self.child_window.show()
#
#
# class Child(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("我是子窗口啊")
#
#
# # 运行主窗口
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Main()
#     window.show()
#     sys.exit(app.exec_())
