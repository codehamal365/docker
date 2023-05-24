from pyspark import SparkConf, SparkContext
import os

conf = SparkConf().setAppName('My App')

sc = SparkContext(conf=conf)

es_conf = {"es.nodes": "elasticsearch", "es.port": "9200", "es.resource": "person",
           "es.index.read.missing.as.empty": "true"}
rdd = sc.newAPIHadoopRDD("org.elasticsearch.hadoop.mr.EsInputFormat", "org.apache.hadoop.io.NullWritable",
                         "org.elasticsearch.hadoop.mr.LinkedMapWritable", conf=es_conf)

print(rdd.collect())


result_rdd = rdd.filter(lambda x: x[1]['age'] >= 30).map(lambda x: x[1])

# rdd_res = rdd.map(lambda x: x[1]).groupBy(lambda t: t['name']).map(lambda x: [x[0], list(x[1])])

print(result_rdd.collect())
