from pyspark.sql import SparkSession
from IPython.display import HTML

spark = SparkSession.builder.appName("Create Table").getOrCreate()

data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
columns = ["Name", "Score"]
df = spark.createDataFrame(data, columns)
df.show()

pandas_df = df.toPandas()

html_table = pandas_df.to_html(index=False)
print(html_table)

HTML(html_table)
