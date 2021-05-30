import sys
from PyQt5.Qt import *

class App(QApplication):
    def notify(self, recevier, evt):
        if recevier.inherits("QPushButton") and evt.type() == QEvent.MouseButtonPress:
            print(recevier, evt)

        return super().notify(recevier, evt)

class Btn(QPushButton):
    def event(self, evt):
        if evt.type() == QEvent.MouseButtonPress:
            print(evt)
        return super().event(evt)

    def mousePressEvent(self, *args, **kwargs):
        print("鼠标被按下了......")
        # return super().mousePressEvent(*args, **kwargs)



app = App(sys.argv)

window = QWidget()

btn = Btn(window)
btn.setText("按钮")
btn.move(100, 100)

def cao():
    print("按钮被点击了")

btn.pressed.connect(cao)

window.show()

sys.exit(app.exec_())