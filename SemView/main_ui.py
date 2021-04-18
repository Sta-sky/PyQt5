from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QSplitter, QHBoxLayout, QWidget
from SemView.set_label import SetLabel
from SemView.set_table import SetTable
from SemView.set_text import SetText
from util.tools import set_font


class MyMainView(QWidget, SetTable, SetLabel, SetText):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("SetView")
		# 设置字体
		font = set_font()
		if font:
			self.setFont(font)
		self.setAutoFillBackground(False)
		self.setGeometry(QtCore.QRect(125, 125, 1700, 900))
		self.table_init()
		self.label_init()
		self.text_init()
		self.init_ui()
	
	def init_ui(self):
		"""
		初始化界面框
		"""
		self.table_view.setFrameShape(QFrame.StyledPanel)
		self.label_view.setFrameShape(QFrame.StyledPanel)
		self.text_view.setFrameShape(QFrame.StyledPanel)
		
		# 初始化横向布局管理器
		self.mainlayout = QHBoxLayout(self)
		
		# 将label 图片框加入spltter1  内部垂直
		splitter1 = QSplitter(Qt.Vertical)
		splitter1.addWidget(self.label_view)
		
		# splitter2 为内部垂直垂直
		splitter2 = QSplitter(Qt.Vertical)
		splitter2.addWidget(self.text_view)
		splitter2.addWidget(self.tab_bnt_sort)
		splitter2.addWidget(self.table_view)
		splitter2.addWidget(self.label_view_but)
		
		# splitter3 为内部水平，  将slitter1， splitter2 加入3中， 1，2构成水平排布方式，
		splitter3 = QSplitter(Qt.Horizontal)
		splitter3.addWidget(splitter1)
		splitter3.addWidget(splitter2)
		
		# 将spltter3 加入布局管理器中，
		self.mainlayout.addWidget(splitter3)
		# 将布局管理器加入 主界面中
		self.setLayout(self.mainlayout)
		



