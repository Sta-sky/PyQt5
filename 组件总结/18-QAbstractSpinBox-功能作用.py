from PyQt5.Qt import *

class MyASB(QAbstractSpinBox):
    def __init__(self, parent=None, num ="0", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.lineEdit().setText(num)

    def stepEnabled(self):
        # 0 -- 9
        # current_num = int(self.text())
        # if current_num == 0:
        #     return QAbstractSpinBox.StepUpEnabled
        # elif current_num == 9:
        #     return QAbstractSpinBox.StepDownEnabled
        # elif current_num < 0 or current_num > 9:
        #     return QAbstractSpinBox.StepNone
        # else:
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled


    def stepBy(self, p_int):
        current_num = int(self.text()) + p_int
        self.lineEdit().setText(str(current_num))

    def validate(self, p_str, p_int):
        # 18 - 180
        num = int(p_str)
        if num < 18:
            return (QValidator.Intermediate, p_str, p_int)
        elif num <= 180:
            return (QValidator.Acceptable, p_str, p_int)
        else:
            return (QValidator.Invalid, p_str, p_int)

    def fixup(self, p_str):
        print(p_str)
        return "18"

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSpinBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        asb = MyASB(self, "6")
        self.asb = asb
        asb.resize(100, 30)
        asb.move(100, 100)

        self.asb.editingFinished.connect(lambda :print("结束编辑"))

        # print(asb.isAccelerated())
        # asb.setAccelerated(True)
        # print(asb.isAccelerated())

        # print(asb.isReadOnly())
        # asb.setReadOnly(True)
        test_btn = QPushButton(self)
        test_btn.move(200, 200)
        test_btn.setText("测试按钮")
        test_btn.clicked.connect(self.btn_test)

    def btn_test(self):
        # print(self.asb.text())
        # # print(self.asb.lineEdit().text())
        # print(self.asb.lineEdit().setText("88"))
        # QLineEdit
        # cl = QCompleter(["sz", "123", "18"], self.asb)
        # self.asb.lineEdit().setCompleter(cl)
        # # self.asb.lineEdit().setAlignment(Qt.AlignCenter)
        # self.asb.setAlignment(Qt.AlignCenter)

        # print(self.asb.hasFrame())
        # self.asb.setFrame(False)

        # self.asb.clear()
        self.asb.setButtonSymbols(QAbstractSpinBox.NoButtons)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())