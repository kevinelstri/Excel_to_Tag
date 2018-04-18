import xlrd
import re
'''
注意：此版本改进了之前版本对excel的读取，
将表格的标题和表格中的空行进一步处理，
以及使用正则表达式对单元格中空格和换行符的替换操作
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

	# 表头提取
	count = 0  # 插入一行的位置
	title = ''
	first = []
	second = []
	for i in range(nrows):
		line = sheet.row_values(i)
		if line is not None:
			s = ''
			for l in line:
				s += str(l)
			if s == '':
				count += 1
			if s != '' and s == line[0]:  # 去除excel空行，并将表头的标题提取出来
				title = line[0]
				count += 1
				# print('标题：', title)
			if s != '' and s != line[0]:  # 去除空行
				if first == []:
					first = [re.sub('\n| ','', str(ele)) for ele in line]
					count += 1
				elif first != [] and second == []:
					second = [re.sub('\n| ','', str(ele)) for ele in line]
					count += 1
					break
	# print(count)
	# print(title, first, second)

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
	return count, result

if __name__ == '__main__':
	filename = '222.xls'
	count, result = read_xlsx(filename)
	# print(len(result))
	print()
	print(count)
	print(result)


