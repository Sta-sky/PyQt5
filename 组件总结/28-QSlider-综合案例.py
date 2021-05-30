from PyQt5.Qt import *

class Slider(QSlider):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setTickPosition(QSlider.TicksBothSides)
        self.setup_ui()

    def setup_ui(self):
        self.label = QLabel(self)
        self.label.setText("0")
        self.label.setStyleSheet("color: red;background-color: green")
        self.label.hide()

    def mousePressEvent(self, evt):
        # QMouseEvent
        super().mousePressEvent(evt)
        x = (self.width() - self.label.width()) / 2
        # y / height = （最大值 - 最小值 - 当前值） / (最大值 - 最小值)
        #
        # y / height = 1 - 当前值 / (最大值 - 最小值)
        #
        # y = (1 - 当前值 / (最大值 - 最小值)) * height
        y = (1 - self.value() / (self.maximum() - self.minimum())) * self.height() - self.label.height()
        self.label.show()
        self.label.move(x, y)

    def mouseMoveEvent(self, evt):
        super().mouseMoveEvent(evt)
        x = (self.width() - self.label.width()) / 2
        # y / height = （最大值 - 最小值 - 当前值） / (最大值 - 最小值)
        #
        # y / height = 1 - 当前值 / (最大值 - 最小值)
        #
        # y = (1 - 当前值 / (最大值 - 最小值)) * height
        y = (1 - self.value() / (self.maximum() - self.minimum())) * (self.height() - self.label.height())
        self.label.show()
        self.label.move(x, y)

        self.label.setText(str(self.value()))
        self.label.adjustSize()

    def mouseReleaseEvent(self, evt):
        super().mouseReleaseEvent(evt)
        self.label.hide()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("综合案例的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 0 创建两个控件
        slider = Slider(self)
        slider.move(200, 200)
        slider.resize(30, 200)




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())