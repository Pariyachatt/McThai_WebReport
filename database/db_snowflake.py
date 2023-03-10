import streamlit as st
import snowflake.connector
import pandas as pd
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine

class DBSnowflake:
    def __init__(self):
        self.conn = snowflake.connector.connect(
            user='wasan',
            password='Netflix28*',
            account='na61469.southeast-asia.azure',
            warehouses='MCTHAI_WH',
            database='mcthaidp',
            schema='mc1',
            client_session_keep_alive=True
        )

        self.url = URL(
            user='wasan',
            password='Netflix28*',
            account='na61469.southeast-asia.azure',
            warehouses='MCTHAI_WH',
            database='mcthaidp',
            schema='mc1'
        )
        
    def run_query(self, query):
        with self.conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    def report_query(self, query):
        engine = create_engine(self.url)
        connection = engine.connect()
        return pd.read_sql(query, connection)

    def run_insert(self, sql):
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)
            return "done"
        except Exception as e:
            return str(e)
