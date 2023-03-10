import os
import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager #pip install streamlit_cookies_manager
from datetime import datetime, timedelta
# from tzlocal import get_localzone # pip install tzlocal
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

    # def test(self):
    #     return self.cookies["time_cookies_start"]

    def cookiesRemaining(self):
        cookies_expiry_info = dict()
        if self.cookies["time_cookies_start"]:
            # 2023-02-21 14:01:44.161458
            time_cookies_alive = float(self.cookies["time_cookies_alive"])
            str_timestamp = self.cookies["time_cookies_start"]
            date_format_str = '%Y-%m-%d %H:%M:%S.%f'
            datetime_start = datetime.strptime(str_timestamp, date_format_str)
            datetime_end = datetime_start + timedelta(hours=time_cookies_alive)

            cookies_remaining = (datetime_end - datetime.now()).total_seconds() / 60
            cookies_quota = (datetime_end - datetime_start).total_seconds() / 60 #minutes_diff

            # DEBUG:
            st.write("Welcome: ", self.cookies["username"])
            st.write("cookies_remaininga: ", cookies_remaining)
            st.write("cookies_quota: ", cookies_quota)

            cookies_expiry_info['cookies_remaining'] = cookies_remaining
            cookies_expiry_info['cookies_quota'] = cookies_quota
        return cookies_expiry_info

    def getProfile(self):
        cookies_profile = dict()
        cookies_profile['username_prof'] = self.cookies["username"]
        return cookies_profile
        # return 'suwit------'

    def updateTimeCookiesAlive(self, mail):
        self.cookies["username"] = mail
        self.cookies["time_cookies_alive"] = "2"  #Hours
        self.cookies["time_cookies_start"] = str(datetime.now())

    def destroyTimeCookiesAlive(self):
        self.cookies["time_cookies_alive"] = "0"  #Hours
        self.cookies["time_cookies_start"] = str(datetime.now())
