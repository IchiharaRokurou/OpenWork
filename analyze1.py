#!/usr/bin/env python3
# -*- coding: utf8 -*-
from pykakasi import kakasi

kakasi = kakasi()
kakasi.setMode('H', 'a')
conv = kakasi.getConverter()

name = ''
sogai = ['p', 't', 'k', 'b', 'd', 'g', 's', 'z', 'h']
kyoumei = ['m', 'n', 'y', 'r', 'w']
sogai_num = 0
kyoumei_num = 0
sum = 0

txt_n = ['demon_comp.txt', 'engel_comp.txt', 'all_monsters_comp.txt']

for txt in txt_n:
    with open(txt, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line[:-1]
            l = line.split()
            name = l[0].replace('っ', '').replace(
                'ゃ', '').replace('ゅ', '').replace('ょ', '')
            name = name.replace('ぁ', '').replace(
                'ぃ', '').replace('ぅ', '').replace('ぇ', '').replace('ぉ', '')
            name = conv.do(name)
            name = name.replace('-', '').replace('\'', '')
            for check in sogai:
                sogai_num += name.count(check)
            for check in kyoumei:
                kyoumei_num += name.count(check)

    sum = sogai_num + kyoumei_num
    s_p = round((sogai_num / sum) * 100, 1)
    k_p = round((kyoumei_num / sum) * 100, 1)

    print(txt.replace('_comp.txt', ''))
    print('阻害音:' + str(sogai_num) + '個'
          + '(' + str(s_p) + '%)')
    print('共鳴音:' + str(kyoumei_num) + '個'
          + '(' + str(k_p) + '%)')
    print('計:' + str(sum) + '個')
    sogai_num = 0
    kyoumei_num = 0
    sum = 0
