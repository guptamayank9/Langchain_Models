#from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()



#preompt creaate
#this si simple chains
prompt = PromptTemplate(
    template = 'Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2
)

#create parsee for struced
parser = StrOutputParser()

#chains form
# | this called pipe operator or langchain expression language

chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})
#ab ye phle topic prompt ke inpt me jyga
#fir model me jyga response aayga 
#fir parser ko jyga fir anse dega

print(result)



#we can also visulaize chains
#by useing getggraph ki chains kasie kaam kgr rhe hai dekh skte ho

chain.get_graph().print_ascii()