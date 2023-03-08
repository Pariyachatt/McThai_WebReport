import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from backend.logins.verified_change_profile import *


class ProfileSetting:
    def __init__(self):
        self.userCurrent = st.session_state.user
        st.title("Profile Setting.")
        components.html("""<hr align="center" width="100%">""", height=10 )
        st.metric(label="", value="Email", delta=st.session_state.user)
        st.metric(label="", value="Role", delta=st.session_state.role)

    def changePasswordUI(self):
        with st.expander("CHANGE YOUR PASSWORD"):
            components.html("""<hr>""",height=30)
            cOldPass = st.text_input("Old Password", type="password", max_chars=15)
            cNewPass = st.text_input("New Password", type="password", max_chars=15)
            cConfPass = st.text_input("Confirm Password", type="password", max_chars=15)
            if st.button("UPDTAE PASSWORD"):
                VCProfile = VerifiedChangeProfile(self.userCurrent, cOldPass,cNewPass,cConfPass)
                VCProfile.checkOldPassowd()

        with st.expander("CHANGE YOUR HINT"):
            components.html("""<hr>""",height=30)
            cHint = st.text_input("Enter Hint", max_chars=4, placeholder='Insert 4-digit.')
            if st.button("UPDTAE HINT"):
                pass
    def actionProfileUi(self):
        self.changePasswordUI()
