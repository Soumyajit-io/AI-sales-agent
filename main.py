from langchain_core.messages import SystemMessage,AIMessage, HumanMessage
from langchain_core.prompts import load_prompt
from agent import chatbot
import streamlit as st
import qrcode
import random
from io import BytesIO
import time

# -----------------Header------------------
st.set_page_config(page_title="AI Sales Assistant",
                   page_icon="🤖",
                   layout="wide")
st.markdown("## **AI Fashion Assistant**")  


# -----------------Session states and User input-------------
first_msg = "Welcome! I’m your AI Fashion Assistant. Share your occasion, style preference, or budget, and I’ll curate the right outfit for you."
if 'message_his' not in st.session_state:
   st.session_state['message_his']=[{'role':'assistant','content':first_msg}]
   time.sleep(1.3)
   with st.chat_message('assistant'):
      text = first_msg
      typed=''
      placeholder = st.empty()
      for ch in text:
         typed+=ch
         placeholder.markdown(f"{typed}_")
         time.sleep(0.03)
      placeholder.markdown(f"{typed}")

user_input =st.chat_input("Enter your message...")

if user_input : st.session_state['message_his'].append({'role':'user','content':user_input})

first_msg = "Welcome! I’m your AI Fashion Assistant. Share your occasion, style preference, or budget, and I’ll curate the right outfit for you."
template = load_prompt('prompts.json')
system_prompt = template.invoke({})

# chat history for ai
if 'chat_history' not in st.session_state:
   st.session_state['chat_history']=[SystemMessage(content=system_prompt.to_string()),AIMessage(content= first_msg)]

# -----------------Display Chat messages---------------------
if len(st.session_state['message_his']) == 1: pass
else:  
   for i in st.session_state['message_his']:
      with st.chat_message(i['role']):
         st.markdown(i['content'])

# ------------------------Sidebar UI---------------------
with st.sidebar:
   
   st.markdown("## **Continue In-Store**")

   if st.button("**Generate QR for In-Store Experience**"):   
      # Generate a simple random 6-digit Twin ID
      twin_id = f"DT-{random.randint(100000, 999999)}"
      qr_img = qrcode.make(twin_id)
      buf = BytesIO()
      qr_img.save(buf)
      st.image(buf.getvalue(), caption=f"Scan in-store — Twin ID: {twin_id}")

   st.markdown("---")
   st.markdown("## My Conversations")
   st.button("New Chat (Dummy)")

   st.button("Conversation 1 (Dummy)")
   st.button("Conversation 2 (Dummy)")
   st.button("Conversation 3 (Dummy)")


# ---------------------------Main UI------------------------
CONFIG = {'configurable':{'thread_id':"thread-1"}}
if user_input:
   st.session_state['chat_history'].append(HumanMessage(content= user_input))

   response = chatbot.invoke({'chat_history':st.session_state['chat_history']},config=CONFIG)
   st.session_state['chat_history'].append(AIMessage(content=response['chat_history'][-1].content))
   st.session_state['message_his'].append({'role':'assistant','content':response['chat_history'][-1].content})

   with st.chat_message('assistant'):
      text = response['chat_history'][-1].content
      typed=''
      placeholder = st.empty()
      for ch in text:
         typed+=ch
         placeholder.markdown(f"{typed}_")
         time.sleep(0.02)
      placeholder.markdown(f"{typed}")

