import streamlit as st
from database.snf_auth_connect import *
from database.permistion_auth import *


class VerifiedSignIn():
    def __init__(self, user, pass):
        self.user = user.strip()
        self.pass = pass.strip()
        self.status = list()
        self.message = ''

    def emptyUserPass(self):
        status = False
        if len(self.user) <= 0:
            self.message = "Please insert you email."
            st.error(self.message, icon="🚨")
        elif len(self.pass) <= 0:
            self.message = "Please insert you password."
            st.error(self.message, icon="🚨")
        else:
            status = True
        self.status.append(status)

    def checkEmailAuth(self):
        # check:  AD ->  table auth
        PAuth = PassAuth(self.user, self.newpass)
        if PAuth.checkSignUp():
        # if PAuth.checkSignUp(True):
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
        self.emptyUserPass()
        # self.checkEmailSignUp()
        # self.digitHint()
        # self.checkPermistionAuth()

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
