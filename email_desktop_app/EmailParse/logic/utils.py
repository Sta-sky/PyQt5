# -*- coding: utf-8 -*-
import os
import re
from datetime import datetime

import numpy as np
import xlwt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from EmailParse.logic.log_util import Log

logger_obj = Log('tools')
logger = logger_obj.print_info()

class SalaryDatabase:
	
	def __init__(self, data_path):
		self.path = data_path
		self.dic_test = [{'name': '刘强海', 'salary': 1000}, {'name': '张三', 'salary': 1200}]
	
	def save_database(self, info_list):
		""" 保存数据 """
		try:
			np.save(self.path, info_list)
			return True
		except Exception as e:
			logger.error(str(e))
			return False
	
	def load_database(self):
		""" 读取数据 """
		try:
			data = np.load(self.path, allow_pickle=True)
			return data.tolist()
		except Exception as e:
			logger.error(str(e))
			return None
	
	def add_database(self, dict_info):
		""" 添加数据 """
		try:
			data_dict = self.load_database()
			if not data_dict:
				data_dict = []
			data_dict.append(dict_info)
			self.save_database(data_dict)
			return True
		except Exception as e:
			logger.error(str(e))
			return False
	
	def delete_database(self, del_name):
		try:
			data_list = self.load_database()
			for index, item in enumerate(data_list):
				if str(item.get('name')) == del_name:
					del data_list[index]
			self.save_database(data_list)
			return True
		except Exception as e:
			logger.error(str(e))
			return False
	
	def judge_data_exsit(self, name):
		try:
			if self.load_database():
				for item in self.load_database():
					if item.get('name') == name:
						return True
				return False
			else:
				return False
		except Exception as e:
			logger.error(str(e))
			return False
	
	def update_data(self, row, type, content):
		try:
			info_list = self.load_database()
			if not self.load_database():
				return False
			for index, item in enumerate(self.load_database()):
				if index == row:
					if type == 'name':
						info_list[row]['name'] = content
					elif type == 'salary':
						info_list[row]['salary'] = content
					elif type == 'level':
						info_list[row]['level'] = content
					elif type == 'sex':
						info_list[row]['sex'] = content
					else:
						pass
			self.save_database(info_list)
			return True
		except Exception as e:
			logger.error(str(e))
			return False
	
	def return_name_level(self, name):
		info_list = self.load_database()
		level, salary, sex = None, None, None
		for item in info_list:
			if item.get('name', None) == name:
				level = item.get('level', None)
				salary = item.get('salary', None)
				sex = item.get('sex', None)
		return level, salary, sex

	def return_name_city_salary(self, city):
		try:
			data_list = self.load_database()
			salary = None
			for item in data_list:
				if item.get('name', None) == city:
					salary = item.get('salary', None)
			return  salary
		except Exception as e:
			logger.error(str(e))
		
	def return_city_list(self):
		try:
			city_list = []
			for item in  self.load_database():
				for city in item.keys():
					city_list.append(city)
			return city_list
		except Exception as e:
			logger.error(str(e))

def waring_info(selfs, message):
	QMessageBox.warning(selfs, "错误提醒", message, QMessageBox.Yes)


def echo_info(selfs, message):
	QMessageBox.warning(selfs, "提示信息", message, QMessageBox.Yes)


def date_format(item, format_item):
	try:
		date = datetime.strptime(item, format_item)
		return date
	except Exception as e:
		return False


def init_table(selfs_employee_city, type, data):
	try:
		selfs_employee_city.clear()
		data_header_list = ['name', 'salary', 'level', 'sex']
		city_header_list = ['name', 'salary']
		if type == 'data':
			header_list = data_header_list
		else:
			header_list = city_header_list
		if data:
			selfs_employee_city.setRowCount(len(data))
			selfs_employee_city.setColumnCount(len(header_list))
			selfs_employee_city.setHorizontalHeaderLabels(header_list)
			
			for index, item in enumerate(data):
				first = QTableWidgetItem(str(item.get('name')))
				first.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
				second = QTableWidgetItem(str(item.get('salary')))
				second.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
				selfs_employee_city.setItem(index, 0, first)
				selfs_employee_city.setItem(index, 1, second)
				if type == 'data':
					third = QTableWidgetItem(str(item.get('level')))
					third.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
					selfs_employee_city.setItem(index, 2, third)
					four = QTableWidgetItem(str(item.get('sex')))
					four.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
					selfs_employee_city.setItem(index, 3, four)
		else:
			selfs_employee_city.setColumnCount(len(header_list))
			selfs_employee_city.setHorizontalHeaderLabels(header_list)
	except Exception as e:
		logger.error(str(e))

