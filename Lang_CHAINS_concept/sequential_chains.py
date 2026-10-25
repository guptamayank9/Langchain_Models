#from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()


#prompt1

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)


model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.4
)


#create parser

parser = StrOutputParser()

#chains create

chains = prompt1 | model | parser | prompt2 | model | parser

#result me store
result = chains.invoke({'topic':'Unemployment in India'})

#print
print(result)

#chain dekhne ke liye kasie dikhta hai kasie ja rha 
# hai ek dusre me mes 
chains.get_graph().print_ascii()