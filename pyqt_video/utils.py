from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox


def set_font(bold=False, italic=False, weight=50):
	# 初始化一个label框
	try:
		font = QtGui.QFont()
		font.setFamily("微软雅黑")
		font.setPointSize(12)
		font.setBold(bold)
		font.setItalic(italic)
		font.setWeight(weight)
		return font
	except Exception as e:
		return False
	
def echo(self, info):  # 消息：信息
	print(info)
	QMessageBox.information(self, "消息框标题", str(info), QMessageBox.Yes | QMessageBox.No)

