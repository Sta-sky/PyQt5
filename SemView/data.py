import random
import pandas as pd

from PyQt5.QtWidgets import QTableWidgetItem

col_list = ['分类', '工号', '姓名', '年龄', '性别', '职称']
row_list = ['Mask1', 'Mask2', 'Mask3', 'Mask4', 'Mask5', 'Mask6', 'Mask7', 'Mask8', 'Mask9', 'Mask10']
row_num_list = []
for num in range(len(row_list)):
	row_num_list.append(str(num))

data = {}
type_list = []
num_list = []
name_list = []
age_list = []
sex_list = []
nike_list = []


def table_data(selfs):
	print(selfs)
	for i in range(len(row_list)):
		for j in range(len(col_list)):
			if j == 4:
				continue
			random_num = random.randint(1, 10000)
			if j == 0:
				print(i)
				random_num = row_list[i]
			data = {
				"type": type_list.append(random.randint(1, 10000)),
				"num": type_list.append(random.randint(1, 10000)),
				"name": type_list.append(random.randint(1, 10000)),
				"age": type_list.append(random.randint(1, 10000)),
				"sex": type_list.append(random.randint(1, 10000)),
				"nike": type_list.append(random.randint(1, 10000)),
				
			}
			selfs.setItem(i, j, QTableWidgetItem(str(random_num)))
