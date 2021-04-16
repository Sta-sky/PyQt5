from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QTextEdit, QPushButton


class SetText:
    def text_init(self, Baseform):
        self.text_label = QLabel(Baseform)
        self.text_label.setGeometry(QtCore.QRect(800, 150, 450, 250))
        self.textedit = QTextEdit()
        self.text_click1 = QPushButton("显示文本")
        self.text_click2 = QPushButton("显示HTML")
        self.lable = QVBoxLayout()
        self.lable.addWidget(self.textedit)
        self.lable.addWidget(self.text_click1)
        self.lable.addWidget(self.text_click2)
        self.text_label.setLayout(self.lable)

        self.text_click1.clicked.connect(self.text_Click_event1)
        self.text_click2.clicked.connect(self.text_Click_event2)

    def text_Click_event1(self, info):
        self.textedit.setPlainText(f"{info}\nHello PyQt5!\n点击按钮")

    def text_Click_event2(self, info):
        info = f"""
            <font color='red' size='3'><red>{info}\nHello PyQt5!\n。</font>
        """
        self.textedit.setHtml(info)
