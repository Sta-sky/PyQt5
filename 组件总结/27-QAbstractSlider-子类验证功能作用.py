from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSlider的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        label = QLabel(self)
        label.setText("0")
        label.move(200, 200)
        label.resize(100, 30)
        # print(QAbstractSlider.__subclasses__())
        sd = QSlider(self)
        sd.move(100, 100)
        # sd.valueChanged.connect(lambda val:label.setText(str(val)))
        sd.valueChanged.connect(lambda :label.setText(str(sd.value())))

        # 设置最大值 最小值
        sd.setMaximum(100)
        sd.setMinimum(0)

        # 当前数值
        # sd.setValue(88)

        # 步长设置
        # sd.setSingleStep(5)
        # sd.setPageStep(8)

        # 跟踪设置
        # print(sd.hasTracking())
        # sd.setTracking(False)

        # 滑块位置的设置
        # sd.setSliderPosition(88)



        # 倒立外观
        # sd.setInvertedAppearance(True)
        # sd.setInvertedControls(True)
        # sd.setOrientation(Qt.Horizontal)


        # sd.sliderMoved.connect(lambda val:print(val))
        # sd.actionTriggered.connect(lambda val:print(val))
        sd.rangeChanged.connect(lambda min, max:print(min, max))

        sd.setMaximum(99)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())