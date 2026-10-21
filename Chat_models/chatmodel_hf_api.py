
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()




#llmka paremeter bnana hoga passs kerne ke 
# liye htoa hai ek 
#llm config , class pass
#REPO KA NAAM PASS MODEL WE USE,
#  TASK KY KRANA CHAHTE HAI
## Hugging Face hosted model configure karo

llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
     max_new_tokens=100,
    provider="auto"
)



model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India ?")
print(result.content)