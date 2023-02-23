import streamlit as st
# import snowflake.connector
# from db_snowflake_test import *
from database.db_snowflake import *
# import hashlib
from hashlib import sha256

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


def sha256Auth(pwauth):
    return sha256(pwauth.encode('utf-8')).hexdigest()

def addUserAuth(mailAuth, passAuth):
    _passAuth = sha256Auth(passAuth)
    sql = """
        INSERT INTO MCTHAIDP.MC1.USER_AUTH( USER_MAIL, PASSWORD)
        VALUES('"""+mailAuth+"""', '"""+_passAuth+"""');
    """
    run_query(sql)

def changePwAuth(mailAuth, passAuth):
    return 1

def checkAlive(type, mailAuth):
    sql = "SELECT "+type+"_name, "+type+"_email FROM mcthaidp.mc1.user_alive WHERE profit_email="+ f"'{mailAuth}'" +" LIMIT 1;"
    return run_query(sql)
    # return sql
#
def profitAlive(email):
    res = checkAlive("profit", email)
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
