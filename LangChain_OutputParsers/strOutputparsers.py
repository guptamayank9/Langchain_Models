# #this is open source model ,this not gice by default structured outputs
# nt: Is technique ko sequential prompting keh
# sakte hain, kyunki second LLM call ka input
# first call ke output par depend karta hai.

# Sequential Prompting seekh raha hai — pehle LLM 
# se detailed report generate karwana, phir usi
# report ka 5-line summary banwana.
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Open-source model ko configure karna
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    max_new_tokens=500
)

model = ChatHuggingFace(llm=llm)

# First prompt: Detailed report generate karna
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# Second prompt: Report ka 5-line summary banana
template2 = PromptTemplate(
    template="Write a 5-line summary of the following text:\n{text}",
    input_variables=["text"]
)

# Step 1: First prompt mein topic pass karna
prompt1 = template1.invoke({"topic": "black hole"})

# Step 2: Detailed report generate karna
result = model.invoke(prompt1)

# Step 3: Detailed report ko second prompt mein pass karna
prompt2 = template2.invoke({"text": result.content})

# Step 4: Summary generate karna
result1 = model.invoke(prompt2)

# Step 5: Final summary print karna
print(result1.content)


#abb issi ko ahum str outp parser se karke
#file name -- >  stroutputparserreal.py
#iseme use hua stroutputparserjo chains ke sath use hota hai