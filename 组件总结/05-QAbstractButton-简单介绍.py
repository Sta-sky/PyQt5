# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QAbstractButton")
window.resize(500, 500)

class Btn(QAbstractButton):
    def paintEvent(self, evt):
        # print("绘制按钮")
        # 绘制按钮上要展示的一个界面内容
        # 可以看不懂
        # 1 创建一个画家, 画在什么地方
        painter = QPainter(self)

        # 2 给画家一个笔
        # 2.1 创建一个笔
        pen = QPen(QColor(111, 200, 20), 5)
        # 2.2 设置这个笔
        painter.setPen(pen)

        # 3 画家画
        painter.drawText(25, 40, self.text())

        painter.drawEllipse(0, 0, 100, 100)

btn = Btn(window)
btn.setText("xxx")
btn.resize(100, 100)

btn.pressed.connect(lambda : print("点击了这个按钮"))




# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())