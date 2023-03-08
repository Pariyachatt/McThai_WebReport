import streamlit as st
from database.snf_auth_connect import *

class VerifiedForgot():
    def __init__(self, fuser, fhint, fnpass, fcpass):
        self.fuser = fuser.strip()
        self.fhint = fhint.strip()
        self.fnpass = fnpass.strip()
        self.fcpass = fcpass.strip()
        self.status = list()
        self.message = ''
        self.PAuth = PassAuth(self.fuser, self.fnpass)

    def matchPassword(self):
        status = False
        if self.fnpass != self.fcpass:
            self.message = "Password and Confirm Password dose not match."
            st.error(self.message, icon="🚨")
        else:
            status = True
        self.status.append(status)

    def digitPassword(self):
        status = False
        if len(self.fnpass) <= 7:
            self.message = "Please try between 'New password' 8 and 15 digit."
            st.error(self.message, icon="🚨")
        elif len(self.fcpass) <= 7:
            self.message = "Please try between 'Confirm password' 8 and 15 digit."
            st.error(self.message, icon="🚨")
        else:
            status = True
        self.status.append(status)



    # def checkEmailSignUp(self):
    #     PAuth = PassAuth(self.user, self.newpass)
    #     if PAuth.checkSignUp():
    #         self.status.append(False)
    #         self.message = "An account with Email already exists."
    #         st.warning(self.message, icon="⚠️")
    #     else:
    #         self.status.append(True)


    def chkUserHint(self):
        if self.PAuth.verifyUserHint(self.fhint):
            self.status.append(True)
        else:
            self.status.append(False)
            self.message = "An account Email or Hint incorrectly."
            st.warning(self.message, icon="⚠️")

    def digitHint(self):
        status = False
        if len(self.fhint) < 4:
            self.message = "Hint must equal 4 digit."
            st.error(self.message, icon="🚨")
        elif self.fhint.isnumeric() == False:
            self.message = "Insert with Hint number only."
            st.error(self.message, icon="🚨")
        else:
            status = True
        self.status.append(status)

    def actionVerify(self):
        with st.spinner('Verifying...'):
            self.matchPassword()
            self.digitPassword()
            self.chkUserHint()
            self.digitHint()

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
