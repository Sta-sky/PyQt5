# -*- coding: utf-8 -*-
import poplib
import socket
import time
from email.header import decode_header
from email.parser import Parser
from email.utils import parseaddr, parsedate_tz
from PyQt5.QtWidgets import QMessageBox

from logic.log_util import Log

logger_obj = Log('email')
logger = logger_obj.print_info()

month_dic = {
	'Jan': '01',
	'Feb': '02',
	'Mar': '03',
	'Apr': '04',
	'May': '05',
	'Jun': '06',
	'Jul': '07',
	'Aug': '08',
	'Sep': '09',
	'Oct': 10,
	'Nov': 11,
	'Dec': 12,
}


def create_connect(username, password, selfs, host: str = 'zhunda.com'):
	try:
		email = poplib.POP3(host)  # 创建一个pop3对象，这个时候实际上已经连接上服务器了
		email.set_debuglevel(1)  # 设置调试模式，可以看到与服务器的交互信息
		email.user(username)  # 向服务器发送用户名 密码
		email.pass_(password)
		return email
	except Exception as e:
		if issubclass(poplib.error_proto, type(e)):
			QMessageBox.warning(selfs, "错误提醒", "用户名密码错误。", QMessageBox.Yes)
			return None
		elif issubclass(socket.gaierror, type(e)):
			QMessageBox.warning(selfs, "错误提醒", "网络连接失败, 请检查网络", QMessageBox.Yes)
			return None


def get_email(email_obj):
	""" 返回服务器邮件数量 """
	server_email_obj = email_obj.stat()  # 获取服务器上信件信息，返回是一个列表，第一项是一共有多上封邮件，第二项是共有多少字节
	email_total_num = server_email_obj[0]  # 邮件总数
	return email_total_num, email_obj


def handle_email(email_total_num, email_obj, year_month, progress):
	try:
		email_count = 0
		email_list = []
		for i in range(email_total_num):
			curr_val = float('%.2f' % ((i / email_total_num) * 100))
			progress.setValue(curr_val)
			email_dic = {}
			email_count += 1
			resp, mailContent, bytes_size = email_obj.retr(i + 1)  # 信件id是从1开始的。
			if '+OK' not in resp.decode().split(' '):
				logger.warning('当前信 状态异常 跳过')
				continue
			msg_content = Parser().parsestr(b'\r\n'.join(mailContent).decode('utf-8'))
			send_date = parsedate_tz(msg_content.get('Date'))
			send_date = format_date(send_date)
			if year_month not in send_date:
				continue
			subject = decode_str(msg_content.get('Subject'))
			from_user = parseaddr(msg_content.get('From'))[1]
			to_user = parseaddr(msg_content.get('To'))[1]
			# 解析邮件内容
			def get_body(msg_content, key_coding):
				if msg_content.is_multipart():
					body = get_body(msg_content.get_payload(0), key_coding=key_coding)
				else:
					body = str(msg_content.get_payload(decode=True), key_coding, errors='ignore')
				return body
			c = 0
			coding_key = 'utf-8'
			for item in msg_content.walk():
				if c != 0:
					for i in item.values():
						if 'GB2312' in i:
							coding_key = 'GB2312'
				c += 1
			
			content = get_body(msg_content, coding_key)
			email_dic["subject"] = subject
			email_dic["from_user"] = from_user
			email_dic["to_user"] = to_user
			email_dic["send_date"] = send_date
			email_dic["content"] = content
			email_dic["bytes_size"] = bytes_size
			email_list.append(email_dic)
		email_info_dic = {
			"email_count": email_total_num,
			"email_info": email_list
		}
		email_obj.close()
		return email_info_dic
	except Exception as e:
		logger.error(str(e))
		return False

def format_date(date_send):
	try:
		date_send = time.ctime(time.mktime(date_send[:len(date_send) - 1]))
		if date_send:
			d_l = date_send.strip().split(' ')
			return f'{d_l[-1]}:{month_dic[d_l[1]]}:{d_l[2]}-{d_l[3]}'
		else:
			return None
	except Exception as e:
		logger.error(str(e))
		return None


def decode_str(s):
	try:
		if not s:
			return None
		value, charset = decode_header(s)[0]
		if charset:
			value = value.decode(charset)
		return value
	except Exception as e:
		logger.error(str(e))

# if __name__ == '__main__':
# 	host = "zhunda.com"  # pop3服务器地址
# 	username = "dangyuanyang@zhunda.com"  # 邮箱用户名
# 	password = "zhunda2021"  # 邮箱密码
# 	email = create_connect(username=username, selfs='vfsd', password=password, host=host)
# 	if email:
# 		email_num, email_obj = get_email(email)
# 		if email_num:
# 			dic_info = handle_email(email_num, email_obj)
# 			print(dic_info)
# 		else:
# 			print('邮件总数量为 0')
