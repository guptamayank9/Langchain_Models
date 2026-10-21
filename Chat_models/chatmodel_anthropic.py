from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv

load_dotenv()

#here we also pareameter temp, or max_token
model = ChatAnthropic(model="claude-3.5-sonnet20241022")

result = model.invoke("What is the capital of India ?")

print(result.content)