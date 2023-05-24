import uuid

from pyspark import SparkContext

conf = {
    "es.nodes.wan.only": "true",
    "es.index.auto.create": "true",
    "es.nodes": "localhost",
    "es.port": "9200",
    "es.resource": "my-index",
}

rdd = SparkContext(appName="test").newAPIHadoopRDD(
    "org.elasticsearch.hadoop.mr.EsInputFormat",
    "org.apache.hadoop.io.NullWritable",
    "org.elasticsearch.hadoop.mr.LinkedMapWritable",
    conf=conf)
print(rdd.first())

