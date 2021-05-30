from PyQt5.Qt import *

class MyDoubleSB(QDoubleSpinBox):
    def textFromValue(self, p_float):
        print("xxxxx", p_float)
        return str(p_float) + "*" + str(p_float)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDoubleSpinBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        dsb = MyDoubleSB(self)
        dsb.move(100, 100)
        dsb.resize(100, 30)
        # 0.00 - 99.99
        # dsb.setMaximum(88.88)
        # dsb.setMinimum(22.22)
        #
        # dsb.setSingleStep(0.02)
        #
        # dsb.setWrapping(True)
        #
        dsb.setPrefix("$")
        dsb.setSuffix("%")
        # dsb.setRange(1.0, 2.0)
        # dsb.setSingleStep(0.5)
        # dsb.setSuffix("倍速")
        # dsb.setSpecialValueText("正常")
        # dsb.setWrapping(True)
        #
        # dsb.setDecimals(1)

        test_btn = QPushButton(self)
        test_btn.move(300, 300)
        test_btn.setText("测试按钮")
        # test_btn.clicked.connect(lambda :dsb.setValue(-166.66))
        # test_btn.clicked.connect(lambda :print(type(dsb.value()), dsb.value()))
        # test_btn.clicked.connect(lambda :print(type(dsb.cleanText()), dsb.cleanText()))
        # test_btn.clicked.connect(lambda :print(type(dsb.text()), dsb.text()))
        test_btn.clicked.connect(lambda :print(type(dsb.lineEdit().text()), dsb.lineEdit().text()))

        # dsb.valueChanged.connect(lambda val: print(val, type(val)))
        dsb.valueChanged[str].connect(lambda val: print(val, type(val)))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())