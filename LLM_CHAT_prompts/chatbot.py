# from langchain_openai import ChatOpenAI
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv


load_dotenv()

print("API key loaded:", bool(os.getenv("GOOGLE_API_KEY")))
model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
# model = ChatOpenAI()

#for storing prev mssg history
chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]



#this is infinite loop jb tk 
# user exit nhi kre
while True:
    user_input = input("You : ")
    #apn ka msg chat history me append krnege
    #human msg me converttn kiya
    #humn msg level ho ke ja rha hai
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    #agr exit nhi hai toh

    #llm ke pass chat history hoga jyga, 
    # sent chat history, invoke means single msg
    result = model.invoke(chat_history)

     #jo ai se aaya usko bhi sotre kro ,
     # list mssg hoga ,,, jo llm se new mmsg 
     # usko bi caht history me appen kdendg
     #ai msg ko convert kr diya result ko
    chat_history.append(AIMessage(content=result.text))

    print("AI response : ",result.text)


#lop se bhr aagynge toh entire chat history
print(chat_history)