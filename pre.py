# -*- coding: gb18030 -*-


def pre(novelname):
    linelist = []
    file = open("jinyong/"+novelname+".txt", "r", encoding='gb18030')
    while 1:
        line = file.readline()
        if not line:
            print("��"+novelname+"��Ԥ�������")
            break
        line2 = line.replace("��������www.cr173.com���txtС˵����վ", '')
        line2 = line2.replace("���������ѵ��������עwww.cr173.com", '')
        line2 = line2.replace('\u3000', '')

        linelist.append(line2)

    file.close()
    file = open(r'jinyong/done/'+novelname+'done.txt', 'w', encoding='gb18030')
    for i in linelist:
        file.write(i)
    file.close()
