import streamlit as st
from app_utils import llama

# App title
st.set_page_config(page_title="🦙💬 Llama 2 Chatbot")
st.title("🦙💬 Llama 2 Chatbot")

question = "say 'Press win+enter to send'. Don't say anything else at all."

context = st.text_area("Enter some context")
question = st.text_input("Enter a question")


response = llama(question, context)

st.write(response)
