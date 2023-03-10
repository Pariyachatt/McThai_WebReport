import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from backend.logins.verified_change_profile import *
from backend.logins.verified_change_hint import *


class ProfileSetting:
    def __init__(self):
        self.userCurrent = st.session_state.user
        st.title("Profile Setting.")
        components.html("""<hr align="center" width="100%">""", height=10 )
        st.metric(label="", value="Email", delta=st.session_state.user)
        st.metric(label="", value="Role Type", delta=st.session_state.role["role_type"])
        st.metric(label="", value="Role Name", delta=st.session_state.role["role_name"])

    def changePasswordUI(self):
        with st.expander("CHANGE YOUR PASSWORD"):
            components.html("""<hr>""",height=30)
            cOldPass = st.text_input("Old Password", type="password", max_chars=15)
            cNewPass = st.text_input("New Password", type="password", max_chars=15)
            cConfPass = st.text_input("Confirm Password", type="password", max_chars=15)
            if st.button("UPDTAE PASSWORD"):
                with st.spinner('Update...'):
                    VCProfile = VerifiedChangeProfile(self.userCurrent, cOldPass,cNewPass,cConfPass)
                    VCProfile.actionVerify()

        with st.expander("CHANGE YOUR HINT"):
            components.html("""<hr>""",height=30)
            cOldHint = st.text_input("Old Hint", max_chars=4, placeholder='Insert 4-digit.')
            cNewHint = st.text_input("New Hint", max_chars=4, placeholder='Insert 4-digit.')
            if st.button("UPDTAE HINT"):
                with st.spinner('Update...'):
                    VCHint = VerifiedChangeHint(self.userCurrent, cOldHint,cNewHint)
                    VCHint.actionVerify()
    def actionProfileUi(self):
        self.changePasswordUI()
