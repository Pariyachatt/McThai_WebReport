import streamlit as st
# import snowflake.connector
# from db_snowflake_test import *
from database.db_snowflake import *

# def test():
#     rows = run_query("SELECT profit_name, profit_email FROM mcthaidp.mc1.user_alive WHERE profit_email='Borompong.Phairatphiboon@th.mcd.com' LIMIT 1;")
#
#     return rows

# # Print results.
# for row in rows:
#     st.write(f"{row[0]} has a :{row[1]}:")

# connectDBlocal("SELECT profit_name, profit_email FROM mcthaidp.mc1.user_alive WHERE profit_email='Borompong.Phairatphiboon@th.mcd.com' LIMIT 1")

# sql = "select * from vw_Net_Sales_Report where " + '"Date"' + \
#     " between "+f"'{s_date}'" + " and " + f"'{e_date}'"
# result = connectDB(sql)
#
# print(result)

def checkAlive(type, mailAuth):
    sql = "SELECT "+type+"_name, "+type+"_email FROM mcthaidp.mc1.user_alive WHERE profit_email="+ f"'{mailAuth}'" +" LIMIT 1;"
    return run_query(sql)
    # return sql
#
def profitAlive(umail):
    res = checkAlive("profit", umail)
    if res:
        return res
    else:
        return res
# profitAlive('Borompong.Phairatphiboon@th.mcd.com')
# def patchAlive(umail):
#     # mail ==
#     return 1
# def storeAlive(umail):
#     # mail ==
#     return 1
#
# def signup():
#     # mail ==
#     return 1
#
# def forgetPassword():
#     return 1
#
# def changePassword():
#     return 1
