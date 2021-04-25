# -*- coding: gb18030 -*-
# unigram


import jieba
import math


def get_tf(tf_dic, words):  # 词频统计
    for i in range(len(words)):
        if words[i] not in tf_dic:
            tf_dic[words[i]] = 1
        else:
            tf_dic[words[i]] += 1
    pass


def cal_gram(words_tf, words_len):
    entropy = []
    for word in words_tf.items():
        xy = word[1]/words_len
        entropy.append(-xy*math.log(xy, 2))  # 计算unigram信息熵
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
    for line in corpus:
        for x in jieba.cut(line):
            split_words.append(x)
            words_len += 1

        get_tf(words_tf, split_words)
        split_words = []
        line_count += 1
    uni_len = sum([dic[1] for dic in words_tf.items()])
    entropy = cal_gram(words_tf, uni_len)
    return count, words_len, uni_len, entropy
