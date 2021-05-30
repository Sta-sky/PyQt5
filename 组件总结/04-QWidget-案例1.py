# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

class MyLabel(QLabel):
    def enterEvent(self, *args, **kwargs):
        print("鼠标进入")
        self.setText("欢迎光临")

    def leaveEvent(self, *args, **kwargs):
        print("鼠标离开")
        self.setText("谢谢惠顾")

    def keyPressEvent(self, evt):
        QKeyEvent
        print("xx")
        # if evt.key() == Qt.Key_Tab:
        #     print("用户点击了Tab键位")
        # 修饰键位 Ctrl 并且 普通键位 s
        # if evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_S:
        # 8 4 2 1      5  7 3
        #  3  == 2 | 1
        # 10
        # 01
        # 11  == 3
        if evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and evt.key() == Qt.Key_A:
            print("ctrl + Shift + A被点击了")


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("鼠标操作的案例1")
window.resize(500, 500)

label = MyLabel(window)
label.resize(200, 200)
label.move(100, 100)
label.setStyleSheet("background-color: cyan;")
label.grabKeyboard()


# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())