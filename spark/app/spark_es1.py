from pyspark import SparkConf, SparkContext
import os

conf = SparkConf().setAppName(
    'My App').setMaster('local[1]')

sc = SparkContext(conf=conf)

es_conf = {"es.nodes": "elasticsearch", "es.port": "9200", "es.resource": "my_index",
           "es.index.read.missing.as.empty": "true", "es.filter": '{"query": {"match": {"content": "quick"}}}'}
rdd = sc.newAPIHadoopRDD("org.elasticsearch.hadoop.mr.EsInputFormat", "org.apache.hadoop.io.NullWritable",
                         "org.elasticsearch.hadoop.mr.LinkedMapWritable", conf=es_conf)
x = rdd.first()

print(x)