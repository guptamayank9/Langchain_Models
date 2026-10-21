from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

#This is a static mssg

#in mssg k thriugh integrate krte hai
#list as chathistory
#create systemmssg
messages = [
   SystemMessage(content='You are helpful assistant'),
   HumanMessage(content='Tell me about Langchain')

]

#result dega ai# model ko bhja ,ans diya 
result = model.invoke(messages)

#plt ke ai ans dega or usee append kr denge
#fir use plt kr ai msg me convert kiya 
messages.append(AIMessage(content=result.content))


#fir caht history me convent kre 
print(messages)

#run python message.py