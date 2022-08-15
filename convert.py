#!/usr/bin/env python3
# -*- coding: utf8 -*-
from pykakasi import kakasi
import re
import jaconv

kakasi = kakasi()
kakasi.setMode('J', 'H')
conv = kakasi.getConverter()

name = ''
rare = ['UR', 'SR', 'R', 'N']

# 作成したいファイル名をmk_file.txtに入れる
d = open('mk_file.txt', mode='w', encoding='utf-8')
end = 0
n = []
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# データが入っているテキストの名前をfile.txtに入れる

with open('file.txt', 'r', encoding='utf-8') as f:
    line = f.readlines()
    for i in range(len(line)):
        for j in range(len(line[i])):
            if end == 1:
                if(line[i][j] != '点'):
                    j += 1
                else:
                    end = 0
            elif(line[i][j] != '/'):
                name += line[i][j]

            else:
                for r in rare:
                    if r in name:
                        # name = name[:name.rfind(r)]
                        if name[-1] == '-':
                            name = name[-1]
                        else:
                            name = name[:-3]
                        name += '\n'
                        name = name.replace('カードレア度ATKDEF評価', '').replace('該当なし', '').replace(
                            '-', '').replace('・', '').replace('『', '').replace('』', '')
                        name = re.sub(r"[a-z]", "", name)
                        name = re.sub(r"[A-Z]", "", name)
#                        name = re.sub(r"[0-9]", "", name)
                        x = 0
                        y = 0

                        if name != '\n' and '?' not in name:
                            if name[:-1].isdecimal():
                                pass
                            else:
                                c = -2
                                n = []
                                while name[c - 1:c] in number:
                                    c -= 1
                                n.append(name[:c])
                                n.append(name[c:-1])
                                if n[1] == '00':
                                    pass
                                else:
                                    if n[1][0] == '0':
                                        n.append(n[1][1:])
                                        n[1] = '0'
                                    elif n[1][3] != '0':
                                        n.append(n[1][3:])
                                        n[1] = n[1][:3]
                                    else:
                                        if len(n[1]) == 4:
                                            n.append(n[1][3:])
                                            n[1] = n[1][:3]
                                        else:
                                            n.append(n[1][4:])
                                            n[1] = n[1][:4]
                                    nm = ""
                                    for m in n:
                                        nm += m + " "
                                        name = nm[:-1] + '\n'
                                    name = conv.do(name)
                                    name = jaconv.kata2hira(name)
                                    d.write(name)
                                    break
                name = ''
                end = 1

d.close()
