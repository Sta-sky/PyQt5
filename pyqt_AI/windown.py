import os
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTreeWidgetItem

from base import get_baidu_image_data
from main_ui import Ui_MainWindow
from qthread import Example
from tool.util import echo, handle_img, handle_result, set_font


class MianWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MianWindow, self).__init__()
		self.setupUi(self)
		self.base_path = ''
		self.setWindowTitle('图像识别工具')
		self.resize(1500, 800)
		self.insert_img.triggered.connect(self.handle_image_file)
		self.treeWidget.clicked.connect(self.handle_asycn_text)
		self.img_label.setPixmap(QPixmap('./tool/not_found.jpg'))
		
	def handle_image_file(self):
		try:
			result1 = QFileDialog.getOpenFileNames(self, '葵花宝典', 'D:/background/b_background', '图片(*.png *.jpg *.jfif)')
		except Exception as e:
			return None
		base_path = result1[0][0].split('/')
		img_list = result1[0]
		base_path.pop()
		for i in base_path:
			self.base_path += f'{i}/'
		root_file = QTreeWidgetItem(self.treeWidget)
		root_file.setText(0, self.base_path)
		for img in img_list:
			img = img.split('/')[-1]
			child = QTreeWidgetItem(root_file)
			child.setText(0, img)
		
		
	def handle_asycn_text(self):
		self.thread = Example()
		self.thread.signal.connect(self.handle_info)
		self.thread.start()
	
	def handle_info(self):
		res = self.treeWidget.selectedItems()[0]
		res = res.text(0)
		img_path = f'{self.base_path}/{res}'
		try:
			if os.path.exists(img_path):
				img_obj = handle_img(self.img_label, img_path)
				self.img_label.setPixmap(QPixmap(img_obj))
				data = get_baidu_image_data(img_path)
				res_data = handle_result(data)
				self.img_info.clear()
				for info in res_data:
					self.img_info.append(info)
					txt = self.img_info.toPlainText()
					txt.split('\n')
				font = set_font()
				print(font)
				self.img_info.setFont(font
				                      )
			else:
				echo(self, '没有文件目录')
		except Exception as e:
			echo(self, f'解析出错， 原因为{str(e)}')




if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainwin = MianWindow()
	mainwin.show()
	sys.exit(app.exec_())