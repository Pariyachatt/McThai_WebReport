import streamlit as st
from database.pass_auth import *
from backend.logins.verified_authen_parent import *

class VerifiedChangeHint():
    def __init__(self, cUser, cOldHint, cNewHint):
        self.cuser = cUser.strip()
        self.cOldHint = cOldHint.strip()
        self.cNewHint = cNewHint.strip()
        self.status = list()
        self.message = ''

        self.AuthenParent = verifiedAuthenParent(self.cuser, 'False')
        self.PAuth = PassAuth(self.cuser, 'False')

    def checkOldHint(self):
        status = False
        ckOldHint = self.PAuth.verifyOldHint(self.cOldHint)
        if ckOldHint[0][0] <= 0:
            self.message = "Old Hint incorrect!"
            st.error(self.message, icon="🚨")
        else:
            status = True
        self.status.append(status)

    def actionVerify(self):
        self.status.append(self.AuthenParent.digitHint(self.cOldHint, "Old"))
        self.status.append(self.AuthenParent.digitHint(self.cNewHint, "New"))
        self.checkOldHint()
        try:
            self.status.index(False)
        except Exception as e:
            _changeHint = self.PAuth.changeHint(self.cNewHint)
            if _changeHint == 'done':
                st.success('Save successful!', icon="✅")
            else:
                st.error(_resetPW, icon="🚨")
