import random

import pandas as pd

col_list = ['分类', '工号', '姓名', '年龄', '性别', '职称']
row_list = ['Mask1', 'Mask2', 'Mask3', 'Mask4', 'Mask5', 'Mask6', 'Mask7', 'Mask8', 'Mask9', 'Mask10']
data = {}
type_list = []
num_list = []
name_list = []
age_list = []
sex_list = []
nike_list = []

for i in range(len(row_list)):
	for j in range(len(col_list)):
		if j == 4:
			continue
			
		if j == 0:
			print(i)
			random_num = row_list[i]
		data = {
			"type": type_list.append(random.randint(1, 10000)),
			"num": num_list.append(random.randint(1, 10000)),
			"name": name_list.append(random.randint(1, 10000)),
			"age": age_list.append(random.randint(1, 10000)),
			"sex": sex_list.append(random.randint(1, 10000)),
			"nike": nike_list.append(random.randint(1, 10000)),
			
		}
print(data)