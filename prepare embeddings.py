# import packages
from gensim.models import KeyedVectors
from data.embedding import Embedding
import io



### Google Books ENG all ###

# convert to gensim txt format
for i in range(1800, 2000, 10):
    embeddings = Embedding.load("./data/Google/Original/" + str(i))
    with io.open("./data/Google/Gensim txt/" + "google" + str(i) + ".txt", "w", encoding="UTF-8") as fp:
        for word in embeddings.iw:
            fp.write(word + " " + " ".join(map(str, (embeddings[word]))) + "\n")

# load txt into gensim

google1800 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1800.txt", binary=False, no_header=True)
google1810 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1810.txt", binary=False, no_header=True)
google1820 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1820.txt", binary=False, no_header=True)
google1830 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1830.txt", binary=False, no_header=True)
google1840 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1840.txt", binary=False, no_header=True)
google1850 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1850.txt", binary=False, no_header=True)
google1860 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1860.txt", binary=False, no_header=True)
google1870 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1870.txt", binary=False, no_header=True)
google1880 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1880.txt", binary=False, no_header=True)
google1890 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1890.txt", binary=False, no_header=True)
google1900 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1900.txt", binary=False, no_header=True)
google1910 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1910.txt", binary=False, no_header=True)
google1920 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1920.txt", binary=False, no_header=True)
google1930 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1930.txt", binary=False, no_header=True)
google1940 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1940.txt", binary=False, no_header=True)
google1950 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1950.txt", binary=False, no_header=True)
google1960 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1960.txt", binary=False, no_header=True)
google1970 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1970.txt", binary=False, no_header=True)
google1980 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1980.txt", binary=False, no_header=True)
google1990 = KeyedVectors.load_word2vec_format("./data/Google/Gensim txt/google1990.txt", binary=False, no_header=True)


# save all data in gensim format

google1800.save('./data/Google/vectors1800.kv')
google1810.save('./data/Google/vectors1810.kv')
google1820.save('./data/Google/vectors1820.kv')
google1830.save('./data/Google/vectors1830.kv')
google1840.save('./data/Google/vectors1840.kv')
google1850.save('./data/Google/vectors1850.kv')
google1860.save('./data/Google/vectors1860.kv')
google1870.save('./data/Google/vectors1870.kv')
google1880.save('./data/Google/vectors1880.kv')
google1890.save('./data/Google/vectors1890.kv')
google1900.save('./data/Google/vectors1900.kv')
google1910.save('./data/Google/vectors1910.kv')
google1920.save('./data/Google/vectors1920.kv')
google1930.save('./data/Google/vectors1930.kv')
google1940.save('./data/Google/vectors1940.kv')
google1950.save('./data/Google/vectors1950.kv')
google1960.save('./data/Google/vectors1960.kv')
google1970.save('./data/Google/vectors1970.kv')
google1980.save('./data/Google/vectors1980.kv')
google1990.save('./data/Google/vectors1990.kv')





### COHA ###

# convert to gensim txt format
for i in range(1810, 2010, 10):
    embeddings = Embedding.load("./data/COHA/Original/" + str(i))
    with io.open("./data/COHA/Gensim txt/" + "COHA" + str(i) + ".txt", "w", encoding="UTF-8") as fp:
        for word in embeddings.iw:
            fp.write(word + " " + " ".join(map(str, (embeddings[word]))) + "\n")

# load txt into gensim

COHA1810 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1810.txt", binary=False, no_header=True)
COHA1820 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1820.txt", binary=False, no_header=True)
COHA1830 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1830.txt", binary=False, no_header=True)
COHA1840 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1840.txt", binary=False, no_header=True)
COHA1850 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1850.txt", binary=False, no_header=True)
COHA1860 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1860.txt", binary=False, no_header=True)
COHA1870 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1870.txt", binary=False, no_header=True)
COHA1880 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1880.txt", binary=False, no_header=True)
COHA1890 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1890.txt", binary=False, no_header=True)
COHA1900 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1900.txt", binary=False, no_header=True)
COHA1910 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1910.txt", binary=False, no_header=True)
COHA1920 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1920.txt", binary=False, no_header=True)
COHA1930 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1930.txt", binary=False, no_header=True)
COHA1940 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1940.txt", binary=False, no_header=True)
COHA1950 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1950.txt", binary=False, no_header=True)
COHA1960 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1960.txt", binary=False, no_header=True)
COHA1970 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1970.txt", binary=False, no_header=True)
COHA1980 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1980.txt", binary=False, no_header=True)
COHA1990 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA1990.txt", binary=False, no_header=True)
COHA2000 = KeyedVectors.load_word2vec_format("./data/COHA/Gensim txt/COHA2000.txt", binary=False, no_header=True)


