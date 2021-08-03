# -*- coding: utf-8 -*-
import datetime
import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QKeySequence, QIcon
from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem, QMessageBox, QFileDialog, QProgressBar, QProgressDialog

from .SubPage import LoginPage, MyProgress
from .email_pop import create_connect, get_email, handle_email
from .log_util import Log
from .utils import echo_info, SalaryDatabase, init_table, add_info, \
	submit_info, get_week_day, SaveXlsx, handle_travel_content
from EmailParse.ui.main_ui import Ui_MainWindow


class EmailWindown(Ui_MainWindow, QMainWindow):
	
	def __init__(self):
		super(EmailWindown, self).__init__()
		self.setupUi(self)
		logger_obj = Log('desktop_app')
		self.logger = logger_obj.print_info()
		self.setContentsMargins(0, 0, 0, 0)
		self.init_ver() # 变量初始化
		self.main_style() # 主页样式加载
		self.primery_page_btn() # 主页面 按钮 事件
		self.sub_page_btn() # 子页面按钮 事件
		self.init_city_data() # 初始化城市界面信息
		self.init_comb_info() # 初始化时间过滤组件
		self.init_employee_data() # 初始化人员界面信息

	def main_style(self):
		self.resize(1700, 850)
		self.setWindowTitle('邮件解析应用')
		self.logger.info(self.base_path + '\\static\\style.qss')
		with open(self.base_path + '\\static\\style.qss') as fp:
			data = fp.read()
			self.setStyleSheet(data)
		self.setWindowIcon(QIcon(self.base_path + '\\static\\image\\win.ico'))
		palette = QPalette()
		palette.setBrush(QPalette.Background, QBrush(QPixmap(self.base_path + "\\static\\image\\background.png")))
		self.setPalette(palette)
		self.login_ui = LoginPage()
		self.login_ui.setModal(True)
		
	def init_ver(self):
		self.email_data = None
		self.x_pos = None
		self.y_pos = None
		self.move_flag = False
		# self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(sys.executable)))
		self.base_path = '.'
		self.database_path = self.base_path + '\\static\\database.npy'
		self.city_path = self.base_path + '\\static\\city_database.npy'
		self.data_obj = SalaryDatabase(self.database_path)
		self.city_obj = SalaryDatabase(self.city_path)
		self.email_obj = None
		self.new_add_emp_list = []
		self.new_add_city_list = []
		self.data_list = []
		self.data_fields = ['日期', '星期', '岗位', '岗位单价', '工时(人/天)', '项目编号', '项目名称', '姓名', '加班备注']
		self.data_set = set()
		self.email_data = {}

	
	def init_employee_data(self):
		""" 初始化成员数据 """
		self.table_employee.blockSignals(True)
		data_ = self.data_obj.load_database()
		init_table(self.table_employee, type='data', data=data_)
		self.table_employee.blockSignals(False)


	def init_city_data(self):
		""" 初始化城市数据 """
		self.table_city.blockSignals(True)
		data_ = self.city_obj.load_database()
		init_table(self.table_city, type='city', data=data_)
		self.table_city.blockSignals(False)

	def init_comb_info(self):
		for num in range(1, 13):
			num = str(num)
			if len(num) == 1:
				num = '0' + num
			self.com_month.addItem(num)
		month = datetime.datetime.now().month
		month = str(month)
		if len(month) == 1:
			month = '0' + month
		self.com_month.setCurrentText(month)
		for num in range(0, 5):
			current_year = datetime.datetime.now().year
			year = current_year - num
			self.com_year.addItem(str(year))
		
	def primery_page_btn(self):
		self.outlogin.setShortcut(QKeySequence('Ctrl+r'))
		self.btn_export_excel.triggered.connect(self.export_excel)      # 导出表格
		self.outlogin.triggered.connect(lambda : self.close())          # 关闭窗口
		self.login.triggered.connect(self.login_in)                     # 登录菜单
		self.btn_down_email.triggered.connect(self.get_email_data)      # 下载邮件
		self.treeWidget.clicked.connect(self.handle_email_tree_item)    # 处理邮件树
		self.add_city.clicked.connect(self.add_city_info)               # 添加城市
		self.add_employee.clicked.connect(self.add_employee_info)       # 添加人员
		self.del_employee.clicked.connect(self.del_employee_info)       # 删除人员
		self.del_city.clicked.connect(self.del_city_info)               # 删除城市
		self.submit_city.clicked.connect(self.submit_city_info)         # 提交城市修改
		self.submit_employee.clicked.connect(self.submit_employee_info) # 提交人员修改
		self.cacell_employee.clicked.connect(self.cacell_employee_info) # 取消人员新增
		self.cancell_city.clicked.connect(self.cancell_city_info)       # 取消城市新增
		self.table_city.cellChanged.connect(self.update_city)           # 修改城市数据
		self.table_employee.cellChanged.connect(self.update_employee)   # 修改成员数据
		
	
	def export_excel(self):
		""" 导出表格 """
		try:
			if self.email_data.get('email_info'):
				self.data_list = []
				savefile_dialog = QFileDialog()
				path_file, ok = savefile_dialog.getSaveFileName(
					self, "文件保存", "C:/", "Files (*.xlsx *.csv *.xls, *.xml)")
				if path_file:
					excel_obj = SaveXlsx(path_file)
					# 生成日报sheet页数据
					self.logger.info('日报--开始生成_日报_sheet页')
					self.day_content_handle()
					self.extract_name_to_set()
					self.logger.info(f'日报--日报费用统计人员为：{self.data_set}')
					failed_list = []
					for name_item in self.data_set:
						if not self.generate_list(name_item):
							self.logger.error(f'日报--生成_{name_item}_日报sheet页失败')
							failed_list.append(name_item)
							continue
						self.logger.info(f'日报--开始写入_{name_item}_sheet页面信息')
						excel_obj.add_sheet(f'工时费用统计({name_item})')
						excel_obj.generate_excel_data(self.every_name_list, self.data_fields)
						self.logger.info(f'日报--{name_item}_sheet页面信息写入完成')
					self.logger.info(f'日报--日报写入失败的人员{failed_list}')
					self.logger.info(f'所有日报--sheet页面信息写入完成')
					# 生成旅行sheet页数据
					self.logger.info('出差--开始生成_出差_sheet页')
					self.travel_data_handle()
					excel_obj.travel_sheet()
					if not excel_obj.travel_write(self.cell_travel_all_list, self):
						echo_info(self, '旅行费用导出失败')
						self.logger.error('旅行费用导出失败')
					# 保存excel
					self.logger.info('出差--出差sheet页 完成')
					excel_obj.save_xlsx()
					echo_info(self, f'保存文件 【 {os.path.basename(path_file)} 】 成功')
					self.logger.info( f'保存文件 【 {os.path.basename(path_file)} 】 成功')
			else:
				echo_info(self, '邮件数据为空, 请先下载邮件')
				return
		except Exception as e:
			self.logger.error(str(e))
			return
	
	def parse_content(self, item_info):
		""" 解析 内容 生成表格 需要的列表格式"""
		try:
			content = item_info['content']
			word_list = [item.strip() for item in content.split(' ') if item]
			word_list = [item for item in word_list if item]
			if not word_list:
				return
			info_dic = {}
			length_list = len(word_list)
			for index, val in enumerate(word_list):
				if index % 2 == 0 and index < length_list - 1:
					info_dic[word_list[index]] = word_list[index + 1]
			self.data_list.append(info_dic)
		except Exception as e:
			self.logger.error(f'解析出差内容成为列表失败, 失败原因：{str(e)}')
			raise
	
	def extract_name_to_set(self):
		for item in self.data_list:
			name = item.get('申请人', None)
			if not name:
				continue
			self.data_set.add(name.strip())
			
	def generate_list(self, name_item):
		try:
			self.every_name_list = []
			for item in self.data_list:
				name = item.get('申请人', None)
				if name == name_item:
					date = item.get('日期', None)
					weekday = None
					if date:
						date_list = [int(i) for i in date.split('/')]
						weekday = get_week_day(datetime.date(date_list[0], date_list[1], date_list[2]))
					level, salary, sex = self.data_obj.return_name_level(name_item)
					if not level or not salary:
						echo_info(self, f'请添加 {name_item} 的 成员数据， 添加后再次导出')
						return False
					_list = [date, weekday, level, salary, item.get('工时周期', None),
					         item.get('项目编号', None), item.get('项目名称', None), item.get('申请人', None)]
					self.every_name_list.append(_list)
			return True
		except Exception as e:
			self.logger.error(str(e))
			return False
			
	def login_in(self):
		self.login_ui.show()
		self.login_ui.line_account.setText('liguiyang@zhunda.com')
		self.login_ui.line_password.setText('zhunda2021')
		
	def sub_page_btn(self):
		self.login_ui.btn_login.clicked.connect(self.handle_login)
		self.email_data.clear()
	
	def handle_email_tree_item(self):
		try:
			subject = self.treeWidget.selectedItems()[0].text(0)
			if subject in ['出差', '加班', '日报']:
				return
			for item in self.email_data['email_info']:
				if item['subject'] == subject:
					content = item['content']
					self.line_subject_mail.setText(item['subject'])
					self.line_send_mail.setText(item['from_user'])
					self.text_content_mail.setText(content)
		except Exception as e:
			self.logger.error(str(e))
			return
	
	def submit_city_info(self):
		try:
			submit_info(
				self,
				self.table_city,
				type='city'
			)
		except Exception as e:
			self.logger.error(str(e))
			
	def submit_employee_info(self):
		try:
			submit_info(
				self,
				self.table_employee,
				type='employee'
			)
		except Exception as e:
			self.logger.error(str(e))
			
	def add_city_info(self):
		try:
			self.table_city.blockSignals(True)
			add_info(self.table_city, 'city', self, self.new_add_city_list)
		except Exception as e:
			self.logger.error(str(e))
			return

	def add_employee_info(self):
		try:
			self.table_employee.blockSignals(True)
			add_info(self.table_employee, 'data', self, self.new_add_emp_list)
		except Exception as e:
			self.logger.error(str(e))
			return
		
	def update_city(self, row, col):
		content = self.table_city.item(row, col).text()
		city = self.table_city.item(row, 0).text()
		if col == 0:
			type = 'name'
		elif col == 1:
			type = 'salary'
		else:
			type = None
		self.city_obj.update_data(row, type, content)
		echo_info(self, f'修改 {city} -- {type} --> {content} 成功')
	
	def update_employee(self, row, col):
		content = self.table_employee.item(row, col).text()
		employee = self.table_employee.item(row, 0).text()
		if col == 0:
			type = 'name'
		elif col == 1:
			type = 'salary'
		elif col == 2:
			type = 'level'
		elif col == 3:
			type = 'sex'
		else:
			type = None
		self.data_obj.update_data(row, type, content)
		echo_info(self, f'修改 {employee} --> {type} 成功')
	
	def del_city_info(self):
		if self.new_add_city_list:
			echo_info(self, '请先完善提交当前修改')
			return
		current_item = self.table_city.currentItem()
		if current_item:
			if self.table_city.currentColumn() != 0:
				echo_info(self, '请选中要删除的 name 行，或者整行选中')
				return
			name = current_item.text()
			message = QMessageBox.question(self, '删除警告', f'确定要删除 {name} 信息？', QMessageBox.Yes | QMessageBox.No)
			if message == 16384:
				self.city_obj.delete_database(name)
				self.init_city_data()
		else:
			echo_info(self, '请选中要删除的行')
			
	def del_employee_info(self):
		if self.new_add_emp_list:
			echo_info(self, '请先完善提交当前修改')
			return
		currnt_item = self.table_employee.currentItem()
		if currnt_item:
			if self.table_employee.currentColumn() != 0:
				echo_info(self, '请选中要删除的 name 行，或者整行选中')
				return
			name = currnt_item.text()
			message = QMessageBox.question(self, '删除警告', f'确定要删除 {name} 信息？', QMessageBox.Yes | QMessageBox.No)
			if message == 16384:
				self.data_obj.delete_database(name)
				self.init_employee_data()
		else:
			echo_info(self, '请选中要删除的行')
			
	def cacell_employee_info(self):
		if not self.new_add_emp_list:
			echo_info(self, '无修改')
			return
		self.table_employee.removeRow(self.new_add_emp_list[0])
		self.new_add_emp_list.clear()
	
	def cancell_city_info(self):
		if not self.new_add_city_list:
			echo_info(self, '无修改')
			return
		self.table_city.removeRow(self.new_add_city_list[0])
		self.new_add_city_list.clear()
		
	def handle_login(self):
		account = self.login_ui.line_account.text()
		password = self.login_ui.line_password.text()
		self.email_obj = create_connect(account, password, self)
		if self.email_obj:
			self.logger.info(f'用户：{account}，登录成功')
			echo_info(self, '登录成功')
			self.login_ui.close()
			
	def get_email_data(self):
		try:
			self.progress = MyProgress()
			self.progress.open()
			if self.email_obj:
				email_num, email_obj = get_email(self.email_obj)
				self.logger.info(f'获取邮件数量为{email_num}')
				self.progress.setValue(20)
				if email_num:
					self.month = self.com_month.currentText()
					self.year = self.com_year.currentText()
					year_month = f'{self.year}:{self.month}'
					self.email_data = handle_email(email_num, email_obj, year_month, self.progress)
					self.logger.info(f'获取邮件信息完成')
					self.progress.setValue(90)
					self.progress.setValue(100)
					if not self.email_data.get('email_info'):
						echo_info(self, f'[ {self.month} ]月的邮件数量为 0 ')
						return
					if not self.email_data:
						self.logger.error('邮件下载处理异常')
						echo_info(self, '邮件下载处理异常')
					self.parse_email(self.email_data)
					self.logger.info('邮件树解析完成')
					self.logger.info('邮件下载完成')
					
				else:
					echo_info(self, '邮件总数量为 0')
			else:
				echo_info(self, '请先登录邮箱')
		except Exception as e:
			if 'sendall' in str(e):
				self.progress.close()
				echo_info(self, '请点击登录')
		finally:
			self.progress.close()
			return
	
	def parse_email(self, info_dic):
		try:
			if self.add_tree_item(info_dic.get('email_info')):
				echo_info(self, '邮件下载成功')
		except Exception as e:
			self.logger.error(str(e))
		
	def add_tree_item(self, info_dic):
		try:
			self.treeWidget.clear()
			travel_item = QTreeWidgetItem(self.treeWidget)
			travel_item.setText(0, '出差')
			over_time_item = QTreeWidgetItem(self.treeWidget)
			over_time_item.setText(0, '加班')
			daily_paper_item = QTreeWidgetItem(self.treeWidget)
			daily_paper_item.setText(0, '日报')
			other_item = QTreeWidgetItem(self.treeWidget)
			other_item.setText(0, '其他')
			for item in  info_dic:
				subject = item['subject']
				if '出差' in subject:
					travel_child = QTreeWidgetItem(travel_item)
					travel_child.setText(0, subject)
				elif '加班' in subject:
					over_time_child = QTreeWidgetItem(over_time_item)
					over_time_child.setText(0, subject)
				elif '日报' in subject:
					daily_paper_child = QTreeWidgetItem(daily_paper_item)
					daily_paper_child.setText(0, subject)
				else:
					other_item_child = QTreeWidgetItem(other_item)
					other_item_child.setText(0, subject)
			return True
		except Exception as e:
			echo_info(self, '生成邮件类别树失败')
			return False
			
	def travel_data_handle(self):
		try:
			self.cell_travel_all_list = []
			data_list = self.email_data.get('email_info', None)
			if not data_list:
				return
			self.travel_list = []
			for item in data_list:
				if '出差' in item['subject']:
					self.travel_list.append(item)
			for item_dic in self.travel_list:
				result = handle_travel_content(item_dic['content'])
				if not result:
					echo_info(self, '解析出差失败')
					return
				self.cell_travel_all_list.append(list(result))
		except Exception as e:
			self.logger.error(f'出差数据解析失败, 失败原因: {str(e)}')
			
	def day_content_handle(self):
		email_info_list = self.email_data['email_info']
		if not email_info_list:
			self.data_list = []
		for item_info in email_info_list:
			if '日报' in item_info['subject']:
				self.parse_content(item_info)
	
	def email_login(self):
		pass
	
	def closeEvent(self, event):
		reply = QMessageBox.question(self, '提示', '你确认要退出吗？', QMessageBox.Yes, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
			self.login_ui.close()
		else:
			event.ignore()
	
	def mousePressEvent(self, event):
		try:
			if event.button() == Qt.LeftButton:
				self.move_flag = True
				self.x_pos = event.x()
				self.y_pos = event.y()
		except Exception as e:
			self.logger.error(str(e))
		
	def mouseMoveEvent(self, event):
		try:
			if self.move_flag:
				pos_x = event.globalPos().x() - self.x_pos + 5
				pos_y = event.globalPos().y() - self.y_pos - 5
				self.move(pos_x, pos_y)
		except Exception as e:
			self.logger.error(str(e))
			pass
		
	def resizeEvent(self, event):
		pass
	
