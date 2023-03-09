import streamlit as st
from database.pass_auth import *
# from database.permistion_auth import *

from backend.logins.verified_authen_parent import *

class VerifiedChangeProfile():
    def __init__(self, cuser, cOldpass, cNpass, cConfpass):
        self.cuser = cuser.strip()
        self.cOldpass = cOldpass.strip()
        self.cNpass = cNpass.strip()
        self.cConfpass = cConfpass.strip()
        self.status = list()
        self.message = ''

        self.AuthenParent = verifiedAuthenParent(self.cuser, self.cNpass, self.cConfpass)
        self.PAuthNew = PassAuth(self.cuser, self.cNpass)
        self.PAuthOld = PassAuth(self.cuser, self.cOldpass)

    def checkOldPassowd(self):
        status = False
        ckOldpw = self.PAuthOld.verifyOldPassowd()
        if ckOldpw[0][0] <= 0:
            self.message = "Old Password incorrect!"
            st.error(self.message, icon="🚨")
        else:
            status = True
        self.status.append(status)

    def actionVerify(self):
        self.status.append(self.AuthenParent.matchPassword())
        self.status.append(self.AuthenParent.digitPassword())
        self.checkOldPassowd()
        try:
            self.status.index(False)
        except Exception as e:
            _changePW = self.PAuthNew.changePassword()
            if _changePW == 'done':
                st.success('Save successful!', icon="✅")
            else:
                st.error(_resetPW, icon="🚨")
