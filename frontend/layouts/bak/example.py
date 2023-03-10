# import streamlit as st
# from st_aggrid import AgGrid
# import pandas as pd
#
# df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
#
# st.write(df)
#
# AgGrid(df)
#

import snowflake.connector
import pandas as pd
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine

url = URL(
    user='wasan',
    password='Netflix28*',
    account='na61469.southeast-asia.azure',
    warehouses='MCTHAI_WH',
    database='mcthaidp',
    schema='mc1'
)
engine = create_engine(url)
connection = engine.connect()

query = '''
select top 10* from MCTHAIDP.MC1.vw_Net_Sales_Report
'''

df = pd.read_sql(query, connection)

df
