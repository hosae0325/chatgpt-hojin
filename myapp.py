import streamlit as st

st.title("Chatgpt")

prompt = st.text_input("Prompt")

if prompt:
   # call chatgpt api
   # response
   message = "Response"
   st.text(message)
