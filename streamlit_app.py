import streamlit as st

lab1 = st.Page("LAB-01.py",title="Lab 1")
lab2 = st.Page("LAB-02.py",title="Lab 2", default=True)
pg = st.navigation([lab1, lab2])
st.set_page_config(page_title="LAB Main Page")
pg.run()