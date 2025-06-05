import streamlit as st

st.title("let's start python development")
st.subheader("welcome to the session")
st.text(" streamlit help user to create the web app using python.")
st.write("here we do not need of any html,css and js")

result=st.selectbox("your favrouite domain",['select','cse','mech','ece','ds'])
st.write(f"the selected domain is {result}")

st.success("success")
