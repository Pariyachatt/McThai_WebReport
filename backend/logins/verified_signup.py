import streamlit as st
from database.snf_auth_connect import *
from database.permistion_auth import *


# class ClName2():
#     def __init__(self, mail):
#         self.arg = mail
#     def get2(self):
#         return "yes"

class VerifiedSignUp():
    def __init__(self, user, newpass, confpass, hint):
        self.user = user.strip()
        self.newpass = newpass.strip()
        self.confpass = confpass.strip()
        self.hint = hint.strip()
        self.status = list()
        self.message = ''


    def matchPassword(self):
        status = False
        if self.newpass != self.confpass:
            self.message = "Password and Confirm Password dose not match."
            st.error(self.message, icon="🚨")
        else:
            status = True
        self.status.append(status)
        # return True if self.status else False

    def digitPassword(self):
        status = False
        if len(self.newpass) <= 7:
            self.message = "Please try between 'New password'  8 and 15 digit."
            st.error(self.message, icon="🚨")
        elif len(self.confpass) <= 7:
            self.message = "Please try between 'Confirm password' 8 and 15 digit."
            st.error(self.message, icon="🚨")
        else:
            status = True
        self.status.append(status)

    def checkEmailSignUp(self):
        PAuth = PassAuth(self.user, self.newpass)
        if PAuth.checkSignUp():
        # if PAuth.checkSignUp(True):
            # self.status.append(PAuth.checkSignUp())
            self.status.append(False)
            self.message = "An account with Email already exists."
            st.warning(self.message, icon="⚠️")
        else:
            self.status.append(True)


    def checkPermistionAuth(self):
        PermiAuth = PermistionAuth(self.user)
        resPeralive = PermiAuth.checkAlive()
        if resPeralive == None:
            self.status.append(False)
            self.message = "Your Email not authorized!"
            st.error(self.message, icon="🚨")
        else:
            # if function retain username and password into tabel.
            self.status.append(True)
            # self.message = "Role '"+ resPeralive +"' detected and ready to apply."
            # st.success(self.message, icon="✅")

    def digitHint(self):
        status = False
        if len(self.hint) < 4:
            self.message = "Hint must equal 4 digit."
            st.error(self.message, icon="🚨")
        else:
            status = True
        self.status.append(status)

    def actionVerify(self):
        with st.spinner('Verifying...'):
            self.matchPassword()
            self.digitPassword()
            self.checkEmailSignUp()
            self.digitHint()
            self.checkPermistionAuth()

        try:
            self.status.index(False)
            # st.write("Stop action!")
        except Exception as e:
            PAuth = PassAuth(self.user, self.newpass)
            _resAddUser = PAuth.addUserAuth(self.hint)
            if _resAddUser == 'done':
                st.success('Save successful!', icon="✅")
            else:
                st.error(_resAddUser, icon="🚨")
