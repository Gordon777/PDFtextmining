#encoding = utf8
import re

import jieba
import jieba.analyse  # 导入结巴jieba相关模块
import jieba.posseg as pseg
#  加载用户词典
jieba.load_userdict("userdict.txt")
output = open(r'Jieba詞性.csv', 'a')
output.write('詞語,詞性\n')
stopkeyword = [line.strip() for line in open(r"stopwords.txt", "r", encoding="utf-8-sig").readlines()]  # 将停止词文件保存到列表
text = open(r"test.txt", "r", encoding="utf-8-sig").read()  # 导入需要计算的内容
pseg.re_han_default = re.compile("([\u4E00-\u9FD5a-zA-Z0-9+#&\._% ]+)", re.U) #add_word前要加
jieba.add_word('computer audit','Computer auditing')

# 分析詞性
words = pseg.cut(text)


# 写入到csv
for word,flag in words:
        print('%s,%s' %( word, flag))
        output.write('%s,%s\n' % (
            word, flag))

output.close()