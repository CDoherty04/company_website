import streamlit as st
from send_email import send_email

with st.form(key="form"):
    email = st.text_input("Email")
    topic = st.selectbox("Select a topic", options=["Job Inquiries", "Project Proposals", "Other"])
    message = st.text_area("Message", placeholder="Enter your message here...")
    button = st.form_submit_button("Submit")

    message = f"""\
Subject: Company Website inquiry about {topic}

{message}

From: {email}
"""

    if button:
        send_email(message)
        st.info("Email sent successfully!")
