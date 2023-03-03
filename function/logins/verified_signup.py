import streamlit as st

class VerifiedSignUp():
    def __init__(self, user,newpass, confpass):
        self.user = user.strip()
        self.newpass = newpass.strip()
        self.confpass = confpass.strip()
        self.status = False
        self.message = ""

    def checkPassword(self):
        if self.newpass != self.confpass:
            self.message = "Password is mismatch!"

    def checkPassword(self):
        if len(self.newpass) <= 7:
            self.message = "Please new password must more then 8 digit."
            st.error(self.message, icon="🚨")
        elif len(self.confpass) <= 7:
            self.message = "Please confirm password more then 8 digit."
            st.error(self.message, icon="🚨")
        else:
            self.status = True

    # check eamil in the table "user_uath"
    # check eamil in the table "user_alive" (view table)
    # def checkEmailPerm(self):
    #     pass

    def actionVerify(self):
        self.checkPassword()
        if self.status:
            st.success('This is a success message!', icon="✅")
        # return self

# def funcSignUp():

    # if authentication_status:
    #     # if password != passwordConfirm:
    #     #     st.warning('Confirm password validation fail.')
    #
    #     if password.count() < 8:
    #         # st.warning('Please add password more than 8 character.')
    #         st.write('Please add password more than 8 character.')

    # if authentication_status:
    #     st.write('Welcome *%s*' % (name))
    #     st.title('Some content')
    # elif authentication_status == False:
    #     st.error('Username/password is incorrect')
    # elif authentication_status == None:
    #     st.warning('Please enter your username and password')

# if submit and email == actual_email and password == actual_password:
#     # If the form is submitted and the email and password are correct,
#     # clear the form/container and display a success message
#     placeholder.empty()
#     st.success("Login successful")
# elif submit and email != actual_email and password != actual_password:
#     st.error("Login failed")
# else:
#     pass
