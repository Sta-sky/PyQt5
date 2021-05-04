import os

from imageclassify import BaiduClient

def open_data(image_path):
	with open(image_path, 'rb', ) as fp:
		data = fp.read()
		return data
		

def get_baidu_image_data(image_path):
	clinet = BaiduClient().create_client()
	image_data = open_data(image_path)
	reduslt_data = clinet.advancedGeneral(image_data)
	return reduslt_data
		

def get_image_pat():
	path_root = None
	file_path = None
	base_path = os.path.abspath('./static')
	for i in os.walk(base_path):
		path_root = i[0]
		file_path = i[2]
	image_path_list = [f'{path_root}\\{i}' for i in file_path]
	if image_path_list:
		return image_path_list
	else:
		return []

