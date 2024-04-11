import streamlit as st
from app_utils import llama

# App title
st.set_page_config(page_title="🦙💬 Llama 2 Chatbot")


prompt = st.text_input("Enter your message here:")

response = llama(prompt)

st.write(response)
