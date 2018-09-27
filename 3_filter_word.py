from imp import reload
import sys

default_encoding = 'utf-8'

reload(sys)
sys.setdefaultencoding('utf8')


def main():
    input_file = open("/Data/test/skn_all_w2v/result_seg.txt")
    output_file = open('/Data/test/skn_all_w2v/result_seg_filter.txt', 'w')

    lines = input_file.readlines()
    index = 0
    for line in lines:
        words = line.split()
        word_set = list()
        skn = ""
        for word in words:
            if word.isdigit():
                if len(word) == 8:
                    skn = word
            elif "," == word:
                continue
            else:
                word_set.append(str(word).lower())
        output_file.write(skn + "\t" + " ".join(str(i) for i in word_set) + "\n")
        index += 1
        if index % 1000 == 0:
            print(index)
    input_file.close()


main()
