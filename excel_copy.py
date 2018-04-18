import xlwt
import xlrd
from xlutils.copy import copy
from similarity import calSimilarity
from read_xls_multiline import read_xlsx
'''
复制excel文件，在新的excel文件中增加一行标签行
'''

def copyexcel(filename, newfilename):
	oldwb = xlrd.open_workbook(filename)  # 原始excel
	oldwbs = oldwb.sheet_by_index(0)  # 原始sheet0
	newwb = copy(oldwb)  # 复制新的excel
	newws = newwb.get_sheet(0)  # 新的sheet0
	# print(oldwbs.ncols)  # 列数

	# 增加一行相似度计算结果的标签
	newLabelRow = calSimilarity(filename)

	# 插入行的位置
	inserRowNo, result = read_xlsx(filename)  # 获取插入行的位置

	for colIndex in range(oldwbs.ncols):
		newws.write(inserRowNo, colIndex, newLabelRow[colIndex])  

	for rowIndex in range(inserRowNo+1, oldwbs.nrows):
	    for colIndex in range(oldwbs.ncols):
	    	# 写入数据，向下移动一行，将上一行数据写入到下一行中
	        newws.write(rowIndex + 1, colIndex, oldwbs.cell(rowIndex, colIndex).value)  
	newwb.save(newfilename)

if __name__ == '__main__':
	filename = '111.xlsx'
	newfilename = 'getfile111101.xls'
	copyexcel(filename, newfilename)
