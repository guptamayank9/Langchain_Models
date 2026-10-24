
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
#isme stroutparser use kar rhe hai 
#iska use most chains me hota hai
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema, PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# Open-source model ko configure karna
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    max_new_tokens=500
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='age of the person')
    city: str = Field(description='Name of the city of the person belongs to')


parser = PydanticOutputParser(pydantic_object=Person)

#prompt
template = PromptTemplate(
    template = 'Generate the name , age & city of a Fictional {place} person \n {format_instructions}',
    input_variables=['place'],
    partial_variables={'format_instructions':parser.get_format_instructions()}

)

prompt= template.invoke({'place':'indian'})

# //behind the screen
# prinpt(prompt) //jo llm ke pas ja rha hai padh skte hai prompt llm ka 

result= model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)
#op = name='priya shrma', age = 22, city='banglore


# #chain le throug
# se chain = template | model | parser
# final_result = chain.invoke({'place':'sri lanka'})

# print(final_result)

# #koi si bhi llm ke stah run kr skte ho
#  gegoel gemini, chatgpt ,huging HuggingFace

