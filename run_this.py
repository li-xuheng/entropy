# -*- coding: gb18030 -*-
# ���ǿ������pretty table�������ļ�

import pre
import uni
import bi
import tri
import time
import prettytable as pt


def cal(novelname):
    start = time.time()
    pre.pre(novelname)  # д��С˵���������ļ���Ԥ����
    count, words_len, uni_len, uni_entropy = uni.gram(novelname)  # ����unigram��ƽ����Ϣ��
    # print("���Ͽ�����", count)
    # print("�ִʸ���", words_len)
    # print("һԪģ�ͳ���:", uni_len)
    # print("����unigram��ƽ����Ϣ��Ϊ:", uni_entropy, "����/��")
    # print('-' * 50)
    words_bi_len, bi_entropy = bi.gram(novelname)  # ����bigram��ƽ����Ϣ��
    # print("��Ԫģ�ͳ���:", words_bi_len)
    # print("����bigram��ƽ����Ϣ��Ϊ:", bi_entropy, "����/��")
    # print('-' * 50)
    words_tri_len, tri_entropy = tri.gram(novelname)  # ����trigram��ƽ����Ϣ��
    # print("��Ԫģ�ͳ���:", words_tri_len)
    # print("����trigram��ƽ����Ϣ��Ϊ:", tri_entropy, "����/��")
    # print('-' * 50)
    end = time.time()
    tb = pt.PrettyTable()
    tb.field_names = ["����", "word_nums", "word_tokens", "unigram_len", "unigram_entropy",
                      "bigram_len", "bigram_entropy", "trigram_len", "trigram_entropy", "time"]
    tb.add_row([novelname, count, words_len, uni_len, uni_entropy,
                words_bi_len, bi_entropy, words_tri_len, tri_entropy, (end-start)])
    print(tb)
    print("���㡶" + novelname + "����Ϣ�ع���ʱ %.3f s" % (end - start))
    with open('result.txt', 'a') as f:
        # f.write(tb)
        # f.write("���㡶" + novelname + "����Ϣ�ع���ʱ %.3f s" % (end - start))
        # f.write('\n\n\n')
        print(tb, file=f)
        print("���㡶" + novelname + "����Ϣ�ع���ʱ %.3f s" % (end - start), file=f)
        print('\n\n\n', file=f)
    pass


if __name__ == '__main__':

    with open("jinyong/inf.txt", 'r', encoding='gb18030') as f:
        str = ''
        for title in f:
            str += title.strip()
        novelname = str.split(',')
        f.close()

    for i in range(len(novelname)):
        cal(novelname[i])
        pass
