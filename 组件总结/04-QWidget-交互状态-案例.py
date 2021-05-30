from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("交互状态案例的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 添加三个子控件
        label = QLabel(self)
        label.setText("标签")
        label.move(100, 50)
        label.hide()

        le = QLineEdit(self)
        # le.setText("文本框")
        le.move(100, 100)

        btn = QPushButton(self)
        btn.setText("登录")
        btn.move(100, 150)
        btn.setEnabled(False)

        def text_cao(text):
            print("文本内容发生了改变", text)
            # if len(text) > 0:
            #     btn.setEnabled(True)
            # else:
            #     btn.setEnabled(False)
            btn.setEnabled(len(text) > 0)
        le.textChanged.connect(text_cao)

        def check():
            # print("按钮被点击了")
            # 1. 获取文本框内容
            content = le.text()
            # 2. 判定是否是Sz
            if content == "Sz":
                # 3. 是 -> 显示之前隐藏的提示标签, 展示文本
                label.setText("登录成功")
            else:
                label.setText("登录失败")

            label.show()
            label.adjustSize()

        btn.pressed.connect(check)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())