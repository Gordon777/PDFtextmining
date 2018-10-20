#coding=utf-8

# Import Libraries
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.probability import *
import csv

# Set Variables
with open('2010.txt', 'r') as file:
    cooking_text =  open(r"2010.txt", "r", encoding="utf-8-sig").read()  # 导入需要计算的内容

file = csv.writer(open('NLTK詞頻.csv', 'w'))

cooking_tokens = word_tokenize(cooking_text)
text = nltk.Text(cooking_tokens)

# Load in Stopwords Library
stopwords = stopwords.words('english')

word_set = []

# Define Functions
def normalize_text(text):
    # Work through all the words in text and filter
    for word in text:
        # Check if word is a word, and not punctuation, AND check against stop words
        if word.isalpha() and word.lower() not in stopwords:
            # If it passes the filters, save to word_set
            word_set.append(word.lower())
    return word_set

# Make Function Calls
#print cooking_text[0:20]
#print cooking_tokens[0:10]
#print text.concordance('economics')
#print text.collocations()
#print text.similar('Pot')

normalize_text(text)

fd = FreqDist(word_set)
print (fd.most_common())
#print fd.hapaxes()
#fd.plot(50,cumulative=False)

# Print results to a CSV file
for key, count in fd.most_common():
    file.writerow([key, count])
