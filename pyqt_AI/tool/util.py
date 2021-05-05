from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox


def echo(self, info):  # 消息：信息
	print(info)
	QMessageBox.information(self, "消息框标题", str(info), QMessageBox.Yes | QMessageBox.No)


def handle_img(self, strimgs):
	try:
		img_obj = QPixmap(strimgs)
		img_obj = img_obj.scaledToWidth(640)
		img_obj = img_obj.scaledToHeight(500)
		self.setScaledContents(True)
		return img_obj
	except Exception as e:
		print(str(e))
		return False

def handle_result(data):
	res_list = []
	data_val = data['result']
	data_val = data_val[:3]
	for info_dic in data_val:
		str_list = []
		model_data = " 命中分数：{} \n 识别结果：{} \n 关键字：{}\n\n\n\n"
		for val in info_dic.values():
			str_list.append(val)
		res = model_data.format(str(str_list[0]), str(str_list[1]), str(str_list[2]))
		res_list.append(res)
	return res_list


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