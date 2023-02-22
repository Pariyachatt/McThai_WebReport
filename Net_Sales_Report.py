import streamlit as st
from database.dbConfig import *
from layouts.Layouts import *
from Login.cookies_login import *
import datetime
import streamlit_nested_layout as sn
from PIL import Image


# Auth =  False
# Auth =  True
# if Auth:
if statusCookies():
    funcLogin()
    # st.write("xxxxxxxxxxxxxxx")
else:
    def main():
        st.set_page_config(
            page_title="Web Report",
            layout="wide",
            page_icon=None
        )

        # Debug
        ckr_list = cookiesRemaining()
        cookies_remaining = ckr_list['cookies_remaining']
        cookies_quota = ckr_list['cookies_quota']
        st.write("cookies_remaining: ", cookies_remaining)
        st.write("cookies_quota: ", cookies_quota)

        username_wel = cookies["username"]
        st.sidebar.title(f"Welcome : {username_wel}")
        if st.sidebar.button("Logout"):
            cookies["time_cookies_alive"] = "0"

        with open('./css/style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        if 'max_date' not in st.session_state:
            st.session_state.max_date = datetime.datetime.now() + datetime.timedelta(
                days=31)
        if 'min_date' not in st.session_state:
            st.session_state.min_date = datetime.date(1, 1, 1)
        def s_date_onchanged():
            st.session_state.max_date = ""
            st.session_state.max_date = st.session_state.s_date + datetime.timedelta(
                days=31)
            if st.session_state.s_date.year != st.session_state.max_date.year:
                st.session_state.max_date = datetime.datetime.strptime(
                    str(st.session_state.s_date.year)+"/"+"12/31", "%Y/%m/%d")
        st.header("Net Sales Report")
        with st.container():
            container_header = st.columns(1)
            with container_header[0]:
                col_filter = st.columns([0.20, 0.20, 0.30, 0.30], gap='small')

                with col_filter[0]:
                    st.text_input("Profit name", disabled=True)
                    st.text_input("Store code")
                with col_filter[1]:
                    st.text_input("Patch name", disabled=True)
                    st.text_input("Store name", disabled=True)
                with col_filter[2]:
                    s_date = st.date_input(
                        "Start Date", min_value=st.session_state.min_date, key='s_date', on_change=s_date_onchanged)
                with col_filter[3]:
                    e_date = st.date_input(
                        "End Date", key='e_date', min_value=st.session_state.s_date, max_value=st.session_state.max_date, value=st.session_state.max_date)
            col_btnS = st.columns(1)
            with col_btnS[0]:
                st.session_state.btn = st.button("Search")
        if st.session_state.btn:
            showReport(st.session_state.s_date, st.session_state.e_date)

if __name__ == "__main__":
    main()
