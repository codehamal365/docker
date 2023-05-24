from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, IntegerType

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

    # 构建表结构
    schema = StructType().add('id', IntegerType(), nullable=False). \
        add('name', StringType(), nullable=True). \
        add('score', IntegerType(), nullable=False)

    df = spark.createDataFrame(rdd, schema)

    df.show(20, False)

    # 将df对象转换成临时视图表 可供sql语句查询
    df.createTempView('people')

    spark.sql("SELECT * FROM people WHERE score = 20").show()
