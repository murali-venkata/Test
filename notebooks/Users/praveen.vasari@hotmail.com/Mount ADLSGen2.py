# Databricks notebook source
configs = {"fs.azure.account.auth.type": "OAuth",
       "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
       "fs.azure.account.oauth2.client.id": "ec0ea228-d3ef-4e95-b36d-facf95360550",
       "fs.azure.account.oauth2.client.secret": "igf8Q~6PyfYlvKmdFoJ_GazFm5Tn3_ssWqmnabVN",
       "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/c3d71b04-dd51-4d21-94a2-b610828cb6ee/oauth2/token",
       "fs.azure.createRemoteFileSystemDuringInitialization": "true"}

dbutils.fs.mount(
source = "abfss://landing@azurezen2murali.dfs.core.windows.net",mount_point = "/mnt/azurezen2muralilanding",extra_configs = configs)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls mnt/azurezen2muralilanding

# COMMAND ----------

df_emp=spark.read.csv('/mnt/azurezen2muralilanding/dept1.csv',header='True')

# COMMAND ----------

# MAGIC %fs head dbfs:/mnt/azurezen2muralilanding/dept_emp.csv