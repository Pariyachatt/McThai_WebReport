import streamlit as st
from database.pass_auth import *

from backend.logins.verified_authen_parent import *


class VerifiedSignIn():
    def __init__(self, vuser, vpass):
        self.vuser = vuser.strip()
        self.vpass = vpass.strip()
        self.status = list()
        self.message = ''

        self.AuthenParent = verifiedAuthenParent(self.vuser, self.vpass)

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
            self.status.append(self.AuthenParent.emptyUserPass())
            self.checkEmailAuth()
        try:
            self.status.index(False)
            # st.write("Stop action!")
            return False
        except Exception as e:
            st.success('Login successful!', icon="✅")
            return True