def add_info(selfs_employee_city, type, selfs, list_info):
	try:
		if list_info:
			echo_info(selfs, '请先完善提交当前修改')
			return
		row_count = selfs_employee_city.rowCount()
		if row_count != -1:
			selfs_employee_city.insertRow(row_count)
			selfs_employee_city.setItem(row_count, 0, QTableWidgetItem(' '))
			selfs_employee_city.setItem(row_count, 1, QTableWidgetItem(' '))
			selfs_employee_city.item(row_count, 0).setBackground(QBrush(QColor(238, 224, 229)))
			selfs_employee_city.item(row_count, 1).setBackground(QBrush(QColor(238, 224, 229)))
			if type == 'data':
				selfs_employee_city.setItem(row_count, 2, QTableWidgetItem(' '))
				selfs_employee_city.item(row_count, 2).setBackground(QBrush(QColor(238, 224, 229)))
				selfs_employee_city.setItem(row_count, 3, QTableWidgetItem(' '))
				selfs_employee_city.item(row_count, 3).setBackground(QBrush(QColor(238, 224, 229)))
			list_info.append(row_count)
	except Exception as e:
		logger.error(str(e))
		
def submit_info(selfs, selfs_employee_city, type):
	try:
		if type == 'city':
			info_list = selfs.new_add_city_list
			self_data = selfs.city_obj
		else:
			info_list = selfs.new_add_emp_list
			self_data = selfs.data_obj
		if not info_list:
			echo_info(selfs, '请先新增并编辑成员信息')
			return
		row = info_list[0]
		name = selfs_employee_city.item(row, 0).text().strip().replace(' ', '')
		salary = selfs_employee_city.item(row, 1).text().strip().replace(' ', '')
		if not name or not salary:
			echo_info(selfs, '请完善新增信息')
			return
		if self_data.judge_data_exsit(name):
			echo_info(selfs, f'{name} 已经存在， 请核对')
			return
		if type == 'employee':
			level = selfs_employee_city.item(row, 2).text().strip().replace(' ', '')
			sex = selfs_employee_city.item(row, 3).text().strip().replace(' ', '')
			if not level or not sex:
				echo_info(selfs, '请完善新增信息')
				return
			res = self_data.add_database({"name": name, 'salary': salary, 'level': level, 'sex': sex})
		else:
			res = self_data.add_database({"name": name, 'salary': salary})
		if not res:
			echo_info(selfs, f'新增 {name} 失败')
			return
		if type == 'city':
			selfs.init_city_data()
		else:
			selfs.init_employee_data()
		info_list.clear()
		echo_info(selfs, f'新增成功 {name} 成功', )
		selfs_employee_city.blockSignals(False)
	except Exception as e:
		logger.error(str(e))
	
def re_date_parse(content):
	try:
		pattern = re.compile(r'\d{4}/\d{1,2}/\d{1,2}|\d{4}\.\d{1,2}\.\d{1,2}|\d{4}年\d{1,2}月\d{1,2}日')  # 定义匹配模式
		pattern_data = re.findall(pattern, content)
		list_form = ['%Y/%m/%d', '%Y.%m.%d', '%Y-%m-%d', '%Y年%m月%d日']
		date = []
		for pattern_item in pattern_data:
			for item in list_form:
				result = date_format(pattern_item, item)
				if result:
					date.append(result.strftime("%Y-%m-%d"))
		return date
	except Exception as e:
		return ''

