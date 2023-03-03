import streamlit as st
# from streamlit_cookies_manager import EncryptedCookieManager
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

from Net_Sales_Report import *
from welcome import *
from function.logins.cookies_login import *
from function.logins.verified_signup import *

# Pages logic
if 'page' not in st.session_state: st.session_state.page = 0
if 'page_detail' not in st.session_state: st.session_state.page_detail = "none"

def login_bnt():
    st.session_state.page = True
def logout_bnt():
    st.session_state.page = False
    st.session_state.page_detail = "none"

CLogin = CookiesLogin()
c_remaining =  CLogin.cookiesRemaining()['cookies_remaining']
if c_remaining < 0:
    st.session_state.page = False
else:
    st.session_state.page = True

# # DEBUG:
st.write("st.session_state.page: ", st.session_state.page)

ph = st.empty()
# Action login
if not st.session_state.page:
    with ph.container():
        # st.header("This is page 1")
        # st.button("Go to page 2",on_click=nextPage)
        st.title('User Authentication.')
        email = st.text_input("Email",'suwit@ssci.co.th')
        password = st.text_input("Password", type="password")
        actionLogin = st.button("LOG IN")
        if actionLogin:
            CLogin.updateTimeCookiesAlive()
            login_bnt()

        with st.expander("FORGET PASSWORD"):
            components.html("""<hr>""",height=30)
            confEmail = st.text_input("Confirm Email")
            oldPass = st.text_input("Old Password", type="password")
            newPass = st.text_input("New Password", type="password")
            ConfPass = st.text_input("Confirm Password", type="password")
            actionConfirm = st.button("Confirm")
        with st.expander("SIGN UP"):
            components.html("""<hr>""",height=30)
            suEmail = st.text_input("Your Email")
            suPass = st.text_input("Enter Password", type="password")
            suConfPass = st.text_input("Enter Confirm Password", type="password")
            actionLogin = st.button("SIGN UP")

            if actionLogin:
                VerSignup = VerifiedSignUp(suEmail,suPass,suConfPass)
                VerSignup.actionVerify()

# show menu left
elif st.session_state.page:
    with st.sidebar:
        # selected = option_menu("Web Reports", ["Net Sales Report", 'Settings','Logout'],
            # icons=['house', 'gear'], menu_icon="cast", default_index=0)
        selected = option_menu("Web Reports", ["Net Sales Report",'Logout'],
            icons=['house'], menu_icon="cast", default_index=0)
        selected
        if selected == 'Logout':
            CLogin.destroyTimeCookiesAlive()
            logout_bnt()
        if selected == 'Net Sales Report':
            # st.session_state.page_detail = 'welcome'
            st.session_state.page_detail = 'Net_Sales_Report'


if st.session_state.page_detail == 'Net_Sales_Report':
    netSalesReport()
