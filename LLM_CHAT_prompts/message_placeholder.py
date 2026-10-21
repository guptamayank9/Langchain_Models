from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    #pst me jitni bi converstatipn hui hogi wo sb aajygi 
    # ai ke pass fir ans deaga shi mssgplaceholder se
    MessagesPlaceholder(variable_name='chat_history'),

    ('human', '{query}')
])

chat_history= []
#load chat history
#python file handling use
with open('chat_history.txt') as f:
    #append krte ja rhe hai
    chat_history.extend(f.readlines())


print(chat_history)

#create prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my refund'})

print(prompt)