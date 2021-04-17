import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush
from PyQt5.QtWidgets import QApplication, QTableWidget, QWidget, QTableWidgetItem, QComboBox, QHBoxLayout, QFrame
from PyQt5.QtWidgets import QSplitter


class MianWindow(QWidget):
    def __init__(self):
        super(MianWindow, self).__init__()
        self.resize(1250, 750)
        self.setWindowTitle('SEMview')
        self.init_window()

    def init_window(self):
        mainlayout = QHBoxLayout()
        right_top = QFrame()
        right_top.setFrameShape(QFrame.StyledPanel)

        right_botm = QFrame()
        right_botm.setFrameShape(QFrame.Box)

        left_box = QFrame()
        left_box.setFrameShape(QFrame.StyledPanel)
        left_box.setLineWidth(100)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(right_top)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(left_box)
        splitter2.addWidget(right_botm)

        splitter3 = QSplitter(Qt.Horizontal)
        splitter3.addWidget(splitter1)
        splitter3.addWidget(splitter2)

        mainlayout.addWidget(splitter3)
        self.setLayout(mainlayout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win_obj = MianWindow()
    win_obj.init_window()
    app.exec_()
