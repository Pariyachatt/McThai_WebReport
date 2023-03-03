import streamlit as st
from database.snf_auth_connect import *


# class ClName2():
#     def __init__(self, mail):
#         self.arg = mail
#     def get2(self):
#         return "yes"

class VerifiedSignUp():
    def __init__(self, user, newpass, confpass):
        self.user = user.strip()
        self.newpass = newpass.strip()
        self.confpass = confpass.strip()
        self.status = list()
        self.message = ''


    def matchPassword(self):
        status = False
        if self.newpass != self.confpass:
            self.message = "Password is mismatch!"
            st.error(self.message, icon="🚨")
        else:
            status = True
        self.status.append(status)
        # return True if self.status else False

    def digitPassword(self):
        status = False
        if len(self.newpass) <= 7:
            self.message = "Please new password must more then 8 digit."
            st.error(self.message, icon="🚨")
        elif len(self.confpass) <= 7:
            self.message = "Please confirm password more then 8 digit."
            st.error(self.message, icon="🚨")
        else:
            status = True
        self.status.append(status)

    def checkEmailSignUp(self):
        PAuth = PassAuth(self.user, self.newpass)
        if PAuth.checkSignUp():
            # self.status.append(PAuth.checkSignUp())
            self.status.append(False)
            self.message = "Your Email sign up aleady!"
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
            self.status.append(True)
            self.message = "Role '"+ resPeralive +"' detected and ready to apply."
            st.success(self.message, icon="✅")

            # st.write("PermiAuth.checkAlive(): ", PermiAuth.checkAlive())


    def actionVerify(self):
        self.matchPassword()
        self.digitPassword()
        self.checkEmailSignUp()
        self.checkPermistionAuth()

        try:
            self.status.index(False)
            # st.write("Stop action!")
        except Exception as e:
            # st.write("Save data.")
            st.success('Save successful!', icon="✅")
