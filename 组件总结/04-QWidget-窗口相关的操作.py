# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):

        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.resize(500, 500)
window.setWindowTitle("w1")

# icon = QIcon("xxx.png")
# window.setWindowIcon(icon)
#
# # QIcon
# print(window.windowIcon())
#
# window.setWindowTitle("社会我顺哥,")
# print(window.windowTitle())
#
# window.setWindowOpacity(0.9)
# print(window.windowOpacity())

# print(window.windowState() == Qt.WindowNoState)

# window.setWindowState(Qt.WindowMinimized)
# window.setWindowState(Qt.WindowMaximized)
# window.setWindowState(Qt.WindowFullScreen)


# w2 = QWidget()
# w2.setWindowTitle("w2")


# 2.3 展示控件
window.show()

# window.showMaximized()

# window.showFullScreen()
# window.showMinimized()

# window.setWindowState(Qt.WindowActive)

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())