# save all data in gensim format

COHA1810.save('./data/COHA/vectors1810.kv')
COHA1820.save('./data/COHA/vectors1820.kv')
COHA1830.save('./data/COHA/vectors1830.kv')
COHA1840.save('./data/COHA/vectors1840.kv')
COHA1850.save('./data/COHA/vectors1850.kv')
COHA1860.save('./data/COHA/vectors1860.kv')
COHA1870.save('./data/COHA/vectors1870.kv')
COHA1880.save('./data/COHA/vectors1880.kv')
COHA1890.save('./data/COHA/vectors1890.kv')
COHA1900.save('./data/COHA/vectors1900.kv')
COHA1910.save('./data/COHA/vectors1910.kv')
COHA1920.save('./data/COHA/vectors1920.kv')
COHA1930.save('./data/COHA/vectors1930.kv')
COHA1940.save('./data/COHA/vectors1940.kv')
COHA1950.save('./data/COHA/vectors1950.kv')
COHA1960.save('./data/COHA/vectors1960.kv')
COHA1970.save('./data/COHA/vectors1970.kv')
COHA1980.save('./data/COHA/vectors1980.kv')
COHA1990.save('./data/COHA/vectors1990.kv')
COHA2000.save('./data/COHA/vectors2000.kv')






### Google books fiction ###

# convert to gensim txt format
for i in range(1800, 2000, 10):
    embeddings = Embedding.load("./data/Google fiction/Original/" + str(i))
    with io.open("./data/Google fiction/Gensim txt/" + "googlefiction" + str(i) + ".txt", "w", encoding="UTF-8") as fp:
        for word in embeddings.iw:
            fp.write(word + " " + " ".join(map(str, (embeddings[word]))) + "\n")

# load txt into gensim

googlefiction1800 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1800.txt", binary=False, no_header=True)
googlefiction1810 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1810.txt", binary=False, no_header=True)
googlefiction1820 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1820.txt", binary=False, no_header=True)
googlefiction1830 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1830.txt", binary=False, no_header=True)
googlefiction1840 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1840.txt", binary=False, no_header=True)
googlefiction1850 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1850.txt", binary=False, no_header=True)
googlefiction1860 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1860.txt", binary=False, no_header=True)
googlefiction1870 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1870.txt", binary=False, no_header=True)
googlefiction1880 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1880.txt", binary=False, no_header=True)
googlefiction1890 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1890.txt", binary=False, no_header=True)
googlefiction1900 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1900.txt", binary=False, no_header=True)
googlefiction1910 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1910.txt", binary=False, no_header=True)
googlefiction1920 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1920.txt", binary=False, no_header=True)
googlefiction1930 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1930.txt", binary=False, no_header=True)
googlefiction1940 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1940.txt", binary=False, no_header=True)
googlefiction1950 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1950.txt", binary=False, no_header=True)
googlefiction1960 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1960.txt", binary=False, no_header=True)
googlefiction1970 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1970.txt", binary=False, no_header=True)
googlefiction1980 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1980.txt", binary=False, no_header=True)
googlefiction1990 = KeyedVectors.load_word2vec_format("./data/Google fiction/Gensim txt/googlefiction1990.txt", binary=False, no_header=True)


# save all data in gensim format

googlefiction1800.save('./data/Google fiction/vectors1800.kv')
googlefiction1810.save('./data/Google fiction/vectors1810.kv')
googlefiction1820.save('./data/Google fiction/vectors1820.kv')
googlefiction1830.save('./data/Google fiction/vectors1830.kv')
googlefiction1840.save('./data/Google fiction/vectors1840.kv')
googlefiction1850.save('./data/Google fiction/vectors1850.kv')
googlefiction1860.save('./data/Google fiction/vectors1860.kv')
googlefiction1870.save('./data/Google fiction/vectors1870.kv')
googlefiction1880.save('./data/Google fiction/vectors1880.kv')
googlefiction1890.save('./data/Google fiction/vectors1890.kv')
googlefiction1900.save('./data/Google fiction/vectors1900.kv')
googlefiction1910.save('./data/Google fiction/vectors1910.kv')
googlefiction1920.save('./data/Google fiction/vectors1920.kv')
googlefiction1930.save('./data/Google fiction/vectors1930.kv')
googlefiction1940.save('./data/Google fiction/vectors1940.kv')
googlefiction1950.save('./data/Google fiction/vectors1950.kv')
googlefiction1960.save('./data/Google fiction/vectors1960.kv')
googlefiction1970.save('./data/Google fiction/vectors1970.kv')
googlefiction1980.save('./data/Google fiction/vectors1980.kv')
googlefiction1990.save('./data/Google fiction/vectors1990.kv')
