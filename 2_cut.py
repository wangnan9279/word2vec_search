import codecs
import jieba
import jieba.analyse

default_encoding = 'utf-8'


def main():

    f = codecs.open('/Data/test/skn_all_w2v/result.txt', 'r', encoding='utf8')
    target = codecs.open('/Data/test/skn_all_w2v/result_seg.txt', 'w', encoding='utf8')
    print 'open files.'
    lineNum = 1
    line = f.readline()
    while line:
        print '---processing ', lineNum, ' article---'
        seg_list = jieba.cut(line, cut_all=False)
        line_seg = ' '.join(seg_list)
        target.writelines(line_seg)
        lineNum = lineNum + 1
        line = f.readline()
    print 'well done.'
    f.close()
    target.close()

    return 0
main()
