from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton(self)
        btn.setText("当前字体")
        btn.clicked.connect(lambda :print(cw.monthShown()))
        btn.clicked.connect(lambda :print(cw.yearShown()))
        def test():
            cw.setSelectedDate(QDate(2019, 12, 12))
            cw.showSelectedDate()

        btn.clicked.connect(test)


        cw = QCalendarWidget(self)

        cw.setDateEditEnabled(True)
        cw.setDateEditAcceptDelay(3000)
        # cw.setNavigationBarVisible(False)
        cw.move(100, 100)
        tf = QTextCharFormat()
        tf.setFontFamily("幼圆")
        tf.setToolTip("今天是我们恋爱的日子")
        tf.setFontOverline(True)


    def selectFont(self, *args):
        print("xxx", args)
        # print(self.d.currentFont())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())

