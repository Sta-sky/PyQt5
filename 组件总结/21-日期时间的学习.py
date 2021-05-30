from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("日期时间的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # dt = QDateTime(2018, 12, 12, 12, 30)
        # dt = QDateTime.currentDateTime()
        # # dt = dt.addYears(-2)
        # print(dt.offsetFromUtc() // 3600)
        # # print(dt)
        #
        # QDateTimeEdit(dt, self)
        # QDate
        # QTime
        time = QTime.currentTime()
        time.start()

        btn = QPushButton(self)
        btn.setText("测试")
        btn.move(200, 200)
        btn.clicked.connect(lambda :print(time.elapsed() / 1000))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())