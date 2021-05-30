from PyQt5.Qt import *

class SB(QSpinBox):
    def textFromValue(self, p_int):
        print("xx2", p_int)
        # 1 * 1
        return str(p_int) + "*" + str(p_int)

    def valueFromText(self, p_str):
        print("xxxx", p_str)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        sb = SB(self)
        self.sb = sb
        sb.resize(100, 25)
        sb.move(100, 100)
        sb.valueChanged[str].connect(lambda val: print(type(val), val))

        btn = QPushButton(self)
        btn.setText("测试按钮")
        btn.move(150, 150)
        btn.clicked.connect(lambda :sb.lineEdit().setText("30*30"))

        # self.最大值最小值()

    def 设置以及获取数值(self):
        # self.sb.setRange(0, 9)
        self.sb.setPrefix("撩课")
        # self.sb.setValue(66)
        print(self.sb.value())
        print(self.sb.text())
        print(self.sb.lineEdit().text())
        pass

    def 显示的进制设置(self):
        print(self.sb.displayIntegerBase())
        self.sb.setDisplayIntegerBase(2)
        print(self.sb.displayIntegerBase())

    def 前缀和后缀(self):
        # self.sb.setRange(1, 12)
        # self.sb.setSuffix("月")
        self.sb.setRange(0, 6)
        self.sb.setPrefix("周")
        self.sb.setSpecialValueText("周日")
        pass

    def 步长设置(self):
        self.sb.setSingleStep(3)

    def 数值循环(self):
        print(self.sb.wrapping())
        self.sb.setWrapping(True)
        print(self.sb.wrapping())

    def 最大值最小值(self):
        # self.sb.setMaximum(180)
        # print(self.sb.maximum())
        #
        # self.sb.setMinimum(18)
        # print(self.sb.minimum())
        self.sb.setRange(18, 180)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())