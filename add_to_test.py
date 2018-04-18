import xlrd
import xlwt
from xlutils.copy import copy

'''
在excel中添加一行来存储数据，
并通过覆盖原excel文件来实现数据的添加
'''
def add_data(filename, info):
	rb = xlrd.open_workbook(filename, formatting_info=True)  # 打开原excel文件
	rs = rb.sheet_by_index(0)  # 获取excel中的一个sheet表
	wb = copy(rb)  # 复制excel
	ws = wb.get_sheet(0)  # 获取sheet表

	line = rs.nrows  # excel表中的行数
	# print(line)

	for i in range(len(info)):
		ws.write(line, i, info[i])
	wb.save(filename)  # 覆盖原excel文件中

if __name__ == '__main__':
	filename = 'test.xls'
	# 添加一行数据
	info = ['12', '张三' , '73728874838943827', '美的', '2018.04', 'american']
	add_data(filename, info)
