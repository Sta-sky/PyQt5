from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QTextEdit, QPushButton


class SetText:
    def text_init(self):
        self.text_view = QLabel()
        self.text_edit = QTextEdit(self)
        self.text_boxloyout = QVBoxLayout()
        self.text_boxloyout.addWidget(self.text_edit)
        self.text_view.setLayout(self.text_boxloyout)
        self.text_view.setGeometry(QtCore.QRect(0, 0, 0, 200))

