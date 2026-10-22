#file name -- > 
#file

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
#isme stroutparser use kar rhe hai 
#iska use most chains me hota hai
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Open-source model ko configure karna
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
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

parser = StrOutputParser()

#here stroutputparser chain me
# use hota hai toh apn bnayenge chain
#isme hua tmpl1 ko model ko diye fir parser ko diye
#  text nikalega , fir temp2 ko diye ttoh fir model ko deiye fir 
# wo pareser ko diya toh usse 5 lines summary nkila ke de dega
#This is much easier to use parser ,benefits using chains
chain = template1 | model | parser | template2 | model | parser

#ab hum sirf topic ka naam denge or result print kra lenge
result = chain.invoke({'topic':'Black hole'})

print(result)


