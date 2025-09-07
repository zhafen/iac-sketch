# Databricks notebook source
# MAGIC %md
# MAGIC # Setup
# MAGIC

# COMMAND ----------

# DBTITLE 1,Install ra_lib
# MAGIC %run ../../../../../../shared_resources/ra_lib_setup

# COMMAND ----------

# DBTITLE 1,Imports
from ra_lib import assistant

# COMMAND ----------

# DBTITLE 1,Object creation
# Get the assistant class to help out
ra = assistant.ResearchAssistant()

# COMMAND ----------

# DBTITLE 1,Load cohort
# Delete this if you don't use cohorts
cohort_df = ra.load_cohort()

# COMMAND ----------

# MAGIC %md
# MAGIC # Query

# COMMAND ----------

# MAGIC %md
# MAGIC ### Simple on-prem queries
# MAGIC
# MAGIC Getting data from on-prem is as simple as putting your on-prem query into `ResearchAssistant.query`.
# MAGIC The results of your query are saved as a temporary view if you pass in a view name.
# MAGIC You can use the on-prem data exactly as any other view, meaning you can blend it with cloud data.

# COMMAND ----------

ra.query(
    "SELECT * FROM nm_bi.information_schema.tables",
    view_name="example"
)
display(spark.table("example"))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Using temp tables with on-prem queries
# MAGIC In some cases you don't want to pull the data into the cloud until you've done several operations,
# MAGIC each of which creates a temp table. In such a case, you can use an open connection, as shown below.

# COMMAND ----------

# Get the open connection
connection = ra.get_connection()

# COMMAND ----------

# Make a temporary table, keeping the connection open
ra.query(
    """SELECT *
    INTO #nm_bi_tables
    FROM nm_bi.information_schema.tables
    """,
    connection=connection,
)

# COMMAND ----------

# Access the temp table that's stored on the on-prem server
ra.query(
    """SELECT * FROM #nm_bi_tables
    """,
    connection=connection,
    view_name="report",
)
display(spark.table("report"))

# COMMAND ----------

# Close the connection when you're done with it
connection.close()

# COMMAND ----------

# MAGIC %md
# MAGIC # Wrapup

# COMMAND ----------

# DBTITLE 1,Save report table
# Call the function to save your report table.
# Requires a view named "report" or for you to otherwise specify the table.
ra.save_report_table()

# COMMAND ----------

# DBTITLE 1,Save a second report table
# If you have a second report table to save, use the following
# ra.save_report_table(view_name="my_other_view_to_save", table_label="your_preferred_label_to_distinguish_second_table")
