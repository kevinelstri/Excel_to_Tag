import Levenshtein
from read_xls_multiline import read_xlsx
from read_xls_lib import read_lablib

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
	count, raw_excel = read_xlsx(filename) 

	# 读取标签库文件
	# libname = 'lablib.xlsx'
	# 调用read_lablib()函数来读取目标词库中的目标词表
	first, second, third = read_lablib()
	

	# 使用编辑距离进行相似度计算
	# word1 = '时间'
	# word2 = '时间'
	# similarity = Edit_distance_str(word1, word2)
	# print(Levenshtein.distance(word1, word2))

	# word1 = raw_excel[1]
	# word2 = first[1]
	# similarity = Edit_distance_str(word1, word2)
	# print(Levenshtein.distance(word1, word2))

	newrow = []
	for i in range(len(raw_excel[:])):
		sim = []
		for j in range(len(first[1:])):
			# 编辑距离计算原词表与目标词表之间的相似度
			sim.append(Edit_distance_str(raw_excel[i], first[j]))  # 相似度算法不准确，不具有语义信息
		maxSimilarity = max(sim)  # 选取最大相似度
		if maxSimilarity > 0.5:
			addnum = sim.index(maxSimilarity)
			# print(first[addnum])
			newrow.append(second[addnum])
		else:
			# print()
			newrow.append('')
	return newrow


if __name__ == '__main__':
	filename = '222.xls'
	newrow = calSimilarity(filename)
	print(len(newrow))
	print(newrow)
