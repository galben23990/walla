import openai
import streamlit
import streamlit as st
from utils import *
import os
from config import *
import time
import pandas as pd
from create_content import *
import json
import re
from utiltes import *
import time
import datetime as dt
from datetime import datetime, timedelta
from serpapi import GoogleSearch
from collections import defaultdict




if 'article_data' not in st.session_state:
    st.session_state['article_data'] = None

        
def chat_process(prompt,massage_history="",write_contetn=False):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages[0]["content"] = "YOUR NAME IS EditBot get use request and generated content and edit it by user request is it improtnetn to edit and not to change the content completly , you change it complety only if user requsteds the goal os to tanslete the orginal hebraw article ana naintaine the style"

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
    
        message_placeholder = st.empty()
        full_response = ""
        for response in openaiclient.chat.completions.create(
            model=st.session_state["openai_model"],
            stream=True,
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
        ):
            # Check for content and finish reason
            if response.choices[0].delta.content is not None:
                full_response += response.choices[0].delta.content
                message_placeholder.write(full_response + "▌")
            if response.choices[0].finish_reason is not None:
                break

        message_placeholder.write(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    st.rerun()
      



    start_index = 2 if st.session_state["submit_pressed"] else 2
    for index, message in enumerate(st.session_state.messages):
        if index < start_index:
            continue
        with st.chat_message(message["role"]):
            st.write(message["content"])



#name with imoji
st.title("TranBot🤖")

x="sk-9xPQ9C50b"
y="c1sYkg2yikQT3Bl"
z="bkFJ6jlVHQrpiJT3KZ9BmOMP"


openai.api_key = x+y+z
openaiclient = openai.OpenAI(api_key=openai.api_key )

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4-1106-preview"
    

if 'url_content' not in st.session_state:
    st.session_state['url_content'] = None

if "submit_pressed" not in st.session_state:
    st.session_state["submit_pressed"] = False



enter_url = st.sidebar.text_area("Paste an article content here",height=150)
instuction=st.sidebar.text_area("Enter the instruction you want to give to Echo")


if st.session_state['url_content'] is not None:
    with st.expander("✔️ Completed Expand to See the Content summury", expanded=True):
        st.write(st.session_state['url_content'])


# Get the list of files in the specified director
# Variable to hold the content of the selected file
data = None

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_pdf_chat},
                                {"role": "assistant", "content": "Hello,Please add article to translate"}]

if st.sidebar.button("Submit"):
    st.session_state["submit_pressed"] = True
     
    prompt=f"**AERTICLE TO TRANSLATE:**`{enter_url}`\ninstuction:`{instuction}`"
    start_index = 3 if st.session_state["submit_pressed"] else 2
    for index, message in enumerate(st.session_state.messages):
        if index < start_index:
            continue
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    spinner_placeholder = st.empty()
    expander_placeholder = st.empty()
    spinner_url = st.empty()
    spinner_news = st.empty()
    spinner_webiste = st.empty()
    spinner_pdf = st.empty()
    expander_url = st.empty()
    expander_news=st.empty()
    expander_website=st.empty()
    expander_pdf=st.empty()


    chat_process(prompt,write_contetn=True)

    



start_index =  3 if st.session_state["submit_pressed"] else 2
for index, message in enumerate(st.session_state.messages):
    if index < start_index:
        continue
    with st.chat_message(message["role"]):
        st.write(message["content"])
if prompt := st.chat_input("What is up?"):
        chat_process(prompt)

        
   


