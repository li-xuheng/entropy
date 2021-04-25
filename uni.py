# -*- coding: gb18030 -*-
# unigram


import jieba
import math


def get_tf(tf_dic, words):  # ��Ƶͳ��
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
        entropy.append(-xy*math.log(xy, 2))  # ����unigram��Ϣ��
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
