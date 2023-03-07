import streamlit as st
import snowflake.connector

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

    def run_query(self, query):
        with self.conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    def run_insert(self, sql):
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)
            return "done"
        except Exception as e:
            return str(e)
