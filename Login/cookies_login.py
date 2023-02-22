import os
import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager #pip install streamlit_cookies_manager
from datetime import datetime, timedelta
from tzlocal import get_localzone # pip install tzlocal
#pip install streamlit_cookies_manager

cookies = EncryptedCookieManager(
    prefix="localhost/",
    password='changeme'
)
if 'cookies_set' not in cookies.keys():
    cookies["cookies_set"] = "True"
    cookies["username"] = ""
    cookies["time_cookies_alive"] = "0"
    cookies["time_cookies_start"] = ""
    cookies.save()
if not cookies.ready():
    # Wait for the component to load and send us current cookies.
    st.stop()

def cookiesRemaining():
    # gobal_cookies =  globalCookies()
    gobal_cookies = cookies
    cookies_expiry_info = dict()
    if gobal_cookies["time_cookies_start"]:
        # 2023-02-21 14:01:44.161458
        time_cookies_alive = int(gobal_cookies["time_cookies_alive"])
        str_timestamp = gobal_cookies["time_cookies_start"]
        date_format_str = '%Y-%m-%d %H:%M:%S.%f'
        datetime_start = datetime.strptime(str_timestamp, date_format_str)
        datetime_end = datetime_start + timedelta(hours=time_cookies_alive)

        cookies_remaining = (datetime_end - datetime.now()).total_seconds() / 60
        cookies_quota = (datetime_end - datetime_start).total_seconds() / 60 #minutes_diff

        # st.write("Welcome: ", cookies["username"])
        # st.write("cookies_remaininga: ", cookies_remaining)
        # st.write("cookies_quota: ", cookies_quota)
        cookies_expiry_info['cookies_remaining'] = cookies_remaining
        cookies_expiry_info['cookies_quota'] = cookies_quota
    return cookies_expiry_info

def funcLogin():
    st.set_page_config(initial_sidebar_state="collapsed")
    with open('./css/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.markdown(
        """
        <style>
            [data-testid="collapsedControl"] {
                display: none
            }
            [data-testid="stSidebar"] {
                display: none
            }
            .css-1z8u7d{
                background-color: #fff;
                border: 0px
            }
            .css-k008qs {
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if cookies["time_cookies_start"]:
        ckr_list = cookiesRemaining()
        cookies_remaining = ckr_list['cookies_remaining']
        cookies_quota = ckr_list['cookies_quota']

        # Debug
        st.write("Welcome: ", cookies["username"])
        st.write("cookies_remaining: ", cookies_remaining)
        st.write("cookies_quota: ", cookies_quota)

        # if int(cookies_remaining) <= 118: # test
        if int(cookies_remaining) <= 0: # production
            cookies["time_cookies_alive"] = "0"
            st.write("time_cookies_alive reset:", cookies["time_cookies_alive"])
            cookies.save()
    def OnLogin():
        if (email == "" or password == ""):
            st.error('Email or Password Incorrect.')
    with st.form("my_form"):
        st.header("Login")
        email = st.text_input("Email", cookies["username"])
        password = st.text_input("Password", type="password")
        if st.form_submit_button("LOG IN", on_click=OnLogin):
            cookies["username"] = email  # This will get saved on next rerun
            cookies["time_cookies_alive"] = "2"  # Hours
            cookies["time_cookies_start"] = str(datetime.now())

def statusCookies():
    ckr_list = cookiesRemaining()
    cookies_remaining = ckr_list['cookies_remaining']
    cookies_quota = ckr_list['cookies_quota']

    if int(cookies_remaining) <= 0:
        return True
    else:
        return False
