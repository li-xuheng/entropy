# -*- coding: gb18030 -*-
# 这是可以输出pretty table的运行文件

import pre
import uni
import bi
import tri
import time
import prettytable as pt


def cal(novelname):
    start = time.time()
    pre.pre(novelname)  # 写入小说书名，对文件做预处理
    count, words_len, uni_len, uni_entropy = uni.gram(novelname)  # 计算unigram的平均信息熵
    # print("语料库字数", count)
    # print("分词个数", words_len)
    # print("一元模型长度:", uni_len)
    # print("基于unigram的平均信息熵为:", uni_entropy, "比特/词")
    # print('-' * 50)
    words_bi_len, bi_entropy = bi.gram(novelname)  # 计算bigram的平均信息熵
    # print("二元模型长度:", words_bi_len)
    # print("基于bigram的平均信息熵为:", bi_entropy, "比特/词")
    # print('-' * 50)
    words_tri_len, tri_entropy = tri.gram(novelname)  # 计算trigram的平均信息熵
    # print("三元模型长度:", words_tri_len)
    # print("基于trigram的平均信息熵为:", tri_entropy, "比特/词")
    # print('-' * 50)
    end = time.time()
    tb = pt.PrettyTable()
    tb.field_names = ["书名", "word_nums", "word_tokens", "unigram_len", "unigram_entropy",
                      "bigram_len", "bigram_entropy", "trigram_len", "trigram_entropy", "time"]
    tb.add_row([novelname, count, words_len, uni_len, uni_entropy,
                words_bi_len, bi_entropy, words_tri_len, tri_entropy, (end-start)])
    print(tb)
    print("计算《" + novelname + "》信息熵共用时 %.3f s" % (end - start))
    with open('result.txt', 'a') as f:
        # f.write(tb)
        # f.write("计算《" + novelname + "》信息熵共用时 %.3f s" % (end - start))
        # f.write('\n\n\n')
        print(tb, file=f)
        print("计算《" + novelname + "》信息熵共用时 %.3f s" % (end - start), file=f)
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
