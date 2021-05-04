from PyQt5.QtCore import QThread, pyqtSignal


class Example(QThread):
	signal = pyqtSignal()  # 括号里填写信号传递的参数
	
	def __init__(self):
		super().__init__()
	
	def __del__(self):
		self.wait()
	
	def run(self):
		# 进行任务操作
		self.signal.emit()  # 发射信号

