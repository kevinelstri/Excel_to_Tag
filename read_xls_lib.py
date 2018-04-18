import xlrd
from pprint import pprint

'''
读取excel目标库文件，按列读取文件，
分别为（目标对象列，标签列，相似度阈值列）
'''
def read_lablib():
	filename = 'lablib.xlsx'
	data = xlrd.open_workbook(filename, 'utf-8')
	sheet = data.sheet_by_index(0)

	first = sheet.col_values(0)
	# temp = []
	# for i in range(len(first)):
		# temp.append(first[i].encode('utf-8').decode('utf-8'))
	# first = temp
	second = sheet.col_values(1)
	third = sheet.col_values(2)
	# 返回三列数据（目标对象数据，标签数据，相似度阈值数据）
	return first, second, third

if __name__ == '__main__':
	read_lablib()

