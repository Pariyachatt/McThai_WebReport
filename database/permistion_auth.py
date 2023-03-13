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
        found_role_type = ""
        before_role_select = list()

        for type in self.tpyesList:
            # sql = """ SELECT """+ type +"""_name, """+ type +"""_email FROM """+ self.userUlive +""" WHERE """+ type +"""_email='"""+ self.mailAuth +"""' LIMIT 1; """
            sql = """ SELECT * FROM """+ self.userUlive +""" WHERE """+ type +"""_email='"""+ self.mailAuth +"""' LIMIT 1; """
            resQuery = self.DBSnowflake.run_query(sql)
            if resQuery:
                user_role['role_type'] = type
                user_role['store_code'] = resQuery[0][0]
                user_role['store_name'] = resQuery[0][1]
                user_role['patch_name'] = resQuery[0][3]
                user_role['profit_name'] = resQuery[0][5]

                st.write("type:  ", type)
                st.write("resQuery  ", resQuery)
                return user_role

    # ---------- Report select option ---------- #

    def sqlRoleFormat(self, optRole, res_con='sql'):
        p_list = list()
        for p in optRole:
            p_list.append(p)
        if res_con == 'sql':
            pram = "'',''".join(p_list)
            return ",'[''"+pram+"'']'"
        else:
            pram = "','".join(p_list)
            return "'"+pram+"'"

    def setFormat(self, sqlResp):
        resfm = list()
        for x in sqlResp:
            resfm.append(list(x)[0])
        return resfm

    # for Administrator role
    def getProfitName(self):
        pass

    # for Profit role
    # @st.cache_resource
    def getProfitName(self, profit, debug=False):
        sql = """
        SELECT DISTINCT(PATCH_NAME) FROM """+ self.userUlive +""";
        """
        if debug:
            st.write("getProfitName >> ",sql)
        return self.setFormat(self.DBSnowflake.run_query(sql))

    def getPatchName(self, profit, debug=False):
        sql = """
        SELECT DISTINCT(PATCH_NAME) FROM """+ self.userUlive +"""
        WHERE PROFIT_NAME='"""+profit+"""'
        AND PROFIT_EMAIL='"""+self.mailAuth+"""';
        """
        if debug:
            st.write("getPatchName >> ",sql)
        return self.setFormat(self.DBSnowflake.run_query(sql))


    # for Patch role
    def getStoreNameCode(self, profit, patchs, debug=False):
        sql = """
        SELECT DISTINCT(CONCAT(STORE_CODE,'|',STORE_NAME)) FROM """+ self.userUlive +"""
        WHERE PROFIT_NAME='"""+profit+"""'
        AND PATCH_NAME IN ("""+patchs+""")
        AND PROFIT_EMAIL='"""+self.mailAuth+"""';
        """
        if debug:
            st.write("getPatchName >> ",sql)
        return self.setFormat(self.DBSnowflake.run_query(sql))
