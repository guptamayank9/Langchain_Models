
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
#isme stroutparser use kar rhe hai 
#iska use most chains me hota hai
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema


load_dotenv()

# Open-source model ko configure karna
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    max_new_tokens=500
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name = 'fact_1' , description='Fact 1 about the topic'),
    ResponseSchema(name = 'fact_2' , description='Fact 2 about the topic'),
    ResponseSchema(name = 'fact_3' , description='Fact 3 about the topic'),
]
#parser create

parser = StructuredOutputParser.from_response_schemas(schema)

#prompt creaete

template = PromptTemplate(
    template = 'Give 3 fast about  {topic} \n {format_instruction}',
    input_variables=['topic'],
    #dict ke nadr bhj denge ki value hone chahiye jo pareser se mil rhi hai
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

#chain ke throuth
#chain = template | model | parser | 
#result = chain.invoke({'topic':'black hole'})
#print(result)
# aise chain se ho jatajata

#prompt bnanyenge
prompt = template.invoke({'topic':'black hole'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)

#here we enfrorce schema

#dis : data validation nhi kr skte hai isme
#ex= name ,age laa ke do
# # name string ho aage integere
#  ho pr 35 yeaser sho toh isse nhi rok skte hai isse ceepte krna padga

# adv==  only enforce schema structerd dene me maxdur kr deta hai
#thats whi we ue Pydatticoutput parser next