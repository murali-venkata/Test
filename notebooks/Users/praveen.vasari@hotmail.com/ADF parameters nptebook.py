# Databricks notebook source
dbutils.widgets.text('tablename','employee','tablename')

# COMMAND ----------

dbutils.widgets.get('tablename')

# COMMAND ----------

dbutils.widgets.getArgument('tablename')

# COMMAND ----------

name=dbutils.widgets.get('personname')
print('person name is:',name)


# COMMAND ----------

location=dbutils.widgets.get('personlocation')
print('personloaction is',location)

# COMMAND ----------

avg_salary=250.65
dbutils.notebook.exit(avg_salary)

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.azurezen2murali.dfs.core.windows.net", "iZ6BD3GSJ8jvaziOXq2N4gwto33Iv/5l10wRDRaM4GYlUdR+vzHr+EKrdYQj8q/NDI3KJ+0OiZtb+AStq6AuFQ==")

# COMMAND ----------

dbutils.fs.ls("abfss://azurezen2murali.dfs.core.windows.net/")