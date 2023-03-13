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

        st.write("Mail user: ",st.session_state.user)

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

                status_profit = True
                status_patch = True
                status_store = True
                # Default is all
                profit_search = ""
                patch_search = ""
                store_search = ""

                store_code_search = st.session_state.role['store_code']
                store_name_search = st.session_state.role['store_name']
                patch_search = st.session_state.role['patch_name']
                profit_search = st.session_state.role['profit_name']

                if st.session_state.role['role_type'] == 'PROFIT':
                    # status_profit = False
                    status_patch = False
                elif st.session_state.role['role_type'] == 'PATCH':
                    pass
                    status_store = False
                # elif st.session_state.role['role_type'] == 'STORE':
                #     # status_profit = False
                #     # status_patch = False
                #     # status_store = False
                #     pass

                with col_filter[0]:
                    # st.write("profit_search:", profit_search)
                    st.text_input("Profit Name", profit_search, disabled=status_profit)
                    s_date = st.date_input(
                        "Start Date", min_value=st.session_state.min_date, key='s_date', on_change=self.s_date_onchanged
                    )
                with col_filter[1]:
                    # listPatchname = self.PARole.getPatchName(profit_search,True)
                    if st.session_state.role['role_type'] == 'STORE' or st.session_state.role['role_type'] == 'PATCH':
                        st.text_input("Patch Name", patch_search, disabled=status_patch)
                        optionsPatch = [patch_search]
                    else:
                        # listPatchname = [patch_search]
                        listPatchname = self.PARole.getPatchName(profit_search)
                        optionsPatch = st.multiselect('Patch Name', listPatchname, disabled=status_patch)


                    e_date = st.date_input(
                        "End Date", key='e_date', min_value=st.session_state.s_date, max_value=st.session_state.max_date, value=st.session_state.max_date
                    )
                    # st.text_input("Store Name", disabled=True)
                with col_filter[2]:
                    if st.session_state.role['role_type'] == 'STORE':
                        st.text_input("Store Code|Name", store_name_search, disabled=status_store)
                    else:
                        patch_format = self.PARole.sqlRoleFormat(optionsPatch, 'get_option')
                        # try:
                        # except Exception as e:
                        #     patch_format = self.PARole.sqlRoleFormat(optionsPatch, 'get_option')

                        listStore = self.PARole.getStoreNameCode(profit_search, patch_format)

                        optionsStore = st.multiselect('Store Code|Name', listStore, disabled=status_profit)

            col_btnS = st.columns(1)
            with col_btnS[0]:
                st.session_state.btn = st.button("Search")
        st.write("st.session_state.btn: ", st.session_state.btn)
        st.cache_data
        if st.session_state.btn:
            # st.write("st.session_state.s_date: "+ str(st.session_state.s_date))
            # st.write("st.session_state.e_date: "+str(st.session_state.e_date))
            with st.spinner('Loading...'):

                storeCode_list = list()
                if optionsStore:
                    st.write("listStore: ", optionsStore)
                    for sc in optionsStore:
                        # st.write("sc: ", sc)
                        # st.write("split: ", sc.split("|")[0])
                        storeCode_list.append(sc.split("|")[0])

                    store_search= self.PARole.sqlRoleFormat(storeCode_list)
                    patch_search= self.PARole.sqlRoleFormat(optionsPatch)
                elif optionsPatch:
                    patch_search= self.PARole.sqlRoleFormat(optionsPatch)

                self.Layouts.reportGrid(st.session_state.s_date, st.session_state.e_date, profit_search, patch_search, store_search)

            st.session_state.btn = False

                # with st.spinner('Patch name to Loading...'):
                #     self.Layouts.reportGrid(st.session_state.s_date, st.session_state.e_date, role_name)
