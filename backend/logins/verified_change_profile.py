import streamlit as st
from database.snf_auth_connect import *
# from database.permistion_auth import *

class VerifiedChangeProfile():
    def __init__(self, cuser, cOldpass, cNpass, cConfpass):
        self.cuser = cuser.strip()
        self.cOldpass = cOldpass.strip()
        self.cNpass = cNpass.strip()
        self.cConfpass = cConfpass.strip()
        self.status = list()
        self.message = ''


        self.PAuthNew = PassAuth(self.cuser, self.cNpass)
        self.PAuthOld = PassAuth(self.cuser, self.cOldpass)

    # def matchPassword(self):
    #     status = False
    #     if self.fnpass != self.fcpass:
    #         self.message = "Password and Confirm Password dose not match."
    #         st.error(self.message, icon="🚨")
    #     else:
    #         status = True
    #     self.status.append(status)
    #
    # def digitPassword(self):
    #     status = False
    #     if len(self.fnpass) <= 7:
    #         self.message = "Please try between 'New password' 8 and 15 digit."
    #         st.error(self.message, icon="🚨")
    #     elif len(self.fcpass) <= 7:
    #         self.message = "Please try between 'Confirm password' 8 and 15 digit."
    #         st.error(self.message, icon="🚨")
    #     else:
    #         status = True
    #     self.status.append(status)
    #
    #
    # def chkUserHint(self):
    #     if self.PAuth.verifyUserHint(self.fhint):
    #         self.status.append(True)
    #     else:
    #         self.status.append(False)
    #         self.message = "An account Email or Hint incorrectly."
    #         st.warning(self.message, icon="⚠️")
    #
    # def digitHint(self):
    #     status = False
    #     if len(self.fhint) < 4:
    #         self.message = "Hint must equal 4 digit."
    #         st.error(self.message, icon="🚨")
    #     elif self.fhint.isnumeric() == False:
    #         self.message = "Insert with Hint number only."
    #         st.error(self.message, icon="🚨")
    #     else:
    #         status = True
    #     self.status.append(status)

    def checkOldPassowd(self):
        st.write(self.cOldpass)

    def actionVerify(self):
        with st.spinner('Verifying...'):
            # self.matchPassword()
            # self.digitPassword()
            # self.chkUserHint()
            # self.digitHint()
            self.checkOldPassowd()

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
