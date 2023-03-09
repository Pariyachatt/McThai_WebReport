import streamlit as st
from database.db_snowflake import *
from hashlib import sha256

## Functions
# 1. Check user Alive authen or not. = Done
# 2. Checking password to login = in-prograss
# 3. Signup = Done
# 4. change pass: oldpass, newpass confirmpass
# 5. forget pass: get pass random by click mail from


# authentication step 2: check mail user
class PermistionAuth:
    def __init__(self, mailAuth):
        self.userUlive = 'MCTHAIDP.MC1.user_alive'
        self.tpyesList = ['profit', 'patch', 'store']
        # self.tpyesList = ['patch', 'profit', 'store']
        # self.tpyesList = ['store', 'patch', 'profit']
        self.mailAuth = mailAuth
        self.DBSnowflake = DBSnowflake()

    def checkAlive(self):
        rold_dict = {}

        for type in self.tpyesList:
            sql = """ SELECT """+ type +"""_name, """+ type +"""_email FROM """+ self.userUlive +""" WHERE """+ type +"""_email='"""+ self.mailAuth +"""' LIMIT 1; """
            resQuery = self.DBSnowflake.run_query(sql)
            if resQuery:
                # st.write("Found: ", sql)
                # rold_dict{}
                return resQuery[0][0]
            # st.write("Next: ", sql)
