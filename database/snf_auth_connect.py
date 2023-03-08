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
        self.DBSnowflake = DBSnowflake()
        # self.snfconn = DBSnowflake().conn

    def sha256Auth(self):
        return sha256(self.passAuth.encode('utf-8')).hexdigest()

    def addUserAuth(self, hint):
        _passAuth = self.sha256Auth()
        sql = """INSERT INTO """+self.DB_USER_AUTH+"""( USER_MAIL, PASSWORD, hint)VALUES('"""+self.mailAuth+"""', '"""+_passAuth+"""', '"""+hint+"""');"""

        #debug
        # sql = """INSERT INTO """+self.DB_USER_AUTH+"""( USER_MAIL, PASSWORD, hint)VALUES('"""+self.mailAuth+"""', '"""+_passAuth+"""', 11111111);"""
        return self.DBSnowflake.run_insert(sql)

    def checkAuth(self):
        _passAuth = self.sha256Auth()
        sql = """
            SELECT USER_MAIL FROM """+self.DB_USER_AUTH+"""
            WHERE USER_MAIL='"""+self.mailAuth+"""' AND PASSWORD='"""+_passAuth+"""';
        """
        if self.DBSnowflake.run_query(sql):
            return 1
        else:
            return 0

    def checkSignUp(self, debug=False):
        sql = """
            SELECT USER_MAIL FROM """+self.DB_USER_AUTH+"""
            WHERE USER_MAIL='"""+self.mailAuth+"""';
        """
        if debug:
            st.write("SQL checkSignUp: ",sql)
        if self.DBSnowflake.run_query(sql):
            return True
        else:
            return False
