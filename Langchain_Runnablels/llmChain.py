from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import LLMChain

#load the llm
llm = OpenAI(model_name = 'gpt-3.5-turbo', temperature=0.7)

#create a prompt template

prompt = PromptTemplate(
    input_variables = ['topic'],
    template = 'Suggest a catchy blog title about {topic}',
)

#create  an llmchain
chain = LLMChain(llm =llm, prompt = prompt)

#run the chains with a specific topic

topic = input('Enter a topic')
output = chain.run(topic)

print("Generated Blog Title: ", output)
