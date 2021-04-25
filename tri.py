# -*- coding: gb18030 -*-
# trigram


import jieba
import math


def get_bigram_tf(tf_dic, words):  # bi-gram词频统计
    for i in range(len(words)-1):
        tf_dic[(words[i], words[i+1])] = tf_dic.get((words[i], words[i+1]), 0) + 1
    pass


def get_trigram_tf(tf_dic, words):  # tri-gram词频统计
    for i in range(len(words)-2):
        tf_dic[((words[i], words[i+1]), words[i+2])] = tf_dic.get(((words[i], words[i+1]), words[i+2]), 0) + 1
    pass


def cal_trigram(words_tri_tf, words_tri_len, words_bi_tf):
    entropy = []
    for tri_word in words_tri_tf.items():
        jp_xy = tri_word[1] / words_tri_len  # 计算联合概率p(x,y)
        cp_xy = tri_word[1] / words_bi_tf[tri_word[0][0]]  # 计算条件概率p(x|y)
        entropy.append(-jp_xy * math.log(cp_xy, 2))  # 计算trigram信息熵
    return round(sum(entropy), 4)


def gram(novelname):
    with open('jinyong/done/'+novelname+'done.txt', 'r', encoding='gb18030') as f:
        corpus = []  # 语料库，每一段内容（txt文件中的每一行），作为字符串列表中的一个元素
        count = 0  # 小说字数
        for line in f:
            if line != '\n':
                corpus.append(line.strip())  # strip()函数可以去掉字符串两边的空格
                count += len(line.strip())

    split_words = []  # 分词结果
    words_len = 0  # 词数
    line_count = 0  # 段数
    words_bi_tf = {}  # bi_gram词频
    words_tri_tf = {}  # tri_gram词频
    for line in corpus:
        for x in jieba.cut(line):
            split_words.append(x)
            words_len += 1
        get_bigram_tf(words_bi_tf, split_words)
        get_trigram_tf(words_tri_tf, split_words)
        split_words = []
        line_count += 1

    words_tri_len = sum([dic[1] for dic in words_tri_tf.items()])
    tri_entropy = cal_trigram(words_tri_tf, words_tri_len, words_bi_tf)
    return words_tri_len, tri_entropy
