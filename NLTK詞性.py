#coding=utf-8
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
import nltk


output = open(r'NLTK詞性.csv', 'a') #輸出格式
output.write('詞語,詞性\n') #輸出格式
# load data
text = open(r"1999-7.txt", "r", encoding="utf-8-sig").read()  # 导入需要计算的内容
# split into words
tokens = word_tokenize(text)
# convert to lower case
tokens = [w.lower() for w in tokens]
# remove punctuation from each word
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
# filter out stop words
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
pos_tags = nltk.tag.pos_tag(words) #NLTK詞性標註

for word,pos in pos_tags:
     # if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'): #只限制名詞
             print (word,pos)

# 写入到csv
for word,flag in pos_tags:
        print('%s,%s' %( word, flag))
        output.write('%s,%s\n' % (
            word, flag))

# 請加入詞語還有詞性在dict
dic = {"computer audit": "NN","Computer auditing":"NN"} #dictionary

csv = open(r'NLTK詞性.csv', 'a')

for key in dic.keys():
	name = key
	email = dic[key]
	row = name + "," + email + "\n"
	csv.write(row)