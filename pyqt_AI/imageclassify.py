from aip import AipImageClassify


class BaiduClient:
	def __init__(self):
		self.APP_ID = '24106734'
		self.API_KEY = '07M2F8BiHMCmkspClnXUeIGA'
		self.SECRET_KEY = 'XDbzzllDmMrV6dy25KXU5SE12cGi8tN8'
		
	def create_client(self):
		return AipImageClassify(self.APP_ID, self.API_KEY, self.SECRET_KEY)