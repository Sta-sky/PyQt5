import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QProgressDialog, QProgressBar, QLabel

from ui.login_ui import LoginUI


class LoginPage(LoginUI):
	def __init__(self):
		super(LoginPage, self).__init__()
		self.setupUi(self)
		self.setWindowTitle('账号登录')
		self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(sys.executable)))
		# self.base_path = '.'
		self.qss_path = self.base_path + '\\static\\login.qss'
		with open(self.qss_path) as fp:
			data = fp.read()
			self.setStyleSheet(data)
	

class MyProgress(QProgressDialog):
	
	def __init__(self):
		super(MyProgress, self).__init__()
		self.setCancelButtonText(None)
		label = QLabel('邮件下载中....')
		label.setStyleSheet('margin-left:100px;font-size:20px;font-weight:900px;text-align:center; width:800px')
		self.setLabel(label)
		bar = QProgressBar(self)
		bar.setMinimumWidth(400)
		bar.setStyleSheet('height:30px; background-color:rgb(211, 211, 211); border-radius:10px; font-size:20px;')
		bar.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
		self.setBar(bar)
		self.setMinimum(0)
		self.setMinimumWidth(600)
		self.setMinimumHeight(140)
		self.setMaximum(100)
