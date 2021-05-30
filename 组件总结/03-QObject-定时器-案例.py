# 0. 导入需要的包和模块
from PyQt5.Qt import * 
import sys

class MyObject(QObject):
    def timerEvent(self, evt):
        print(evt, "1")

class MyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("10")
        self.move(100, 100)
        self.setStyleSheet("font-size: 22px;")

    def setSec(self, sec):
        self.setText(str(sec))

    def startMyTimer(self, ms):
        self.timer_id = self.startTimer(ms)

    def timerEvent(self, *args, **kwargs):
        print("xx")
        # 1. 获取当前的标签的内容
        current_sec = int(self.text())
        current_sec -= 1
        self.setText(str(current_sec))

        if current_sec == 0:
            print("停止")
            self.killTimer(self.timer_id)


class MyWidget(QWidget):
    def timerEvent(self, *args, **kwargs):
        current_w = self.width()
        current_h = self.height()
        self.resize(current_w + 10, current_h + 10)

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)


# 2. 控件的操作
# 2.1 创建控件
window = MyWidget()
# 2.2 设置控件
window.setWindowTitle("QObject定时器的使用")
window.resize(500, 500)

window.startTimer(100)



# label = MyLabel(window)
# label.setSec(5)
# label.startMyTimer(500)



# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())