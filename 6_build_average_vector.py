# -*- coding: UTF-8 -*-
from imp import reload
import sys
import re
import gensim

default_encoding = 'utf-8'

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    fdir = '/Data/test/skn_all_w2v/'
    model = gensim.models.KeyedVectors.load_word2vec_format(fdir + 'text.vector', binary=False)

    input_file = open("/Data/test/skn_all_w2v/result_seg_filter.txt")
    output_file = open('/Data/test/skn_all_w2v/skn_average.vector', 'w')
    lines= input_file.readlines()
    index = 0
    for line in lines:
        words = line.split()
        skn_vector_list = []
        skn = ""
        for word in words:
            if word.isdigit():
                if len(word) == 8:
                    skn = word
            else:
                try:
                    input_word = str(word).decode('utf-8')
                    skn_vector_list.append(model[input_word])
                except:
                    continue
        if len(skn_vector_list) == 0:
            continue
        vec_list = [1] * 100
        for i in range(100):
            sum = 0
            for j in range(len(skn_vector_list)):
                vector = skn_vector_list[j]
                value = vector[i]
                sum += value
            average = round(sum /len(skn_vector_list),8)
            vec_list[i] = average
        output_file.write(skn + " " + " ".join(str(i) for i in vec_list)+"\n")
        index += 1
        if index % 1000 == 0:
            print index
    input_file.close()


main()
