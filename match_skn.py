#!/usr/bin/env python
# -*- coding: utf-8  -*-
# 测试训练好的模型
import numpy as np
import sys

import gensim
import urllib

from gensim.models import Word2Vec


def main():
    fdir = '/Data/test/skn_keyword_w2v/product_brand_sort_name_keyword/'
    #model = gensim.models.Word2Vec.load(fdir + 'text.model')
    model = gensim.models.KeyedVectors.load_word2vec_format(fdir + 'text.vector', binary=False)
    #model = gensim.models.KeyedVectors.load_word2vec_format(fdir+'skn_average.vector', binary=False)


    input = u"印花"

    print "input is : " + input
    #word = model.most_similar(input)

    #for t in word:
        #print t[0], t[1]

    vector_skn = model[input]

    print "【word vector】"
    print vector_skn




    #print "【averge vector】"
    #vector_skn_list = [model[u'izzue'], model[u'女式'], model[u'个性'], model[u'印花'], model[u'休闲'], model[u'背心']]

    #vec_list = [1] * 100
    #for i in range(100):
        #sum = 0
        #for j in range(5):
            #vector = vector_skn_list[j]
            #value = vector[i]
            #sum += value
        #averge = sum / 100
        #vec_list[i] = averge

    #print vec_list

    #print "【cos】"
    #result = cos(vector_skn, vec_list)
    #print result

    #print
    #"result :"

    print "【result】"

    model2 = gensim.models.KeyedVectors.load_word2vec_format(fdir + 'skn.vector', binary=False)
    word = model2.similar_by_vector(np.array(vector_skn.flat),
                                   topn=10)
    for t in word:
        print t[0], t[1]

    #word = model.similar_by_vector( np.array([2.1172310e-03,-4.4086878e-03,2.0042551e-03,3.6892148e-03,2.5091355e-04,-2.1932428e-03,-5.2581979e-03,2.4035794e-03,1.1743482e-03,2.5080673e-03,-1.9683253e-03,-7.3637469e-03,-2.3572689e-03,-2.3667514e-03,-5.4457579e-03,1.8232261e-03,-8.5532255e-03,3.6773831e-03,2.2637025e-03,-4.2129615e-03,6.5243505e-03,5.8635543e-03,4.4522309e-03,1.3279644e-03,1.6948396e-03,8.4407977e-05,6.8992667e-04,5.5966321e-03,-3.5526287e-03,2.4850257e-03,-1.0008086e-03,-6.1683347e-03,-2.3582564e-03,2.6809804e-03,3.4196328e-03,3.1120125e-03,8.8125450e-04,-2.6590696e-03,2.1196792e-03,1.1207899e-02,1.1833846e-03,-4.0875445e-03,-2.7947722e-03,2.4032129e-03,2.0556421e-04,3.0710245e-03,-6.3196998e-03,-1.7264606e-03,1.8719730e-03,6.2328274e-03,-4.9188460e-04,-1.3969307e-03,4.6461257e-03,-2.2720899e-03,3.9135390e-03,-3.6661285e-03,4.7624568e-03,1.1466012e-03,-1.5051144e-03,-2.3562915e-03,-4.7041066e-03,-6.0585961e-03,-2.2477289e-03,-8.5335504e-04,2.6586503e-03,-1.6132039e-03,3.5328378e-03,-3.2124356e-03,8.6853106e-04,5.2891071e-03,3.1704875e-03,3.3240947e-03,-2.4066560e-03,-9.7608529e-03,6.8913400e-03,-3.9412165e-03,9.9765286e-03,-8.3397655e-03,-4.3550031e-03,1.0896300e-02,7.2592869e-04,2.4112011e-03,-9.4960751e-03,-9.1123674e-04,-3.8886652e-03,-3.2182082e-03,2.0528135e-03,1.5725137e-04,7.6011387e-03,-4.4964938e-03,1.3775956e-03,3.2305683e-04,-3.8627035e-03,-1.2367291e-03,-3.2902490e-03,9.6386345e-04,1.4435301e-03,3.9328646e-04,2.1237582e-03,3.1612357e-03]),
    #                                topn = 300)
    #for t in word:
       # print t[0], t[1]

    '''
    word = model.most_similar(positive=[u'皇上',u'国王'],negative=[u'皇后'])
    for t in word:
        print t[0],t[1]
    print model.doesnt_match(u'太后 妃子 贵人 贵妃 才人'.split())
    print model.similarity(u'书籍',u'书本')
    print model.similarity(u'逛街',u'书本')
    '''


def cos(vector1, vector2):#
    dot_product = 0.0;
    normA = 0.0;
    normB = 0.0;
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return None
    else:
        return dot_product / ((normA * normB) ** 0.5)


main()
