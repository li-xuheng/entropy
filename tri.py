# -*- coding: gb18030 -*-
# trigram


import jieba
import math


def get_bigram_tf(tf_dic, words):  # bi-gram��Ƶͳ��
    for i in range(len(words)-1):
        tf_dic[(words[i], words[i+1])] = tf_dic.get((words[i], words[i+1]), 0) + 1
    pass


def get_trigram_tf(tf_dic, words):  # tri-gram��Ƶͳ��
    for i in range(len(words)-2):
        tf_dic[((words[i], words[i+1]), words[i+2])] = tf_dic.get(((words[i], words[i+1]), words[i+2]), 0) + 1
    pass


def cal_trigram(words_tri_tf, words_tri_len, words_bi_tf):
    entropy = []
    for tri_word in words_tri_tf.items():
        jp_xy = tri_word[1] / words_tri_len  # �������ϸ���p(x,y)
        cp_xy = tri_word[1] / words_bi_tf[tri_word[0][0]]  # ������������p(x|y)
        entropy.append(-jp_xy * math.log(cp_xy, 2))  # ����trigram��Ϣ��
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
    words_bi_tf = {}  # bi_gram��Ƶ
    words_tri_tf = {}  # tri_gram��Ƶ
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
