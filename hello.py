import streamlit as st

t,t1=False,False
name=st.text_input("What is your name?")
DOB=st.date_input("What is your date of birth?")
if name != "":
    t=True
    if DOB != "":
        t1=True
    s=st.button("Submit")
if t1 and t:
    st.write("Hello",name,"you are born on",DOB)


