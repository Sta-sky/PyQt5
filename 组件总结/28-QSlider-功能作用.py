from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSlider的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        sd = QSlider(self)
        sd.move(200, 200)
        sd.resize(30, 200)
        sd.setTickPosition(QSlider.TicksBothSides)
        # sd.setPageStep(5)
        sd.setTickInterval(5)

        sd.valueChanged.connect(lambda val: print(val))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()
    
    
    sys.exit(app.exec_())