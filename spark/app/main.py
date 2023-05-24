from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('test').setMaster('spark://master:7077')

sc = SparkContext(conf=conf)
words = sc.parallelize(
    ["scala",
     "java",
     "hadoop",
     "spark",
     "akka",
     "spark vs hadoop",
     "pyspark",
     "pyspark and spark"]
)
counts = words.count()
print(counts)




