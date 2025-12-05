from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
import streamlit as st
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
# -----------------------
st.header("AI Sales agent ")  

if 'message_his' not in st.session_state:
   st.session_state['message_his']=[]

user_input =st.chat_input("Type here ")
if user_input : st.session_state['message_his'].append({'role':'user','content':user_input})
for i in st.session_state['message_his']:
   with st.chat_message(i['role']):
      st.text(i['content'])
if 'chat_history' not in st.session_state:
   st.session_state['chat_history']=[SystemMessage(content=system_prompt.to_string())]

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

