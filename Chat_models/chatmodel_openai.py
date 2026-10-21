from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.3, max_completion_tokens=10)

result = model.invoke("What is the capital of India")

#ye sb additional inf bhi dega toh
#so we use result.content
#print(result)
#at temp 0 suggest me  5 indian male name
#at 1.5+ write a 5 line poem on circket

print(result.content)