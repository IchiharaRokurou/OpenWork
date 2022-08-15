#!/usr/bin/env python3
# -*- coding: utf8 -*-
from pykakasi import kakasi
import matplotlib.pyplot as plt
import numpy as np

kakasi = kakasi()
kakasi.setMode('H', 'a')
conv = kakasi.getConverter()

name = ''
dakuon = ['b', 'd', 'g', 'z', 'j', 'v']
dakuon_num = 0
dakuon_attack = [0] * 6
dakuon_defense = [0] * 6
d_num = [0] * 6
i = 1

with open('all_monsters_comp.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line[:-1]
        l = line.split()
        attack = int(l[1])
        defense = int(l[2])
        name = l[0].replace('っ', '').replace(
            'ゃ', '').replace('ゅ', '').replace('ょ', '')
        name = name.replace('ぁ', '').replace(
            'ぃ', '').replace('ぅ', '').replace('ぇ', '').replace('ぉ', '')
        name = conv.do(name)
        name = name.replace('-', '').replace('\'', '')

        dakuon_num = 0
        for check in dakuon:
            dakuon_num += name.count(check)

        for i in range(0, 6):
            if dakuon_num == i:
                dakuon_attack[i] += attack
                dakuon_defense[i] += defense
                d_num[i] += 1
                break

        if dakuon_num > 5:
            dakuon_attack[5] += attack
            dakuon_defense[5] += defense
            d_num[5] += 1


for i in range(6):
    dakuon_attack[i] = dakuon_attack[i] / d_num[i]
    dakuon_defense[i] = dakuon_defense[i] / d_num[i]

left = np.arange(len(dakuon_defense))
label = ['0', '1', '2', '3', '4', 'Over 5']

width = 0.3

plt.xlabel('Number of dull sound')
plt.ylabel('Value')
plt.bar(left, dakuon_attack, color='r',
        width=width, align='center', label='attack')
plt.bar(left + width, dakuon_defense, color='b',
        width=width, align='center', label='defense')
plt.legend()
plt.xticks(left + width / 2, label)
plt.show()
plt.xlabel('Number of dull sound')
plt.ylabel('Value')
plt.plot(left, dakuon_attack, color='r', label='attack')
plt.plot(left, dakuon_defense, color='b', label='defense')
plt.legend()
plt.show()
