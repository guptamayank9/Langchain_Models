from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)


model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

result = model.invoke("What is the capital of india?")

print(result.content)