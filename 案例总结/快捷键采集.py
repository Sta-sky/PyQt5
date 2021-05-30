from PyQt5.Qt import *  # 刚开始学习可以这样一下导入
import sys

"""
创建QKeySequenceEdit 控件来采集快捷键#   转化为可读字符串 以及统计  快捷键个数
"""


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QKeySequenceEdit 控件的学习")
        self.resize(400, 400)

        # 创建QKeySequenceEdit 控件来采集快捷键
        self.keySequenceEdit = QKeySequenceEdit(self)
        keySequence = QKeySequence("Ctrl+C")
        self.keySequenceEdit.setKeySequence(keySequence)
        # 获取QKeySequenceEdit 中的快捷键###############################
        btn = QPushButton(self)
        btn.setText("按钮")
        btn.move(0, 300)

        btn.clicked.connect(self.handle)

    def handle(self):
        # 转化为可读字符串 以及统计  快捷键个数  ##
        res = self.keySequenceEdit.keySequence().toString()
        count = self.keySequenceEdit.keySequence().count()
        if count > 1:
            print('error')
            return
        else:
            print(res, count)

        # 清除
        self.keySequenceEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
