from pyspark.sql import SparkSession
from IPython.display import HTML

spark = SparkSession.builder.appName("DataFrame Example").getOrCreate()

data = [("Alice", 25, "female"), ("Bob", 30, "male"), ("Charlie", 35, "male"), ("David", 40, "male")]
columns = ["Name", "Age", "Gender"]
df = spark.createDataFrame(data, columns)

df.printSchema()

filtered_df = df.filter(df.Age > 30)
filtered_df.show()

pet_data = [("Alice", "dog"), ("Alice", "cat"), ("Bob", "cat"), ("David", "fish")]
pet_columns = ["Name", "Pet"]
pet_df = spark.createDataFrame(pet_data, pet_columns)

joined_df = df.join(pet_df, "Name")
joined_df.show()


pandas_df = joined_df.toPandas()

html_table = pandas_df.to_html(index=False)
print(html_table)

HTML(html_table)
