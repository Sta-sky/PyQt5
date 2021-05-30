from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QKeySequenceEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        kse = QKeySequenceEdit(self)
        # ks = QKeySequence("Ctrl+C")
        # ks = QKeySequence(QKeySequence.Copy)
        ks = QKeySequence(Qt.CTRL + Qt.Key_C, Qt.CTRL + Qt.Key_A)
        kse.setKeySequence(ks)
        kse.clear()

        btn = QPushButton(self)
        btn.move(100, 100)
        btn.setText("测试按钮")
        btn.clicked.connect(lambda :print(kse.keySequence().toString(), kse.keySequence().count()))

        kse.editingFinished.connect(lambda :print("结束编辑"))
        kse.keySequenceChanged.connect(lambda key_val:print("键位序列发生改变", key_val.toString()))
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())