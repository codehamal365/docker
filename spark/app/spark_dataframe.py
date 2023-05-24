from pyspark.sql import SparkSession

if __name__ == '__main__':
    # 构建入口对象
    spark = SparkSession.builder. \
        appName("test"). \
        master("local[1]"). \
        getOrCreate()

    sc = spark.sparkContext

    # 基于RDD转换成DataFrame
    rdd = sc.textFile('/opt/share/stu_score.txt'). \
        map(lambda x: x.split(" ")). \
        map(lambda x: (int(x[0]), x[1], int(x[2])))

    df = spark.createDataFrame(rdd, schema=['id', 'name', 'score'])

    df.printSchema()

    # 打印df中的数据
    # 参数1 表示展示多少数据 默认为20
    # 参数2 表示是否对列进行截断， 如果列的数据超过20 后续内容不显示
    df.show(20, False)

    # 将df对象转换成临时视图表 可供sql语句查询
    df.createTempView('people')

    spark.sql("SELECT * FROM people WHERE score = 20").show()

