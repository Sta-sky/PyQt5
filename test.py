# -*- coding: utf-8 -*-


def output_day(year, month, day):
	months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
	if 0 < month <= 12:
		sum = months[month - 1]
	else:
		print('date error')
		return False
	sum += day
	leap = 0
	if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
		leap = 1
	if (leap == 1) and (month > 2):
		sum += 1
	return (f'{year}-{month}-{day}: 是今年的第[ %d ]天' % sum)


if __name__ == '__main__':
	try:
		result = output_day(2021, 2, 12)
		print(result)
	except Exception as e:
		print(e)