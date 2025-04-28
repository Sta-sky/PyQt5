import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QShortcut, QLabel, QApplication, QHBoxLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 初始化界面
        self.label = QLabel("Try Ctrl+O, Shift+O", self)
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.label)

        # 设置快捷键
        self._setup_shortcuts()

        self.resize(300, 200)
        self.show()

    def _setup_shortcuts(self):
        # Ctrl+F 快捷键
        self.shortcut_ctrl = QShortcut(QKeySequence("Ctrl+F"), self)
        self.shortcut_ctrl.activated.connect(self.on_open)

        # Shift+O 快捷键
        self.shortcut_shift = QShortcut(QKeySequence("Shift+O"), self)
        self.shortcut_shift.activated.connect(self.on_open_shift)

        # Alt+O 快捷键
        self.shortcut_alt = QShortcut(QKeySequence("Alt+O"), self)
        self.shortcut_alt.activated.connect(self.on_open_alt)

    @pyqtSlot()
    def on_open(self):
        print("Ctrl+F Triggered!")

    @pyqtSlot()
    def on_open_shift(self):
        print("Shift+O Triggered!")

    @pyqtSlot()
    def on_open_alt(self):
        print("Alt+O Triggered!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())