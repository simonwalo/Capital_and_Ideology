
import pickle
with open('./data/models_all.pickle', 'rb') as handle:
    models_all = pickle.load(handle)

# save data in word2vec format

vectors1800 = models_all[1800]
vectors1800.save_word2vec_format('./data/vectors1800.bin', binary=True)
vectors1810 = models_all[1810]
vectors1810.save_word2vec_format('./data/vectors1810.bin', binary=True)
vectors1820 = models_all[1820]
vectors1820.save_word2vec_format('./data/vectors1820.bin', binary=True)
vectors1830 = models_all[1830]
vectors1830.save_word2vec_format('./data/vectors1830.bin', binary=True)
vectors1840 = models_all[1840]
vectors1840.save_word2vec_format('./data/vectors1840.bin', binary=True)
vectors1850 = models_all[1850]
vectors1850.save_word2vec_format('./data/vectors1850.bin', binary=True)
vectors1860 = models_all[1860]
vectors1860.save_word2vec_format('./data/vectors1860.bin', binary=True)
vectors1870 = models_all[1870]
vectors1870.save_word2vec_format('./data/vectors1870.bin', binary=True)
vectors1880 = models_all[1880]
vectors1880.save_word2vec_format('./data/vectors1880.bin', binary=True)
vectors1890 = models_all[1890]
vectors1890.save_word2vec_format('./data/vectors1890.bin', binary=True)
vectors1900 = models_all[1900]
vectors1900.save_word2vec_format('./data/vectors1900.bin', binary=True)
vectors1910 = models_all[1910]
vectors1910.save_word2vec_format('./data/vectors1910.bin', binary=True)
vectors1920 = models_all[1920]
vectors1920.save_word2vec_format('./data/vectors1920.bin', binary=True)
vectors1930 = models_all[1930]
vectors1930.save_word2vec_format('./data/vectors1930.bin', binary=True)
vectors1940 = models_all[1940]
vectors1940.save_word2vec_format('./data/vectors1940.bin', binary=True)
vectors1950 = models_all[1950]
vectors1950.save_word2vec_format('./data/vectors1950.bin', binary=True)
vectors1960 = models_all[1960]
vectors1960.save_word2vec_format('./data/vectors1960.bin', binary=True)
vectors1970 = models_all[1970]
vectors1970.save_word2vec_format('./data/vectors1970.bin', binary=True)
vectors1980 = models_all[1980]
vectors1980.save_word2vec_format('./data/vectors1980.bin', binary=True)
vectors1990 = models_all[1990]
vectors1990.save_word2vec_format('./data/vectors1990.bin', binary=True)


# save data in gensim format

from gensim.models import KeyedVectors

vectors1800 = models_all[1800]
vectors1800.save('./data/vectors1800.kv')
vectors1810 = models_all[1810]
vectors1810.save('./data/vectors1810.kv')
vectors1820 = models_all[1820]
vectors1820.save('./data/vectors1820.kv')
vectors1830 = models_all[1830]
vectors1830.save('./data/vectors1830.kv')
vectors1840 = models_all[1840]
vectors1840.save('./data/vectors1840.kv')
vectors1850 = models_all[1850]
vectors1850.save('./data/vectors1850.kv')
vectors1860 = models_all[1860]
vectors1860.save('./data/vectors1860.kv')
vectors1870 = models_all[1870]
vectors1870.save('./data/vectors1870.kv')
vectors1880 = models_all[1880]
vectors1880.save('./data/vectors1880.kv')
vectors1890 = models_all[1890]
vectors1890.save('./data/vectors1890.kv')
vectors1900 = models_all[1900]
vectors1900.save('./data/vectors1900.kv')
vectors1910 = models_all[1910]
vectors1910.save('./data/vectors1910.kv')
vectors1920 = models_all[1920]
vectors1920.save('./data/vectors1920.kv')
vectors1930 = models_all[1930]
vectors1930.save('./data/vectors1930.kv')
vectors1940 = models_all[1940]
vectors1940.save('./data/vectors1940.kv')
vectors1950 = models_all[1950]
vectors1950.save('./data/vectors1950.kv')
vectors1960 = models_all[1960]
vectors1960.save('./data/vectors1960.kv')
vectors1970 = models_all[1970]
vectors1970.save('./data/vectors1970.kv')
vectors1980 = models_all[1980]
vectors1980.save('./data/vectors1980.kv')
vectors1990 = models_all[1990]
vectors1990.save('./data/vectors1990.kv')


# save COHA embeddings in Gensim format

coha1810 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1810.txt', binary=False, no_header=True)
coha1820 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1820.txt', binary=False, no_header=True)
coha1830 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1830.txt', binary=False, no_header=True)
coha1840 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1840.txt', binary=False, no_header=True)
coha1850 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1850.txt', binary=False, no_header=True)
coha1860 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1860.txt', binary=False, no_header=True)
coha1870 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1870.txt', binary=False, no_header=True)
coha1880 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1880.txt', binary=False, no_header=True)
coha1890 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1890.txt', binary=False, no_header=True)
coha1900 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1900.txt', binary=False, no_header=True)
coha1910 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1910.txt', binary=False, no_header=True)
coha1920 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1920.txt', binary=False, no_header=True)
coha1930 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1930.txt', binary=False, no_header=True)
coha1940 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1940.txt', binary=False, no_header=True)
coha1950 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1950.txt', binary=False, no_header=True)
coha1960 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1960.txt', binary=False, no_header=True)
coha1970 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1970.txt', binary=False, no_header=True)
coha1980 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1980.txt', binary=False, no_header=True)
coha1990 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_1990.txt', binary=False, no_header=True)
coha2000 = KeyedVectors.load_word2vec_format('./data/COHA/Original/coha-word_sgns_gensim_2000.txt', binary=False, no_header=True)


coha1810.save('./data/COHA/vectors1810.kv')
coha1820.save('./data/COHA/vectors1820.kv')
coha1830.save('./data/COHA/vectors1830.kv')
coha1840.save('./data/COHA/vectors1840.kv')
coha1850.save('./data/COHA/vectors1850.kv')
coha1860.save('./data/COHA/vectors1860.kv')
coha1870.save('./data/COHA/vectors1870.kv')
coha1880.save('./data/COHA/vectors1880.kv')
coha1890.save('./data/COHA/vectors1890.kv')
coha1900.save('./data/COHA/vectors1900.kv')
coha1910.save('./data/COHA/vectors1910.kv')
coha1920.save('./data/COHA/vectors1920.kv')
coha1930.save('./data/COHA/vectors1930.kv')
coha1940.save('./data/COHA/vectors1940.kv')
coha1950.save('./data/COHA/vectors1950.kv')
coha1960.save('./data/COHA/vectors1960.kv')
coha1970.save('./data/COHA/vectors1970.kv')
coha1980.save('./data/COHA/vectors1980.kv')
coha1990.save('./data/COHA/vectors1990.kv')
coha2000.save('./data/COHA/vectors2000.kv')


