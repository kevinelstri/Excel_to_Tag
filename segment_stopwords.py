import numpy as np
import jieba
from read_xls_multiline import read_xlsx
from read_xls_lib import read_lablib

# 停用词处理
stopwords = []
with open('stop-words_zh_hit.txt', encoding='utf-8') as f:
	for line in f:
		stopwords.append(line.strip())

'''
分词处理，分别对excel原数据表头和目标数据对象进行分词处理
'''
def seg(raw_excel):
	result = []
	for line in raw_excel:
		line = line.strip()
		segline = ''
		seglines = jieba.cut(line)
		for seg in seglines:
			if seg not in stopwords:
				segline += seg
		result.append(segline)
		# print(segline)  # 分词后的结果
	return result

if __name__ == '__main__':
	filename = '222.xls'
	# count为表头行，raw_excel为原始excel表头
	count, raw_excel = read_xlsx(filename)
	result = seg(raw_excel)
	print(result)
	print('--------------------------------')

	first, second, third = read_lablib()
	result = seg(first)
	print(result)


