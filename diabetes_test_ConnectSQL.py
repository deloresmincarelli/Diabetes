
# This code just verifies we can connect to sqlite database

import pandas as pd
import sqlalchemy as sql

# Note, the database file does not have ".db" as suffix
sql_engine = sql.create_engine("sqlite:///DIABETES_DATABASE")
sql_engine
conn = sql_engine.connect()

# Table Names - run all 3 of these; the last one will show name of tables
metadata = sql.MetaData()

metadata.reflect(bind=sql_engine)

metadata.tables.keys()

# Read the tables - run this line of code to see data from the table in Terminal window

pd.read_sql_table('DIABETES_PREDICTIONS_TABLE', conn)
pd.read_sql_table('PATIENT_ER_VISITS_TABLE', conn)
# close the connection 

conn.close()


