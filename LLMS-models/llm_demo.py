from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#make obj of llm

llm = OpenAI(model='gpt-3.5-turbo-instruct')

#importn funct call invoke
result = llm.invoke("What is the capital of India")

print(result)