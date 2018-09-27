import time
import sys
from imp import reload

from pyspark.sql import HiveContext, SparkSession

default_encoding = 'utf-8'

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    ss = SparkSession.builder.master("spark://ip:7077").appName("search-task").enableHiveSupport().getOrCreate()
    hc = HiveContext(ss.sparkContext)
    hc.sql("use w2v")
    result = hc.sql("select product_skn,brand,sort,name,keyword from product_brand_sort_name_keyword")
    rows = result.collect()
    f = open('/Data/test/skn_all_w2v/result.txt', 'w')
    for row in rows:
        f.write(str(row['product_skn']) + "\t"+str(row['brand']) + "\t"+str(row['sort']) + "\t"+str(row['name']) + "\t" + str(row['keyword']) + "\n")
    f.close()
    return 0


main()
