from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap


def handle_img(self, strimgs):
	try:
		img_obj = QPixmap(strimgs)
		img_obj = img_obj.scaledToWidth(640)
		img_obj = img_obj.scaledToHeight(500)
		self.label_view.setScaledContents(True)
		return img_obj
	except Exception as e:
		print(str(e))
		return False
	

def set_font():
	# 初始化一个label框
	try:
		font = QtGui.QFont()
		font.setFamily("微软雅黑")
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		return font
	except Exception as e:
		return False