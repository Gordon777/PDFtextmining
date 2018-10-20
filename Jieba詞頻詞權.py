#encoding = utf8
import re

import jieba
#  加载用户词典
jieba.load_userdict("userdict.txt")
import jieba.analyse  # 导入结巴jieba相关模块

stopkeyword = [line.strip() for line in open(r"stopwords.txt", "r", encoding="utf-8-sig").readlines()]  # 将停止词文件保存到列表
text = open(r"1999-7.txt", "r", encoding="utf-8-sig").read()  # 导入需要计算的内容
jieba.re_han_default = re.compile("([\u4E00-\u9FD5a-zA-Z0-9+#&\._% ]+)", re.U) #add_word前要加
jieba.add_word('computer audit')
jieba.add_word('Computer auditing')


zidian = {}
fenci = jieba.cut(text,cut_all=False)
for fc in fenci:
    if fc in zidian:
        zidian[fc] += 1
    else:
        zidian.setdefault(fc,1)   #字典中如果不存在键，就加入键，键值设置为1
        zidian[fc] = 1
# 计算tfidf
tfidf = jieba.analyse.extract_tags(text, topK="", withWeight=True)



# 写入到csv
output = open(r'Jieba詞頻詞權.csv', 'a')
output.write('詞語,詞頻,詞權\n')
for word_weight in tfidf:
    if word_weight in stopkeyword:
        pass
    else:  # 不存在的话就输出
        print
        word_weight[0], zidian.get(word_weight[0], 'not found'), str(int(word_weight[1] * 100)) + '%'
        output.write('%s,%s,%s\n' % (
        word_weight[0], zidian.get(word_weight[0], 'not found'), str(int(word_weight[1] * 100)) + '%'))
output.close()
