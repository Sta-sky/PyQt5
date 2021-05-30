# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

class Label(QLabel):
    def mousePressEvent(self, evt):
        self.raise_()

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("层级关系调整")
window.resize(500, 500)

label1 = Label(window)
label1.setText("标签1")
label1.resize(200, 200)
label1.setStyleSheet("background-color: red;")

label2 = Label(window)
label2.setText("标签2")
label2.resize(200, 200)
label2.setStyleSheet("background-color: green;")
# label2.move(200, 200)
label2.move(100, 100)


# label2.lower()
# label1.raise_()

# label2.stackUnder(label1)

# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())