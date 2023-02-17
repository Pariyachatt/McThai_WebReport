import streamlit as st
from database.dbConfig import *
from layouts.Layouts import *
import datetime
import streamlit_nested_layout as sn
from PIL import Image

st.set_page_config(
    page_title="Web Report",
    layout="wide",
    page_icon=None,
)

with open('./css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def main():

    # min_date = datetime.datetime.now()

    # min_date = datetime.datetime.strptime(
    # str(datetime.datetime.now().year)+"/"+"01/01", "%Y/%m/%d")

    if 'max_date' not in st.session_state:
        st.session_state.max_date = datetime.datetime.now()
        
    if 'min_date' not in st.session_state:
        st.session_state.min_date = datetime.datetime.now()

    if 'isInvaild' not in st.session_state:
        st.session_state.isInvaild = False

    def s_date_onchanged():

        st.session_state.max_date = st.session_state.s_date + datetime.timedelta(
            days=31)
        
        st.session_state.max_date
        # st.session_state.max_date
        # if 'min_date' not in st.session_state:
        #     st.session_state.min_date = st.session_state.s_date
        # if st.session_state.max_date.year != s_date.year:
        #     st.session_state.max_date = datetime.datetime.strptime(
        #         str(datetime.datetime.now().year)+"/"+"12/31", "%Y/%m/%d")

    # def e_date_onchanged():
    #     if st.session_state.e_date < st.session_state.s_date:
    #         st.session_state.isInvaild = True

    # get_user = ["OUI", "KAI", "5", "Pattaya"]

    st.header("Net Sales Report")
    with st.container():
        container_header = st.columns(1)
        with container_header[0]:
            # col_1, col_2 = st.columns([0.40, 0.60],gap='small')
            col_filter = st.columns([0.20, 0.20, 0.30, 0.30], gap='small')

            with col_filter[0]:
                st.text_input("Profit name", disabled=True)
                st.text_input("Store code")
            with col_filter[1]:
                st.text_input("Patch name", disabled=True)
                st.text_input("Store name", disabled=True)
            with col_filter[2]:
                s_date = st.date_input(
                    "Start Date", key='s_date', on_change=s_date_onchanged)
                s_date
            with col_filter[3]:
                e_date = st.date_input(
                    "End Date", key='e_date', max_value=st.session_state.max_date)
                # if st.session_state.isInvaild:
                #     st.write("End date greater than or equal to Start date.")
        col_btnS = st.columns(1)
        with col_btnS[0]:
            st.session_state.btn = st.button("Search")

    if st.session_state.btn:
        showReport(s_date, e_date)


main()
