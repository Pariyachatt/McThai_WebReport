import snowflake.connector
import streamlit as st


def connectDB(sql):
    ctx = snowflake.connector.connect(
        user='wasan',
        password='Netflix28*',
        account='ad28777.southeast-asia.azure',
        warehouses='mcthai_wh',
        database='mcthaidp',
        schema='mc1'
    )
    cs = ctx.cursor()
    # st.write(cs)
    try:
        result = cs.execute(sql).fetch_pandas_all()

    finally:
        cs.close()
    ctx.close()
    return result
