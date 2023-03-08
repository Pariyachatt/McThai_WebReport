import streamlit as st
from database.snf_auth_connect import *
# from database.permistion_auth import *


class VerifiedSignIn():
    def __init__(self, vuser, vpass):
        self.vuser = vuser.strip()
        self.vpass = vpass.strip()
        self.status = list()
        self.message = ''

    def emptyUserPass(self):
        status = False
        if len(self.vuser) <= 0:
            self.message = "Please insert you email."
            st.error(self.message, icon="🚨")
        elif len(self.vpass) <= 0:
            self.message = "Please insert you password."
            st.error(self.message, icon="🚨")
        else:
            status = True
        self.status.append(status)

    def checkEmailAuth(self):
        # check:  AD ->  table auth
        PAuth = PassAuth(self.vuser, self.vpass)
        if PAuth.checkAuth():
            self.status.append(True)
        else:
            self.status.append(False)
            self.message = "Username or Password incorrect!"
            st.warning(self.message, icon="⚠️")

    def actionVerify(self):
        with st.spinner('Verifying...'):
            self.emptyUserPass()
            self.checkEmailAuth()
        try:
            self.status.index(False)
            # st.write("Stop action!")
        except Exception as e:
            st.success('Login successful!', icon="✅")
