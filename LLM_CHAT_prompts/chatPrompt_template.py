from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

#this is a chatprompttemplate means ye ek dyanmicmssgs hai
#also we use ChChatPromptTemplate.from_messages
#this is a dynamic template
#ChatPromptTemplate isko multiple mssg usek rne ke liye use krte hai 
chat_template = ChatPromptTemplate([
    #tuple send
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
    # SystemMessage(content='You are a helpful {domain} expert'),
    # HumanMessage(content='Explain in simple terms, what is {topic}')
])
#value dedi variable ki inputki
#ye fill nhi hua abhi utan nhi hai toh  we give tuple
prompt = chat_template.invoke({'domain':'cricket', 'topic':'Dusra'})

print(prompt)