import os
import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager #pip install streamlit_cookies_manager
from datetime import datetime, timedelta
from tzlocal import get_localzone # pip install tzlocal

#pip install streamlit_cookies_manager

def FuncLogin():
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

    # This should be on top of your script
    cookies = EncryptedCookieManager(
        # This prefix will get added to all your cookie names.
        # This way you can run your app on Streamlit Cloud without cookie name clashes with other apps.
        prefix="localhost/",
        #prefix="",   # no prefix will show all your cookies for this domain
        # You should setup COOKIES_PASSWORD secret if you're running on Streamlit Cloud.
        #password=os.environ.get("COOKIES_PASSWORD", "My secret password"),
        password='changeme'
    )

    if not cookies.ready():
        # Wait for the component to load and send us current cookies.
        st.stop()


    if 'cookies_set' not in cookies.keys():
        cookies["cookies_set"] = "True"
        cookies["username"] = ""
        cookies["time_cookies_alive"] = "0"
        cookies["time_cookies_start"] = ""
        cookies.save()

    # if int(cookies["time_cookies_alive"]) == 0:
    #     username = st.text_input("Username", cookies["username"])
    #     Password = st.text_input("Password")
    #     if st.button("Login"):
    #         cookies["username"] = username  # This will get saved on next rerun
    #         cookies["time_cookies_alive"] = "2"  # Hours
    #         cookies["time_cookies_start"] = str(datetime.now())  # This will get saved on next rerun
    # else:
    #     if st.button("Logout"):
    #         cookies["time_cookies_alive"] = "0"
    #         st.refresh()

    if cookies["time_cookies_start"]:
        # 2023-02-21 14:01:44.161458
        time_cookies_alive = int(cookies["time_cookies_alive"])
        str_timestamp = cookies["time_cookies_start"]
        date_format_str = '%Y-%m-%d %H:%M:%S.%f'
        datetime_start = datetime.strptime(str_timestamp, date_format_str)
        datetime_end = datetime_start + timedelta(hours=time_cookies_alive)

        cookies_remaining = (datetime_end - datetime.now()).total_seconds() / 60
        cookies_quota = (datetime_end - datetime_start).total_seconds() / 60 #minutes_diff

        st.write("Welcome: ", cookies["username"])
        st.write("cookies_remaininga: ", cookies_remaining)
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

    # return cookies

def statusCookies():
    cookies = EncryptedCookieManager(
        prefix="localhost/",
        password='changeme'
    )
    cookies_chk = FuncLogin()

    cookies_remaining = (datetime_end - datetime.now()).total_seconds() / 60
    if int(cookies_remaining) <= 0: or int(cookies_chk["time_cookies_alive"]) == 0:
        return True
    else:
        return False






st.write("cookies_quota: ", cookies["time_cookies_alive"])
