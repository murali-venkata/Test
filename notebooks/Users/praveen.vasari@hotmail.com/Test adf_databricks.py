# Databricks notebook source
# MAGIC %fs ls dbfs:/FileStore/tables

# COMMAND ----------

fileName=dbutils.widgets.get("filepath")
print(fileName)

# COMMAND ----------

df1 = spark.read.format("csv").option("header", "true").load(fileName)

# COMMAND ----------

df1.show()

# COMMAND ----------

dbutils.notebook.exit("{'status':'success','newfilepath':'abc/xyz'}")

# COMMAND ----------

df1.show()