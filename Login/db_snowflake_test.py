import streamlit as st
import snowflake.connector

@st.cache_resource
def init_connection():
    return snowflake.connector.connect(
        user='wasan',
        password='Netflix28*',
        account='na61469.southeast-asia.azure',
        warehouses='MCTHAI_WH',
        database='mcthaidp',
        schema='mc1',
        client_session_keep_alive=True
    )
conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
