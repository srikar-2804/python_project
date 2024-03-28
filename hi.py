import streamlit as st
def substract():
    st.write("2")
def add():
    st.write("clicked")
    substract()



st.write("welcome")

st.button("click me",on_click=add)