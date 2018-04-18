# import gensim

# model = gensim.models.KeyedVectors.load_word2vec_format('vectors.bin', binary=True)

# list1 = ['的']
# list2 = ['在']

# sim = model.n_similarity(list1, list2)
# print(sim)

from gensim.models import KeyedVectors
word_vectors = KeyedVectors.load_word2vec_format('vectors.bin', binary=True)

sim1 = word_vectors.most_similar(['时间'])
print(sim1)
