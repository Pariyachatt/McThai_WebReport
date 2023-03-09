import streamlit as st
from database.pass_auth import *
 # from database.pass_auth import *

class verifiedAuthenParent():
    def __init__(self, aPuser, aPnPass, aPcPass="", aPoPass=""):
        self.aPuser = aPuser.strip()
        self.aPnPass = aPnPass.strip()
        self.aPcPass = aPcPass.strip()
        self.aPoPass = aPoPass.strip()
        self.status = list()
        self.message = ''

        self.PAuth = PassAuth(self.aPuser, self.aPnPass)

    def matchPassword(self):
        status = False
        if self.aPnPass != self.aPcPass:
            self.message = "Password and Confirm Password dose not match.--"
            st.error(self.message, icon="🚨")
        else:
            status = True
        return status

    def digitPassword(self):
        status = False
        if len(self.aPnPass) <= 7:
            self.message = "Please try between 'New password' 8 and 15 digit.--"
            st.error(self.message, icon="🚨")
        elif len(self.aPcPass) <= 7:
            self.message = "Please try between 'Confirm password' 8 and 15 digit.--"
            st.error(self.message, icon="🚨")
        else:
            status = True
        return status

    def emptyUserPass(self):
        status = False
        if len(self.aPuser) <= 0:
            self.message = "Please insert you email.--"
            st.error(self.message, icon="🚨")
        elif len(self.aPnPass) <= 0:
            self.message = "Please insert you password.--"
            st.error(self.message, icon="🚨")
        else:
            status = True
        return status

    def digitHint(self, hint, hint_current=""):
        status = False
        if len(hint) < 4:
            self.message = hint_current+" Hint must equal 4 digit.--"
            st.error(self.message, icon="🚨")
        elif hint.isnumeric() == False:
            self.message = "Insert with "+hint_current+" Hint number only.--"
            st.error(self.message, icon="🚨")
        else:
            status = True
        return status

    def checkEmailSignUp(self):
        if self.PAuth.checkSignUp():
            status = False
            self.message = "An account with Email already exists."
            st.warning(self.message, icon="⚠️")
        else:
            status = True
        return status



    #
    # def checkOldPassowd(self):
    #     status = False
    #     ckOldpw = self.PAuthOld.verifyOldPassowd()
    #     if ckOldpw[0][0] <= 0:
    #         self.message = "Old Password incorrect!"
    #         st.error(self.message, icon="🚨")
    #     else:
    #         status = True
    #     self.status.append(status)
