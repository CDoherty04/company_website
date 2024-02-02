import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("Welcome to The Company!")
content = ("Here at The Company, innovation meets excellence in every endeavor. As a pioneering force in our industry, "
           "we are dedicated to delivering unparalleled solutions that redefine standards and exceed expectations. "
           "With a relentless commitment to quality, integrity, and client satisfaction, we empower businesses to "
           "thrive in dynamic environments. Backed by a team of seasoned experts and fueled by a passion for progress, "
           "we harness the latest technologies and strategic insights to drive transformative outcomes. Explore our "
           "comprehensive suite of services and discover how we can catalyze your success today.")
st.write(content)
st.markdown("***")
st.title("Meet the team")

col1, col2, col3, col4 = st.columns(4)
df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:3].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images\\" + row["image"])
        st.title("")

with col2:
    for index, row in df[3:6].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images\\" + row["image"])
        st.title("")

with col3:
    for index, row in df[6:9].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images\\" + row["image"])
        st.title("")

with col4:
    for index, row in df[9:].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images\\" + row["image"])
        st.title("")
