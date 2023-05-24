from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder. \
        appName("spark_sql"). \
        getOrCreate()


    sc = spark.sparkContext

    df = spark.read.csv('/opt/bitnami/spark/data/stu_score.txt', sep=' ', header=False)
    df2 = df.toDF('id', 'name', 'score')
    df2.printSchema()
    df2.show()

    df2.createTempView('score')

    # SQL 风格
    spark.sql("""
    SELECT * from score LIMIT 5
    """).show()

    # DSL 风格
    df2.where("name='jim'").limit(5).show()
