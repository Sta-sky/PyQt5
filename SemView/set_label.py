from PyQt5.QtWidgets import QLabel
from util.tools import set_font

class SetLabel:
    def label_init(self):
        self.label_view = QLabel()
        font = set_font()
        if font:
            self.label_view.setFont(font)
        self.label_view.setText("请点击表格查看详细数据")
