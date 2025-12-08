from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
import streamlit as st
import qrcode
import random
from io import BytesIO

import time
load_dotenv()

u_name=""
u_loc=""
u_size=""
u_gender=''
template = load_prompt('prompts.json')
system_prompt = template.invoke(
   {
      'user_name':u_name,
      'user_location':u_loc,
      'user_size':u_size,
      'user_gender':u_gender
   }
)


# Sidebar content
with st.sidebar:
   
   st.markdown("---")
   st.markdown("### Continue In-Store")

   if st.button("Generate QR for In-Store Experience"):   
      # Generate a simple random 6-digit Twin ID
      twin_id = f"DT-{random.randint(100000, 999999)}"
      qr_img = qrcode.make(twin_id)
      buf = BytesIO()
      qr_img.save(buf)
      st.image(buf.getvalue(), caption=f"Scan in-store — Twin ID: {twin_id}")


# -----------------------
st.header("AI Sales Assistant")  

first_msg = "Hi! I’m your AI Sales Assistant. Tell me what you're looking for and I’ll help you find the perfect outfit."
if 'message_his' not in st.session_state:
   st.session_state['message_his']=[{'role':'assistant','content':first_msg}]

user_input =st.chat_input("Type here ")



if user_input : st.session_state['message_his'].append({'role':'user','content':user_input})

for i in st.session_state['message_his']:
   with st.chat_message(i['role']):
      st.markdown(i['content'])
if 'chat_history' not in st.session_state:
   st.session_state['chat_history']=[SystemMessage(content=system_prompt.to_string()),AIMessage(content= first_msg)]

# ----------------------------------------
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

if user_input:
   
   
   st.session_state['chat_history'].append(HumanMessage(content= user_input))
   response = model.invoke(st.session_state['chat_history'])
   st.session_state['chat_history'].append(AIMessage(content=response.content))

   st.session_state['message_his'].append({'role':'assistant','content':response.content})
   with st.chat_message('assistant'):
      text = response.content
      typed=''
      placeholder = st.empty()
      for ch in text:
         typed+=ch
         placeholder.markdown(f"{typed}_")
         time.sleep(0.02)
      placeholder.markdown(f"{typed}")

