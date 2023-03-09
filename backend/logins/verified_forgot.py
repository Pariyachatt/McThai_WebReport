import streamlit as st
from database.pass_auth import *

from backend.logins.verified_authen_parent import *

class VerifiedForgot():
    def __init__(self, fuser, fhint, fnpass, fcpass):
        self.fuser = fuser.strip()
        self.fhint = fhint.strip()
        self.fnpass = fnpass.strip()
        self.fcpass = fcpass.strip()
        self.status = list()
        self.message = ''

        self.PAuth = PassAuth(self.fuser, self.fnpass)
        self.AuthenParent = verifiedAuthenParent(self.fuser, self.fnpass, self.fcpass)

    def chkUserHint(self):
        if self.PAuth.verifyUserHint(self.fhint):
            self.status.append(True)
        else:
            self.status.append(False)
            self.message = "An account Email or Hint incorrectly."
            st.warning(self.message, icon="⚠️")

    def actionVerify(self):
        with st.spinner('Verifying...'):
            self.status.append(self.AuthenParent.matchPassword())
            self.status.append(self.AuthenParent.digitHint(self.fhint))
            self.status.append(self.AuthenParent.digitPassword())
            self.chkUserHint()
        try:
            self.status.index(False)
            # st.write("Stop action!")
        except Exception as e:
            # st.success('Save successful!', icon="✅")
            _resetPW = self.PAuth.resetPassword(self.fhint)
            if _resetPW == 'done':
                st.success('Save successful!', icon="✅")
            else:
                st.error(_resetPW, icon="🚨")
