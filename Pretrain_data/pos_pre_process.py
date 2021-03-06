#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/5/7 10:57

from tqdm import tqdm
import pkuseg

pku_seg = pkuseg.pkuseg(model_name='medicine', postag=True)


def pku(line):
    pku_result = pku_seg.cut(line)
    return [(word, tag) for (word, tag) in pku_result]


if __name__ == '__main__':
    with open('corpora/R.txt','r',encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    total_nums = len(lines)
    print('total lines:', total_nums)

    word_cuts_all = []
    tags_all = []

    batch = 100
    nums = int(total_nums / batch)
    for i in tqdm(range(nums)):
        lines_temp = lines[i * batch: (i + 1) * batch]
        word_cuts = cut(lines_temp)
        word_cuts_all += word_cuts
        tags = tagger(word_cuts)
        tags_all += tags

    word_cuts = cut(lines[nums * batch: total_nums])
    word_cuts_all += word_cuts
    tags = tagger(word_cuts)
    tags_all += tags

    assert len(tags_all) == total_nums

    with open('corpora/R_word_cuts.txt','w',encoding='utf-8') as f:
        [f.write(str(word_cuts) + '\n') for word_cuts in word_cuts_all]

    with open('corpora/R_tags.txt','w',encoding='utf-8') as f:
        [f.write(str(tas) + '\n') for tas in tags_all]

