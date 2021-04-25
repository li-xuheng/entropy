# -*- coding: gb18030 -*-
# bigram


import jieba
import math


def get_tf(tf_dic, words):  # ��Ƶͳ��
    for i in range(len(words)):
        if words[i] not in tf_dic:
            tf_dic[words[i]] = 1
        else:
            tf_dic[words[i]] += 1
    pass


def get_bigram_tf(tf_dic, words):  # bi-gram��Ƶͳ��
    for i in range(len(words)-1):
        tf_dic[(words[i], words[i+1])] = tf_dic.get((words[i], words[i+1]), 0) + 1  # ��һ��ͳ�ƴ�Ƶ�ķ���
    pass


def cal_bigram(words_bi_tf, words_bi_len, words_tf):
    entropy = []
    for bi_word in words_bi_tf.items():
        jp_xy = bi_word[1] / words_bi_len  # �������ϸ���p(x,y)
        cp_xy = bi_word[1] / words_tf[bi_word[0][0]]  # ������������p(x|y)
        entropy.append(-jp_xy * math.log(cp_xy, 2))  # ����bigram��Ϣ��
    return round(sum(entropy), 4)


def gram(novelname):
    with open('jinyong/done/'+novelname+'done.txt', 'r', encoding='gb18030') as f:
        corpus = []  # ���Ͽ⣬ÿһ�����ݣ�txt�ļ��е�ÿһ�У�����Ϊ�ַ����б��е�һ��Ԫ��
        count = 0  # С˵����
        for line in f:
            if line != '\n':
                corpus.append(line.strip())  # strip()��������ȥ���ַ������ߵĿո�
                count += len(line.strip())

    split_words = []  # �ִʽ��
    words_len = 0  # ����
    line_count = 0  # ����
    words_tf = {}  # uni_gram��Ƶ
    words_bi_tf = {}  # bi_gram��Ƶ
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
