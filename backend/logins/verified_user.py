import os
import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager #pip install streamlit_cookies_manager
from datetime import datetime, timedelta
from tzlocal import get_localzone # pip install tzlocal
#pip install streamlit_cookies_manager

# from database.db_snowflake import *
# from function.logins.snf_auth_connect import *

class CookiesLogin:
    def __init__(self):
        self.cookies = EncryptedCookieManager(
            prefix="localhost/",
            password='changeme'
        )

        if 'cookies_set' not in self.cookies.keys():
            self.cookies["cookies_set"]  = "True"
            self.cookies["sign_status"] = "login"
            # # self.cookies["sign_status"] = "signup"
            self.cookies["username"] = ""
            self.cookies["time_cookies_alive"] = "0"
            self.cookies["time_cookies_start"] = str(datetime.now())
            self.cookies.save()
        if not self.cookies.ready():
            # Wait for the component to load and send us current cookies.
            st.stop()

    def test(self):
        return self.cookies["time_cookies_start"]

    """
    ## Sign in Fucntion
    if View == True && user_auth == True && password == True:
        -- User login/authentication is successful.
    if View == True && user_auth == True && password == False:
        -- Password Incorrect!.
    if View == False && user_auth == False
        -- Username Incorrect/Not authorized!.
    if View == True && user_auth == False
        -- Please Sign Up.
    if login_failed == 3:
        -- hold button login

    # Sign Up
    if View == False || AD == False:
        -- Your Email@ssci.com is Not authorized.
    if View == True || AD == True:
        -- add password to table
    if hint != 4:
        -- plase add hint  4 digit
    if pass < 8:
        -- please add 8 digit
    Ddd hint 4 digit number
        veriry by

    # Change password
    if  user_auth == False
        -- Username Incorrect
    if  Old-pass == False
        -- Old password Incorrect
    if  new-password != confirm-password
        -- confirm password mismatch.
    if  user_auth == True &&  Old-pass  == True && (new-password != confirm-password)
        -- update new password successful.

    # Forgot password -- On-hold
        -- veriry by hint 4 digit number

    # Update/Edit profile




    """
    # def cookiesRemaining():
    #     # gobal_cookies =  globalCookies()
    #     gobal_cookies = cookies
    #     cookies_expiry_info = dict()
    #     if gobal_cookies["time_cookies_start"]:
    #         # 2023-02-21 14:01:44.161458
    #         time_cookies_alive = int(gobal_cookies["time_cookies_alive"])
    #         str_timestamp = gobal_cookies["time_cookies_start"]
    #         date_format_str = '%Y-%m-%d %H:%M:%S.%f'
    #         datetime_start = datetime.strptime(str_timestamp, date_format_str)
    #         datetime_end = datetime_start + timedelta(hours=time_cookies_alive)
    #
    #         cookies_remaining = (datetime_end - datetime.now()).total_seconds() / 60
    #         cookies_quota = (datetime_end - datetime_start).total_seconds() / 60 #minutes_diff
    #
    #         # st.write("Welcome: ", cookies["username"])
    #         # st.write("cookies_remaininga: ", cookies_remaining)
    #         # st.write("cookies_quota: ", cookies_quota)
    #         cookies_expiry_info['cookies_remaining'] = cookies_remaining
    #         cookies_expiry_info['cookies_quota'] = cookies_quota
    #     return cookies_expiry_info


#
# def funcLogin():
#     st.set_page_config(initial_sidebar_state="collapsed")
#     with open('./css/style.css') as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
#     st.markdown(
#         """
#         <style>
#             [data-testid="collapsedControl"] {
#                 display: none
#             }
#             [data-testid="stSidebar"] {
#                 display: none
#             }
#             .css-1z8u7d{
#                 background-color: #fff;
#                 border: 0px
#             }
#             .css-k008qs {
#                 text-align: center;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )
#
#     if cookies["time_cookies_start"]:
#         ckr_list = cookiesRemaining()
#         cookies_remaining = ckr_list['cookies_remaining']
#         cookies_quota = ckr_list['cookies_quota']
#
#         # Debug
#         st.write("Welcome: ", cookies["username"])
#         st.write("cookies_remaining: ", cookies_remaining)
#         st.write("cookies_quota: ", cookies_quota)
#         st.write("sign_status:----- ", cookies["sign_status"])
#
#         # if int(cookies_remaining) <= 118: # test
#         if int(cookies_remaining) <= 0: # production
#             cookies["time_cookies_alive"] = "0"
#             st.write("time_cookies_alive reset:", cookies["time_cookies_alive"])
#             cookies.save()
#
#     def OnLogin():
#         if (email == "" ):
#             st.error('Email is empty.')
#             return 0
#         if (password == ""):
#             st.error('Password is empty.')
#             return 0
#         PAuth = PassAuth(email, password)
#         PermAuth = PermistionAuth(email)
#         # check username and password
#         if PAuth.checkAuth():
#             st.success('Login successful!', icon="✅")
#         else:
#             # Check Email username on the view table "Alive to SignUp"
#             if PermAuth.checkAlive() and PAuth.checkSignUp() != 1:
#                 st.warning('Please click Button Sign Up.', icon="⚠️")
#                 st.form_submit_button("SIGN UP")
#             else:
#                 st.warning('Username or Password Incorrect.', icon="⚠️")
#
#     # placeholder = st.empty()
#     with placeholder.form("login"):
#         st.header("Login")
#         email = st.text_input("Email", cookies["username"])
#         password = st.text_input("Password", type="password")
#
#         actionLogin = st.form_submit_button("LOG IN")
#         if actionLogin:
#             OnLogin()
#             cookies["sign_status"] = "signup"
#             # st.session_state.runpage = main_page
#             # st.experimental_rerun()
#             # if OnLogin() == 2:
#             #     placeholder.empty()
#             #     uiSignUp()
#         cookies["username"] = 'Suthathip.Thepthoranee@th.mcd.com'
#         # cookies["time_cookies_alive"] = "2"  #s Hours
#         # cookies["time_cookies_start"] = str(datetime.now())
#
#
#
# def statusCookies():
#     ckr_list = cookiesRemaining()
#     cookies_remaining = ckr_list['cookies_remaining']
#     cookies_quota = ckr_list['cookies_quota']
#
#     if int(cookies_remaining) <= 0:
#         return True
#     else:
#         return False
#
# def signStatus():
#     gobal_cookies = cookies
#     if gobal_cookies["sign_status"] == 'login':
#         return True
#     else:
#         return False