class SaveXlsx:
	
	def __init__(self, save_path):
		self.work = xlwt.Workbook(encoding='utf-8')
		self.file_save_path = save_path
	
	def add_sheet(self, sheet_name):
		self.sheet = self.work.add_sheet(sheet_name)
		return self.sheet
	
	def generate_excel_data(self, data, fields):
		"""
		传入一个如下格式的数据，
			data格式为data[
				[count, name,age],
				[count, name,age]
			]
			fields格式为：[序号，姓名，年龄]
		保存xml表格, 路径，文件名可自定义，
		:param data: 列表嵌套
		:param fields: 表头字段
		:return:
		"""
		try:
			self.sheet.write_merge(0, 1, 0, 8, '四川准达信息技术股份有限公司 (工时确认)',
			                       self.set_style(height=400, bg_color=55))
			pattern_top = xlwt.Pattern()
			pattern_top.pattern = xlwt.Pattern.SOLID_PATTERN
			pattern_top.pattern_fore_colour = 5
			for num in range(len(fields)):
				self.sheet.write(2, num, fields[num], self.set_style(height=300, bg_color=40))
			for row in range(3, len(data) + 3):
				for col in range(len(fields) - 1):
					lists_res = data[row - 3][col]
					if lists_res in ['星期六', '星期天']:
						self.sheet.write(row, len(fields) - 1, '加班', self.set_style(height=250, bg_color=5))
					self.sheet.write(row, col, lists_res, self.set_style(height=250))
			for col in range(len(fields)):
				self.set_cell_width(col, 256 * 20)
			self.set_cele_height(0, 20 * 40)
			self.set_cele_height(2, 20 * 40)
			for index in range(3, 500):
				self.set_cele_height(index, 20 * 30)
		except Exception as e:
			logger.error(str(e))
	
	def set_cell_width(self, col, width):
		""" 设置表格宽  width = 256 * 20    256为衡量单位，20表示20个字符宽度 """
		item_col = self.sheet.col(col)
		item_col.width = width
	
	def set_cele_height(self, row, height):
		self.sheet.row(row).height_mismatch = True
		self.sheet.row(row).height = height  # 20 * 40   20为基准数，40意为40磅
	
	def save_xlsx(self):
		if os.path.exists(self.file_save_path):
			os.remove(self.file_save_path)
		self.work.save(self.file_save_path)
	
	def set_style(self, font_name='楷体', height=200, color=0x7DDD, bg_color=None, blod=False):
		style = xlwt.XFStyle()
		font = xlwt.Font()
		font.bold = blod
		font.name = font_name
		font.height = height
		font.colour_index = color
		# 设置对其方式
		"""
			VERT_TOP = 0x00 上端对齐
			VERT_CENTER = 0x01 居中对齐(垂直方向上)
			VERT_BOTTOM = 0x02 低端对齐
			HORZ_LEFT = 0x01 左端对齐
			HORZ_CENTER = 0x02 居中对齐(水平方向上)
			HORZ_RIGHT = 0x03 右端对齐
		"""
		# 设置居中
		alignment = xlwt.Alignment()
		alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
		alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直方向
		# 设置背景色
		if bg_color:
			pattern_top = xlwt.Pattern()
			pattern_top.pattern = xlwt.Pattern.SOLID_PATTERN
			pattern_top.pattern_fore_colour = bg_color
			style.pattern = pattern_top
		
		style.font = font
		style.alignment = alignment
		return style
	
	def travel_sheet(self):
		self.travelsheet = self.add_sheet('差旅费用统计')
		self.travelsheet.write_merge(0, 0, 0, 20, '2021年   Q2   差旅报销明细汇总表', style=self.set_style(height=500))
		self.travelsheet.write_merge(1, 2, 0, 0, '序号', style=self.set_style(blod=True))
		self.travelsheet.write_merge(1, 2, 1, 1, '出差人', style=self.set_style(blod=True))
		self.travelsheet.write_merge(1, 2, 2, 2, '性别', style=self.set_style(blod=True))
		self.travelsheet.write_merge(1, 2, 3, 3, '职务级别', style=self.set_style(blod=True))
		
		self.travelsheet.write_merge(1, 1, 4, 7, '出发时间地点', style=self.set_style(blod=True))
		self.travelsheet.write(2, 4, '年', style=self.set_style(blod=True))
		self.travelsheet.write(2, 5, '月', style=self.set_style(blod=True))
		self.travelsheet.write(2, 6, '日', style=self.set_style(blod=True))
		self.travelsheet.write(2, 7, '地点', style=self.set_style(blod=True))
		self.travelsheet.write_merge(1, 1, 8, 11, '返回地点及时间', style=self.set_style(blod=True))
		self.travelsheet.write(2, 8, '年', style=self.set_style(blod=True))
		self.travelsheet.write(2, 9, '月', style=self.set_style(blod=True))
		self.travelsheet.write(2, 10, '日', style=self.set_style(blod=True))
		self.travelsheet.write(2, 11, '地点', style=self.set_style(blod=True))
		self.travelsheet.write_merge(1, 1, 12, 14, '交通', style=self.set_style(blod=True))
		self.travelsheet.write(2, 12, '车/船/飞机费', style=self.set_style(blod=True))
		self.travelsheet.write(2, 13, '交通工具', style=self.set_style(blod=True))
		self.travelsheet.write(2, 14, '交通工具等级标准', style=self.set_style(blod=True))
		
		self.travelsheet.write_merge(1, 1, 15, 17, '补贴', style=self.set_style(blod=True))
		self.travelsheet.write(2, 15, '出差天数', style=self.set_style(blod=True))
		self.travelsheet.write(2, 16, '补贴/天', style=self.set_style(blod=True))
		self.travelsheet.write(2, 17, '小计', style=self.set_style(blod=True))
		self.travelsheet.write_merge(1, 2, 18, 18, '合计', style=self.set_style(blod=True))
		self.travelsheet.write_merge(1, 2, 19, 19, '项目', style=self.set_style(blod=True))
		for index in range(21):
			self.set_cell_width(index, 256 * 10)
		self.set_cele_height(0, 20 * 60)
		self.set_cele_height(1, 20 * 40)
		self.set_cele_height(2, 20 * 40)
		self.set_cell_width(7, 256 * 30)
		self.set_cell_width(11, 256 * 30)
		self.set_cell_width(12, 256 * 15)
		self.set_cell_width(14, 256 * 25)
		self.set_cell_width(19, 256 * 40)
		for index in range(3, 500):
			self.set_cele_height(index, 20 * 30)
			
	def travel_write(self, travel_list, selfs):
		try:
			row_base = 2
			number = 0
			for item in travel_list:
				selfs.logger.info(f'出差_开始写入_{item}_信息')
				number += 1
				row_base += 1
				day = item[0]
				start_date = item[1].split('/')
				end_date = item[2].split('/')
				start_city = item[3]
				end_city = item[4]
				project = item[5]
				person = item[6]
				salary_total = None
				salary = None
				if day:
					day = int(day)
					for city in selfs.city_obj.return_city_list():
						if city in end_city:
							salary = selfs.city_obj.return_name_city_salary(city)
						else:
							salary = selfs.city_obj.return_name_city_salary('其他城市')
						salary_total = day * int(salary)
				level, sal, sex = selfs.data_obj.return_name_level(person)
				# 序号
				self.travelsheet.write(row_base, 0, number, style=self.set_style(blod=True))
				# 职级
				self.travelsheet.write(row_base, 3, level, style=self.set_style(blod=True))
				# 出工天数
				self.travelsheet.write(row_base, 15, day, style=self.set_style(blod=True))
				# 补贴薪资
				self.travelsheet.write(row_base, 16, salary, style=self.set_style(blod=True))
				# 补贴总数
				self.travelsheet.write(row_base, 17, salary_total, style=self.set_style(blod=True))
				# 开始日期
				self.travelsheet.write(row_base, 4, start_date[0], style=self.set_style(blod=True))
				self.travelsheet.write(row_base, 5, start_date[1], style=self.set_style(blod=True))
				self.travelsheet.write(row_base, 6, start_date[2], style=self.set_style(blod=True))
				# 结束日期
				self.travelsheet.write(row_base, 8, end_date[0], style=self.set_style(blod=True))
				self.travelsheet.write(row_base, 9, end_date[1], style=self.set_style(blod=True))
				self.travelsheet.write(row_base, 10, end_date[2], style=self.set_style(blod=True))
				# 出发城市
				self.travelsheet.write(row_base, 7, start_city, style=self.set_style(blod=True))

				# 到达城市
				self.travelsheet.write(row_base, 11, end_city, style=self.set_style(blod=True))
				# 人名
				self.travelsheet.write(row_base, 1, person, style=self.set_style(blod=True))
				# 性别
				self.travelsheet.write(row_base, 2, sex, style=self.set_style(blod=True))
				# 项目
				self.travelsheet.write(row_base, 19, project, style=self.set_style(blod=True))
				selfs.logger.info(f'_{item}_出差信息写入完成')
			selfs.logger.info(f'-所有-出差信息全部写入完成')
			return True
		except Exception as e:
			logger.error(str(e))
			return False
		
