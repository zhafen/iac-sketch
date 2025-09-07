# Databricks notebook source
# MAGIC %md
# MAGIC # Cohort notebook

# COMMAND ----------

# MAGIC %md
# MAGIC # Setup

# COMMAND ----------

# DBTITLE 1,Install ra_lib
# MAGIC %run ../../../../../../shared_resources/ra_lib_setup

# COMMAND ----------

# DBTITLE 1,Imports
# Imports
from ra_lib import assistant

# COMMAND ----------

# DBTITLE 1,Object creation
# Get the assistant class to help out
ra = assistant.ResearchAssistant()

# COMMAND ----------

# MAGIC %md
# MAGIC # Query

# COMMAND ----------

# Cloud query example
display(spark.sql("SELECT * FROM research_dm.research_cohort.reports_config"))

# COMMAND ----------

# On-prem query example
ra.query(
    """SELECT * FROM nm_bi.information_schema.tables
    """,
    view_name="cohort"
)
display(spark.table("cohort"))

# COMMAND ----------

# MAGIC %md
# MAGIC # Wrapup

# COMMAND ----------

# DBTITLE 1,Save the cohort
# The following will work as long as we have a temporary view
# named cohort consisting of one column with data type string.
ra.save_cohort()
