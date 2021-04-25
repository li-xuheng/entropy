# -*- coding: gb18030 -*-


def pre(novelname):
    linelist = []
    file = open("jinyong/"+novelname+".txt", "r", encoding='gb18030')
    while 1:
        line = file.readline()
        if not line:
            print("《"+novelname+"》预处理完成")
            break
        line2 = line.replace("本书来自www.cr173.com免费txt小说下载站", '')
        line2 = line2.replace("更多更新免费电子书请关注www.cr173.com", '')
        line2 = line2.replace('\u3000', '')

        linelist.append(line2)

    file.close()
    file = open(r'jinyong/done/'+novelname+'done.txt', 'w', encoding='gb18030')
    for i in linelist:
        file.write(i)
    file.close()
