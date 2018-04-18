import Levenshtein
from read_xls_multiline import read_xlsx
from read_xls_lib import read_lablib
from segment_stopwords import seg
from add_to_test import add_data

# 计算两个词语之间的编辑距离
def Edit_distance_str(str1, str2):
    import Levenshtein
    edit_distance_distance = Levenshtein.distance(str1, str2)
    similarity = 1-(edit_distance_distance/max(len(str1), len(str2)))
    return similarity

# 计算表头之间的相似度
def calSimilarity(filename):
	# 读取excel表
	# filename = '111.xlsx'
	# count为表头行，raw_excel为原始excel表头
	count, raw_excel = read_xlsx(filename)  # 读取excel表头文件
	raw_excel = seg(raw_excel)  # 对表头进行分词处理

	# 读取标签库文件
	libname = 'lablib_new.xls'
	# 调用read_lablib()函数来读取目标词库中的目标词表
	first, second, third = read_lablib()  # 读取目标库数据
	first = seg(first)  # 对目标库列表进行分词处理
	# 使用编辑距离进行相似度计算
	# word1 = '时间'
	# word2 = '时间'
	# similarity = Edit_distance_str(word1, word2)
	# print(Levenshtein.distance(word1, word2))

	# word1 = raw_excel[1]
	# word2 = first[1]
	# similarity = Edit_distance_str(word1, word2)
	# print(Levenshtein.distance(word1, word2))

	# 将具有一定相似度的数据写入到csv文件中
	f = open('save_match.csv', 'a+')
	# 新添加一行匹配的标签结果
	newrow = []
	for i in range(len(raw_excel[:])):
		sim = []
		for j in range(len(first[1:])):
			# 编辑距离计算原词表与目标词表之间的相似度
			sim.append(Edit_distance_str(raw_excel[i], first[j]))  # 相似度算法不准确，不具有语义信息
		maxSimilarity = max(sim)  # 选取最大相似度
		if maxSimilarity > 0.8:
			Line = []  # 最有最大相似度值的相似度行
			addnum = sim.index(maxSimilarity)
			Line.append(raw_excel[i])  # 原表头
			Line.append(first[addnum])  # 目标表头
			Line.append(second[addnum])  # 匹配标签
			Line.append(maxSimilarity)  # 相似度
			# print(first[addnum])
			newrow.append(second[addnum])
			print(Line)

			# 将具有一定相似度的（原表头、目标表头、标签、相似度值），写入csv文件
			s = ''
			for i in range(len(Line)-1):
				s += Line[i]+','
			s += str(Line[-1])
			if s not in f:
				f.write(s)
				f.write('\n')
		else:
			Line = []  # 找不到最大相似度值的行，写入到库中
			if raw_excel[i] != '':
				Line.append(raw_excel[i])  # 目标表头
				add_data(libname, Line)  # 未匹配的原表头写入到目标库中
			newrow.append('')
	return newrow


if __name__ == '__main__':
	filename = '222.xls'
	newrow = calSimilarity(filename)
	print(len(newrow))
	print(newrow)
