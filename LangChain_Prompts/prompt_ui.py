#This is a Static 
# Prompt here hame baar  bar query krnee padta 4
# hia ki kasie summarize chahtiyeh ia toh ye bahut diffilct ai baar baar bhjna padta hai

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


st.header('Research Tool')

user_input = st.text_input("Enter your Prompt")

#button
if st.button("summarize"):
    result = model.invoke(user_input)
    st.write(result.content)
   