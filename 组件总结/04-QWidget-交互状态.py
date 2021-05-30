# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def paintEvent(self, evt):
        print("窗口被绘制了")
        return super().paintEvent(evt)

class Btn(QPushButton):
    def paintEvent(self, evt):
        print("按钮被绘制了")
        return super().paintEvent(evt)

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle("交互状态")
window.resize(500, 500)


btn = Btn(window)
btn.setText("按钮")
btn.destroyed.connect(lambda : print("按钮被释放了"))

# btn.setVisible(False)
# btn.setHidden(True)
# btn.hide()

# btn.deleteLater()
btn.setAttribute(Qt.WA_DeleteOnClose, True)
# btn.close()
btn.setVisible(False)



# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())