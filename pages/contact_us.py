import streamlit as st
import send_Email
with st.form(key="Contact_us"):

    Sender_Email = st.text_input("Enter your Email Address",key='sender_email')
    message=st.text_area("Enter the message you want to send",key='message')
    topic=st.selectbox('Choose Topic',["Discussion","Meeting","Development"])
    msg=f"""\
Subject : New Email from {Sender_Email}

From : {Sender_Email}

Topic: {topic}
{message}
"""
    button = st.form_submit_button()
    if button:
        # print(st.session_state['sender_email'],st.session_state['message'])
        send_Email.sendEmail(msg)
        print(msg)
        st.info("Mail sent successfully")