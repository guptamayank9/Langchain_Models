#LLm ko force krta hai ki output json me aaye

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
#isme stroutparser use kar rhe hai 
#iska use most chains me hota hai
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

load_dotenv()

# Open-source model ko configure karna
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    max_new_tokens=500
)

model = ChatHuggingFace(llm=llm)

#parser form
parser = JsonOutputParser()

template = PromptTemplate(
    temmplate = 'Give me the name, age , city of a fictional person \n {format_instruction}',
    input_variables=[],
    #prompt form karte time addtional inform chhiaye toh parser btabta hai 
    #ki when  u call the get.format_instauction toh ye aata hai 
    #partial variable use bz ye runtimek phle fill ho jaata hai with the help
    #of get.format_instaruton smjha

    partial_variables={'format_instruction':parser.get_format_instructions()}

)
#chain use
# chan =  template | model | parser
#value bhjo blank dict 
#result = chain.invoke({})
#print(result)

prompt = template.format()

result = model.invoke(prompt)

#parser usek renge
final_result = parser.parse(result.content)
#gve in json format
print(final_result)

#type also print
print(type(final_result))


#but isme problem hai isme schema force nhi kar sskte
#ki structuring nhi kar skte  wo llm khud krt ah i 
#means  json ka structuring nhi bta skte ho

#   temmplate = 'Give me the 5 facts of {topic} \n {format_instruction}',
#     input_variables=['topic'],

#result = chain.invoke({'topic':'black hole'})
#toh structing me ache se nhi dega 

#maan lo mujhe asie chaiye
#fact1-- _____ yha value ho facts likha ho
#fact2-- _____ yha value ho facts likha ho
#toh hum log aise me isse nhi kar skte hai
#json me nhi kar skte hai yhi hai biggest flwao

#fir yhi aaya StructuredOutput parser  isme kar skte hai structing ache se
#next yhi seekhegne