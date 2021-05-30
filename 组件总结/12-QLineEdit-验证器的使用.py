from PyQt5.Qt import *


class AgeVadidator(QValidator):
    def validate(self, input_str, pos_int):
        print(input_str, pos_int)

        # 判定
        # 结果字符串, 应该全部都是由一些数字组成
        # return
        try:
            if 18 <= int(input_str) <= 180:
                return (QValidator.Acceptable, input_str, pos_int)
            elif 1 <= int(input_str) <= 17:
                return (QValidator.Intermediate, input_str, pos_int)
            else:
                return (QValidator.Invalid, input_str, pos_int)
        except:
            if len(input_str) == 0:
                return (QValidator.Intermediate, input_str, pos_int)
            return (QValidator.Invalid, input_str, pos_int)

    def fixup(self, p_str):
        print("xxx", p_str)
        try:
            if int(p_str) < 18:
                return "18"
            return "180"
        except:
            return "18"

class MyAgeVadidator(QIntValidator):
    def fixup(self, p_str):
        print("xxx", p_str)
        if len(p_str) == 0 or int(p_str) < 18:
        # if int(p_str) < 18 or len(p_str) == 0:
            return "18"

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEidt验证器的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        le = QLineEdit(self)
        le.move(100, 100)
        # 18 - 180
        # vadidator = AgeVadidator()
        # vadidator = QIntValidator(18, 180)
        vadidator = MyAgeVadidator(18, 180)
        le.setValidator(vadidator)


        le2 = QLineEdit(self)
        le2.move(200, 200)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())