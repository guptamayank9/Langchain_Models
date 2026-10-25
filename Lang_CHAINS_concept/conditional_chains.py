#from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv


load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.4
)

parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal['positive',  'negative'] = Field(description='Give the sentiment of the feedback')


parser2 = PydanticOutputParser(pydantic_object=Feedback)



prompt1 = PromptTemplate(
    template='Classify the sentiment of the following eedback text into positive or negative \n {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)
#classiefer chains
#phle negative wla generate

classifier_chain = prompt1 | model | parser2


#it give negative
# print(result)

#create runnable branch 
#pass multiple tuples bhjte ho
#2 cheexz bhjte ho (cndition, or usme ky anserwe chhaiye wo bhjte ho) ===>(contidton1, chain) last me
#  default agr nhi hua toh kuch 


#prompt2 and 3 create one for each branch
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    #asie conditon likhna hai sentiment positoive ay nega hoga, funciton create
    (lambda x: x.sentiment == 'positive' ,prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative' ,prompt3 | model | parser),

    #simple lambda function for default, this is not chain but we have ote xecue chain 
    # isko runable me conveert me krna pdaga using Runnablelmbda this cozz convet 
    # in runnable and we can use it as chainss
    # now this is an chain

    RunnableLambda(lambda x:'Could not find sentiment')

)

#final chain

chain = classifier_chain | branch_chain


#chain invoke

result = chain.invoke({'feedback':'This is a wonderful smartphone'})

print(result)

chain.get_graph().print_ascii()