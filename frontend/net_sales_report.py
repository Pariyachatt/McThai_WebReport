import streamlit as st
from database.db_snowflake import *
import datetime
from PIL import Image

from frontend.layouts.table_layout import *
from database.permistion_auth import *

class NetSalesReport:
    def __init__(self):
        self.Layouts = TableLayouts()
        self.PARole = PermistionAuth(st.session_state.user)

    def s_date_onchanged(self):
        st.session_state.max_date = ""
        st.session_state.max_date = st.session_state.s_date + datetime.timedelta(days=31)
        if st.session_state.s_date.year != st.session_state.max_date.year:
            st.session_state.max_date = datetime.datetime.strptime(
                str(st.session_state.s_date.year)+"/"+"12/31", "%Y/%m/%d")

    def loadPage(self):
        # Layouts = TableLayouts()
        # with open('./css/style.css') as f:
        #     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

        if 'max_date' not in st.session_state:
            st.session_state.max_date = datetime.datetime.now() + datetime.timedelta(days=31)
        if 'min_date' not in st.session_state:
            st.session_state.min_date = datetime.date(1, 1, 1)

        st.header("Net Sales Report")
        with st.container():
            container_header = st.columns(1)
            with container_header[0]:
                col_filter = st.columns([0.33, 0.33, 0.33], gap='small')

                status_role = True
                role_name = ""
                if st.session_state.role['role_type'] == 'PROFIT':
                    status_role = False
                    role_name = st.session_state.role['role_name']

                with col_filter[0]:
                    st.text_input("Profit Name", role_name, disabled=status_role)
                    s_date = st.date_input(
                        "Start Date", min_value=st.session_state.min_date, key='s_date', on_change=self.s_date_onchanged
                    )

                with col_filter[1]:
                    listPatchname = self.PARole.getPatchName(role_name)
                    optionsPatch = st.multiselect(
                        'Patch Name',
                        listPatchname, args=True)
                    # self.callbackReportGrid(role_name)
                    # st.write('You selected:', optionsPatch)
                    # st.text_input("Patch Name", disabled=True)
                    e_date = st.date_input(
                        "End Date", key='e_date', min_value=st.session_state.s_date, max_value=st.session_state.max_date, value=st.session_state.max_date
                    )
                with col_filter[2]:
                    st.text_input("Store code")
                    st.text_input("Store Name", disabled=True)
                #     s_date = st.date_input(
                #         "Start Date", min_value=st.session_state.min_date, key='s_date', on_change=self.s_date_onchanged
                #     )
                # with col_filter[3]:
                #     e_date = st.date_input(
                #         "End Date", key='e_date', min_value=st.session_state.s_date, max_value=st.session_state.max_date, value=st.session_state.max_date
                #     )
            col_btnS = st.columns(1)
            with col_btnS[0]:
                st.session_state.btn = st.button("Search")
        if st.session_state.btn:
            # st.write("st.session_state.s_date: "+ str(st.session_state.s_date))
            # st.write("st.session_state.e_date: "+str(st.session_state.e_date))
            with st.spinner('Loading...'):
                self.Layouts.reportGrid(st.session_state.s_date, st.session_state.e_date, role_name)

        if listPatchname:
            with st.spinner('Patch name to Loading...'):
                self.Layouts.reportGrid(st.session_state.s_date, st.session_state.e_date, role_name)
