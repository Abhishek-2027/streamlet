import streamlit as st

st.title('lemon juce app')
if st.button("make  juce"):
    st.success("juce is being ready")
juce_type=st.radio("choose juce type",['mango','orange','litchi','apple'])
st.write(f" your juce is of {juce_type}")
salt=st.checkbox("add salt")
if salt:
    st.success("salt would be added .")
else:
    st.write("no salt would be provided seperately")

add_flabour=st.checkbox("add flaboure")
if add_flabour:
    st.write("flaboure added to juce")
sugar=st.slider("sugar level",0,5,2)
st.write(f"sugar level is {sugar}")

glass=st.number_input("how many glass",min_value=1, max_value=8,step=1)
st.write(f"number of glass is : {glass}")

name=st.text_input("enter your name ")
st.write(f"{name}")

dob=st.date_input("select your date of birth:.")
print(dob)


