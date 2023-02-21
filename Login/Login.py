import streamlit as st


def Func_Login():
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

    def OnLogin():
        if (email == "" or password == ""):
            st.error('Email or Password Incorrect.')
            

    with st.form("my_form"):
        st.header("Login")
        email = st.text_input("Email",)
        password = st.text_input("Password", type="password")

        st.form_submit_button("Submit", on_click=OnLogin)


