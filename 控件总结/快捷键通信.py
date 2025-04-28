import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QShortcut, QLabel, QApplication, QHBoxLayout


import sys
from PyQt5.QtWidgets import QWidget, QShortcut, QLabel, QApplication, QHBoxLayout
from functools import partial


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 初始化界面
        self.label = QLabel("Try Ctrl+F, Shift+O", self)
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.label)

        # 设置快捷键
        self._setup_shortcuts()

        self.resize(300, 200)
        self.show()

    def _setup_shortcuts(self):
        # Ctrl+F 快捷键
        self.shortcut_ctrl = QShortcut(QKeySequence("Ctrl+F"), self)
        self.shortcut_ctrl.activated.connect(partial(self.on_open, "Ctrl+F"))

        # Shift+O 快捷键
        self.shortcut_shift = QShortcut(QKeySequence("Shift+O"), self)
        self.shortcut_shift.activated.connect(partial(self.on_open, "Shift+O"))

        # Alt+O 快捷键
        self.shortcut_alt = QShortcut(QKeySequence("Alt+O"), self)
        self.shortcut_alt.activated.connect(partial(self.on_open, "Alt+O"))

    def on_open(self, key):
        print(f"{key} Triggered!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())