import streamlit as st
from database.db_snowflake import *
from hashlib import sha256

## Functions
# 1. Check user Alive authen or not. = Done
# 2. Checking password to login = in-prograss
# 3. Signup = Done
# 4. change pass: oldpass, newpass confirmpass
# 5. forget pass: get pass random by click mail from


# authentication step 2: add and check password
class PassAuth:
    def __init__(self, mailAuth, passAuth):
        self.mailAuth = mailAuth
        self.passAuth = passAuth
        self.DB_USER_AUTH = 'MCTHAIDP.MC1.USER_AUTH'

    def sha256Auth(self):
        return sha256(self.passAuth.encode('utf-8')).hexdigest()

    # Module log-in
    def addUserAuth(self):
        _passAuth = self.sha256Auth()
        sql = """
            INSERT INTO """+self.DB_USER_AUTH+"""( USER_MAIL, PASSWORD)
            VALUES('"""+self.mailAuth+"""', '"""+_passAuth+"""');
        """
        run_query(sql)

    def checkAuth(self):
        _passAuth = self.sha256Auth()
        sql = """
            SELECT USER_MAIL FROM """+self.DB_USER_AUTH+"""
            WHERE USER_MAIL='"""+self.mailAuth+"""' AND PASSWORD='"""+_passAuth+"""';
        """
        if run_query(sql):
            return 1
        else:
            return 0

    def checkSignUp(self):
        sql = """
            SELECT USER_MAIL FROM """+self.DB_USER_AUTH+"""
            WHERE USER_MAIL='"""+self.mailAuth+"""';
        """
        if run_query(sql):
            return True
        else:
            return False

    # def changePwAuth(mailAuth, passAuth):
    #     return 1

# class ClName():
#     def __init__(self, mail):
#         self.arg = mail
#     def get2(self):
#         return "yes22"


# authentication step 2: check mail user
class PermistionAuth:
    def __init__(self, mailAuth):
        self.userUlive = 'MCTHAIDP.MC1.user_alive'
        self.tpyesList = ['profit', 'patch', 'store']
        # self.tpyesList = ['patch', 'profit', 'store']
        # self.tpyesList = ['store', 'patch', 'profit']
        self.mailAuth = mailAuth

    def checkAlive(self):
        for type in self.tpyesList:
            sql = """ SELECT """+ type +"""_name, """+ type +"""_email FROM """+ self.userUlive +""" WHERE """+ type +"""_email='"""+ self.mailAuth +"""' LIMIT 1; """
            resQuery = run_query(sql)
            if resQuery:
                # st.write("Found: ", sql)
                return resQuery[0][0]
            # st.write("Next: ", sql)


# def signup():
#     # mail ==
#     return 1
#
# def forgetPassword():
#     return 1
#
# def changePassword():
#     return 1
