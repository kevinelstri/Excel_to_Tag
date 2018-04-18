import xlrd

'''
注意：此版本表头的读取，未考虑表格标题和表格中空行的存在
'''

'''
读取excel文件，将原excel表头与目标库进行匹配，
将匹配成功的标签写入到excel表头下面，也就是增加一行来保存表头
'''
def read_xlsx(filename):
	data = xlrd.open_workbook(filename)
	# print(data)
	sheet = data.sheets()[0]  # 通过索引顺序获取第一个工作表
	# print(sheet)
	sheet = data.sheet_by_index(0)  # 通过索引来选取第一个工作表
	# print(sheet)
	nrows = sheet.nrows  # 行数
	ncols = sheet.ncols  # 列数
	# print(nrows, ncols)  # 行，列
	first = sheet.row_values(0)
	second = sheet.row_values(1)

	# print(len(first), len(second))  # 列数相等

	for i in range(len(first)):
		if first[i] == '' and second[i] != '':
			first[i] = first[i-1]
	# print(first, second)

	# excel表头转换
	result = []
	for i in range(len(first)):
		if first[i] == '' and second[i] == '':
			result.append('')
		if first[i] != '' and second[i] == '':
			result.append(first[i])
		if first[i] !='' and second[i] != '':
			result.append(first[i]+'.'+second[i])
	return result

if __name__ == '__main__':
	filename = '111.xlsx'
	result = read_xlsx(filename)
	# print(len(result))
	print(result)


