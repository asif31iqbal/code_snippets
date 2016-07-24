import json_mapper
from pyspark import SparkConf, SparkContext


conf = SparkConf("local[*]")
sc = SparkContext(conf=conf)

lines = sc.textFile('data')
lines.flatMap(json_mapper.map_line).saveAsTextFile('out_data7')