def get_week_day(date):
	
	week_day_dict = {
		0: '星期一',
		1: '星期二',
		2: '星期三',
		3: '星期四',
		4: '星期五',
		5: '星期六',
		6: '星期天',
	}
	day = date.weekday()
	return week_day_dict[day]


def handle_travel_content(content):
	try:
		day, start_date, end_date, start_city, end_city, person, \
		project = None, None, None, None, None, None, None
		data_list = []
		con_list = content.split('\n')
		con_list = [item for item in con_list if item.strip()]
		new_list = []
		flag = False
		for item in con_list:
			if '出差申请单' in item:
				flag = True
			if flag:
				if item:
					new_list.append(item)
		count = 0
		for item in new_list:
			result = re_date_parse(item)
			if len(result) >= 2:
				item_list = [i for i in item.split(' ') if i]
				start_date = item_list[0]
				end_date = item_list[1]
				start_city = item_list[2]
				end_city = item_list[3]
				day = item_list[4]
				project = item_list[5]
				if len(item_list) > 7:
					project = item_list[6]
			# if '出差天数' in item :
			# 	day = re.findall('\d+', item)
			if '申请人签字' in item:
				person_list = [i for i in item.strip().split(' ') if i]
				person = person_list[1].strip()
			count += 1
			data_list = [day, start_date, end_date, start_city, end_city, project, person]
		return data_list
	except Exception as e:
		logger.error(str(e))
		raise