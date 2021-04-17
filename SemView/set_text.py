from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QTextEdit, QPushButton


class SetText:
    def text_init(self):
        self.text_view = QLabel()
        self.text_edit = QTextEdit(self)
        self.text_click1 = QPushButton("显示文本")
        self.text_click2 = QPushButton("显示HTML")
        self.text_boxloyout = QVBoxLayout()
        self.text_boxloyout.addWidget(self.text_edit)
        self.text_boxloyout.addWidget(self.text_click1)
        self.text_boxloyout.addWidget(self.text_click2)
        self.text_view.setLayout(self.text_boxloyout)
        
        self.text_view.setGeometry(QtCore.QRect(0, 0, 0, 200))

        self.text_click1.clicked.connect(self.text_Click_event1)
        self.text_click2.clicked.connect(self.text_Click_event2)

    def text_Click_event1(self, info):
        self.text_edit.setPlainText(f"{info}\nHello PyQt5!\n点击按钮")

    def text_Click_event2(self, info):
        info = f"""
            <font color='red' size='3'><red>{info}\nHello PyQt5!\n。</font>
        """
        self.text_edit.setHtml(info)
