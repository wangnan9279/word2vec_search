#!/usr/bin/env python
# -*- coding: utf-8  -*-
#测试训练好的模型
from __builtin__ import raw_input, unicode
import sys

import gensim
import urllib



if __name__ == '__main__':
    fdir = '/Data/test/skn_click_w2v/'
    model = gensim.models.Word2Vec.load(fdir + 'text.model')
    input = u"nike air 运动鞋"
    print "input is : "+input
    word = model.most_similar(input)
    for t in word:
        print t[0],t[1]

    #print model[u'vans']

    '''
    word = model.most_similar(positive=[u'皇上',u'国王'],negative=[u'皇后'])
    for t in word:
        print t[0],t[1]


    print model.doesnt_match(u'太后 妃子 贵人 贵妃 才人'.split())
    print model.similarity(u'书籍',u'书本')
    print model.similarity(u'逛街',u'书本')
    '''


