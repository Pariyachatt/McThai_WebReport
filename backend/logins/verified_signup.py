import streamlit as st
from database.pass_auth import *
from database.permistion_auth import *

from backend.logins.verified_authen_parent import *

class VerifiedSignUp():
    def __init__(self, user, newpass, confpass, hint):
        self.user = user.strip()
        self.newpass = newpass.strip()
        self.confpass = confpass.strip()
        self.hint = hint.strip()
        self.status = list()
        self.message = ''

        self.AuthenParent = verifiedAuthenParent(self.user, self.newpass,self.confpass)

    def checkPermistionAuth(self):
        PermiAuth = PermistionAuth(self.user)
        resPeralive = PermiAuth.checkAlive()
        if resPeralive == None:
            self.status.append(False)
            self.message = "Your Email not authorized!"
            st.error(self.message, icon="🚨")
        else:
            self.status.append(True)

    def actionVerify(self):
        with st.spinner('Verifying...'):
            self.checkPermistionAuth()
            self.status.append(self.AuthenParent.matchPassword())
            self.status.append(self.AuthenParent.digitPassword())
            self.status.append(self.AuthenParent.checkEmailSignUp())
            self.status.append(self.AuthenParent.digitHint(self.hint))
        try:
            self.status.index(False)
        except Exception as e:
            # Send "mail pass hint" to save.
            PAuth = PassAuth(self.user, self.newpass)
            _resAddUser = PAuth.addUserAuth(self.hint)
            # Python sql return done
            if _resAddUser == 'done':
                st.success('Save successful!', icon="✅")
            else:
                st.error(_resAddUser, icon="🚨")
