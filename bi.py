# -*- coding: gb18030 -*-
# bigram


import jieba
import math


def get_tf(tf_dic, words):  # 词频统计
    for i in range(len(words)):
        if words[i] not in tf_dic:
            tf_dic[words[i]] = 1
        else:
            tf_dic[words[i]] += 1
    pass


def get_bigram_tf(tf_dic, words):  # bi-gram词频统计
    for i in range(len(words)-1):
        tf_dic[(words[i], words[i+1])] = tf_dic.get((words[i], words[i+1]), 0) + 1  # 另一种统计词频的方法
    pass


def cal_bigram(words_bi_tf, words_bi_len, words_tf):
    entropy = []
    for bi_word in words_bi_tf.items():
        jp_xy = bi_word[1] / words_bi_len  # 计算联合概率p(x,y)
        cp_xy = bi_word[1] / words_tf[bi_word[0][0]]  # 计算条件概率p(x|y)
        entropy.append(-jp_xy * math.log(cp_xy, 2))  # 计算bigram信息熵
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
    words_tf = {}  # uni_gram词频
    words_bi_tf = {}  # bi_gram词频
    for line in corpus:
        for x in jieba.cut(line):
            split_words.append(x)
            words_len += 1
        get_tf(words_tf, split_words)
        get_bigram_tf(words_bi_tf, split_words)

        split_words = []
        line_count += 1

    words_bi_len = sum([dic[1] for dic in words_bi_tf.items()])
    bi_entropy = cal_bigram(words_bi_tf, words_bi_len, words_tf)
    return words_bi_len, bi_entropy
