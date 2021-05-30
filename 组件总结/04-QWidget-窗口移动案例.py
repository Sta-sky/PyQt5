from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("窗口移动的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()
    
    
    sys.exit(app.exec_())