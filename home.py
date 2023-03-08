import streamlit as st
# from streamlit_cookies_manager import EncryptedCookieManager
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

from frontend.net_sales_report import *
# from backend.cookies_login import *
from backend.logins.cookies_login import *

# from verified_signup import *
# from backend.verified_signup import *
from backend.logins.verified_signup import *
from backend.logins.verified_signin import *

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
# Action login


# optional
# def ck_callback():
#     st.write("You searched for:", st.session_state.input)
#     # return st.session_state.input
#     if st.session_state.input == "111":
#         st.session_state.input2 = "2022"

if not st.session_state.page:
    with ph.container():
        # st.header("This is page 1")
        # st.button("Go to page 2",on_click=nextPage)
        st.title('User Authentication.')
        email = st.text_input("Email",'Borompong.Phairatphiboon@th.mcd.com')
        password = st.text_input("Password", type="password")

        # optional
        # st.text_input("Test widget", placeholder='Life of Brian', key='input', on_change=ck_callback)
        # if 'input2' in st.session_state:
        #     st.write("You searched for2:", st.session_state.input2)

        actionLogin = st.button("LOG IN")
        if actionLogin:
            VerifiedSignIn = VerifiedSignIn(email, password)
            VerifiedSignIn.actionVerify()

            # CkLogin.updateTimeCookiesAlive()
            # login_bnt()



        with st.expander("FORGET PASSWORD"):
            components.html("""<hr>""",height=30)
            confEmail = st.text_input("Confirm Email")
            oldPass = st.text_input("Old Password", type="password", max_chars=15)
            newPass = st.text_input("New Password", type="password", max_chars=15)
            ConfPass = st.text_input("Confirm Password", type="password", max_chars=15)
            actionConfirm = st.button("Confirm")
        with st.expander("SIGN UP"):
            components.html("""<hr>""",height=30)

            # email exist
            # suEmail = st.text_input("Your Email",'Borompong.Phairatphiboon@th.mcd.com')

            # not Found
            # suEmail = st.text_input("Your Email",'Krisana.Charoensirinukul@th.mcd.com',placeholder='mail@domain.com')
            suEmail = st.text_input("Your Email",'Borompong.Phairatphiboon@th.mcd.com',placeholder='mail@domain.com')

            suPass = st.text_input("Enter Password",'11111111', type="password", placeholder='Insert 8 and 15 digit.', max_chars=15)
            suConfPass = st.text_input("Enter Confirm Password",'11111111', type="password",placeholder='Insert 8 and 15 digit', max_chars=15)
            suHint = st.text_input("Enter Hint",'1111', max_chars=4, placeholder='abcd')

            actionLogin = st.button("SIGN UP")

            if actionLogin:
                VerSignup = VerifiedSignUp(suEmail,suPass,suConfPass,suHint)
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
            CkLogin.destroyTimeCookiesAlive()
            logout_bnt()
        if selected == 'Net Sales Report':
            # st.session_state.page_detail = 'welcome'
            st.session_state.page_detail = 'Net_Sales_Report'


if st.session_state.page_detail == 'Net_Sales_Report':
    netSalesReport()
