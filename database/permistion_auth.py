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
        self.tpyesList = ['PROFIT', 'PATCH', 'STORE']
        # self.tpyesList = ['patch', 'profit', 'store']
        # self.tpyesList = ['store', 'patch', 'profit']
        self.mailAuth = mailAuth
        self.DBSnowflake = DBSnowflake()

    def checkAlive(self):
        user_role = dict()

        for type in self.tpyesList:
            sql = """ SELECT """+ type +"""_name, """+ type +"""_email FROM """+ self.userUlive +""" WHERE """+ type +"""_email='"""+ self.mailAuth +"""' LIMIT 1; """
            resQuery = self.DBSnowflake.run_query(sql)
            if resQuery:
                # st.write("Found: ", sql)
                # rold_dict{}
                user_role['role_type'] = type
                user_role['role_name'] = resQuery[0][0]
                return user_role
                # return resQuery[0][0]
            # st.write("Next: ", sql)

    # ---------- Report select option ---------- #
    def setFormat(self, sqlResp):
        resfm = list()
        for x in sqlResp:
            resfm.append(list(x)[0])
        return resfm

    # for Administrator role
    def getProfitName(self):
        pass

    # for Profit role
    def getPatchName(self, profit,):
        sql = """
        SELECT DISTINCT(PATCH_NAME) FROM """+ self.userUlive +"""
        WHERE PROFIT_NAME='"""+profit+"""' AND PROFIT_EMAIL='"""+self.mailAuth+"""';
        """
        return self.setFormat(self.DBSnowflake.run_query(sql))

    # for Patch role
    def getStoreName(self):
        pass
