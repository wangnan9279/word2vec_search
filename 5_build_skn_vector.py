# -*- coding: UTF-8 -*-
from imp import reload
import sys

default_encoding = 'utf-8'

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    input_file = open("/Data/test/skn_all_w2v/text.vector")  # 返回一个文件对象
    output_file = open('/Data/test/skn_all_w2v/skn.vector', 'w')
    lines= input_file.readlines()  # 调用文件的 readline()方法
    for line in lines:
        index = line.find(" ")
        keyword = line[0:index]
        if keyword.isdigit():
            if len(keyword) == 8:
                output_file.write(line)
    input_file.close()


main()
