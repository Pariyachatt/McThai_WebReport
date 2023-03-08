import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from streamlit_autorefresh import st_autorefresh

from frontend.net_sales_report import *
from frontend.profile_setting import *

from backend.logins.cookies_login import *
from database.permistion_auth import *
from backend.logins.verified_signup import *
from backend.logins.verified_signin import *
from backend.logins.verified_forgot import *

# addition packet
# pip install streamlit-option-menu

# Pages logic
if 'page' not in st.session_state: st.session_state.page = 0
if 'page_detail' not in st.session_state: st.session_state.page_detail = "none"

def login_bnt():
    st.session_state.page = True
def logout_bnt():
    st.session_state.page = False
    st.session_state.page_detail = "none"

CkLogin = CookiesLogin()
c_remaining =  CkLogin.cookiesRemaining()['cookies_remaining']
if c_remaining < 0:
    st.session_state.page = False
else:
    st.session_state.page = True

# # DEBUG:
st.write("st.session_state.page: ", st.session_state.page)

ph = st.empty()
if not st.session_state.page:
    with ph.container():

        # Action login
        st.title(':lock_with_ink_pen: User Authentication.')

        email = st.text_input("Email",'Borompong.Phairatphiboon@th.mcd.com')
        password = st.text_input("Password", type="password", max_chars=15)

        # optional
        # st.text_input("Test widget", placeholder='Life of Brian', key='input', on_change=ck_callback)
        # if 'input2' in st.session_state:
        #     st.write("You searched for2:", st.session_state.input2)

        actionLogin = st.button("LOG IN")
        if actionLogin:
            VerifiedSignIn = VerifiedSignIn(email, password)
            if VerifiedSignIn.actionVerify():
                CkLogin.updateTimeCookiesAlive()
                login_bnt()
                countRef = st_autorefresh(interval=2000, limit=3)
                # st.write("countRef: ", countRef)
        components.html("""<hr align="center" width="90%">""", height=50 )

        ## FORGOT PASSWORD
        with st.expander("FORGOT PASSWORD"):
            components.html("""<hr>""",height=30)
            fgEmail = st.text_input("Email", placeholder='name@web.com')
            fgHint = st.text_input("Enter Hint",'1111', max_chars=4, placeholder='Insert 4-digit.')
            fgNewPass = st.text_input("New Password", type="password", max_chars=15)
            fgConfPass = st.text_input("Confirm Password", type="password", max_chars=15)

            actionConfirm = st.button("Confirm")
            if actionConfirm:
                VerifiedForgot = VerifiedForgot(fgEmail, fgHint, fgNewPass, fgConfPass)
                VerifiedForgot.actionVerify()

        ## SIGN UP
        with st.expander("SIGN UP"):
            components.html("""<hr>""",height=30)
            suEmail = st.text_input("Your Email",'Borompong.Phairatphiboon@th.mcd.com',placeholder='mail@domain.com')
            suPass = st.text_input("Enter Password",'11111111', type="password", placeholder='Insert 8 and 15 digit.', max_chars=15)
            suConfPass = st.text_input("Enter Confirm Password",'11111111', type="password",placeholder='Insert 8 and 15 digit', max_chars=15)
            suHint = st.text_input("Enter Hint", value=1111, max_chars=4)
            actionLogin = st.button("SIGN UP")

            if actionLogin:
                VerSignup = VerifiedSignUp(suEmail,suPass,suConfPass,suHint)
                VerSignup.actionVerify()

# show menu left
elif st.session_state.page:
    with st.sidebar:
        selected = option_menu("Web Reports", ["Net Sales Report",'Profile','Logout'],
            icons=['card-checklist', 'person','power'], menu_icon="bi-house-door-fill", default_index=0)
        selected
        if selected == 'Logout':
            CkLogin.destroyTimeCookiesAlive()
            logout_bnt()
            st_autorefresh(interval=2000, limit=3)
        elif selected == 'Net Sales Report':
            # st.session_state.page_detail = 'welcome'
            st.session_state.page_detail = 'Net_Sales_Report'
        elif selected == 'Profile':
            st.session_state.page_detail = 'ProfileSetting'
            username =  CkLogin.getProfile()['username_prof']
            st.session_state.user = username
            PerAuth = PermistionAuth(username)
            st.session_state.role = PerAuth.checkAlive()


if st.session_state.page_detail == 'Net_Sales_Report':
    netSalesReport()
elif st.session_state.page_detail == 'ProfileSetting':
    ProfileSetting = ProfileSetting()
    ProfileSetting.actionProfileUi()
