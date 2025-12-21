from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
from langgraph.graph.message import add_messages

load_dotenv()
# -----------------State----------------------
class chatstate(TypedDict):
   chat_history:Annotated[list[BaseMessage],add_messages]

# --------------------Model----------------------
llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# -----------------Chat function----------------
def chat_node(state:chatstate):
   msg = state["chat_history"]
   try:
    response=( llm.invoke(msg))
    return {"chat_history":[response]}
   
   except Exception as e :
    fallback_message = AIMessage(
            content=(
                "I’m having a temporary issue responding right now. "
                "Please try again in a moment, or continue this experience in-store using the QR option."
            )
        )
    return {"chat_history": [fallback_message]}

# -----------------Graph----------------------
graph = StateGraph(chatstate)
graph.add_node("chat_node",chat_node)
checkpointer = InMemorySaver() # Checkpointer
graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

chatbot = graph.compile(checkpointer=checkpointer)
