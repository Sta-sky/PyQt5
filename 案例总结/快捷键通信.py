import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QShortcut, QLabel, QApplication, QHBoxLayout

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.label = QLabel("Try Ctrl+O, Shift+O", self)
        self.shortcut = QShortcut(QKeySequence("Ctrl+f"), self)
        self.shortcut = QShortcut(QKeySequence("Shift+O"), self)
        self.shortcut = QShortcut(QKeySequence("Alt+O"), self)
        self.shortcut.activated.connect(self.on_open)
        self.shortcut.activated.connect(self.on_open_shift)
        self.shortcut.activated.connect(self.on_open_alt)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)
        self.resize(150, 100)
        self.show()

    @pyqtSlot()
    def on_open(self):
        print("Opening!")

    @pyqtSlot()
    def on_open_shift(self):
        print("Opening shift!")

    @pyqtSlot()
    def on_open_alt(self):
        print("Opening Alt!")

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
