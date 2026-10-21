#here we create reviews of phones and extract structured op from dict

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

#literal me pos ,neg aie kar kte hai 
load_dotenv()

model = ChatOpenAI()

#flow

#her we schema create krenge
#data validation nhi kar skte ismes
#iske liye we use Pydantic next we see
class Review(TypedDict):

     #llist of theme ke jasie
    key_theme = Annotated[list[str], "Write down all the kye themes discused in the review in a  list"] 
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negativen, psitive , or neutral"]
    #pros ho bhi yanhi bhi toh optional kr skte hai iske liye we have Optional function
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons : Annotated[Optional[list[str]],"Write down all the cons inside a list"]
    name : Annotated[Optional[str], "Write the name of the reviewer"]


structured_model = model.with_structured_output(Review)







#here reqivew k bhj detae hai
result = structured_model.invoke(""" The hardware is great, but the software feels bloated. 
            there are too many pre-install app that I can't remove.
            Also the ui look outdated compared to other brand Hoping for
            a software update to fix this.
            I recently visited a smartphone service centre and had a positive experience with their professional and customer-focused service. The staff carefully understood the issue, explained the possible causes, and provided a detailed overview of the repair process before proceeding. They performed a thorough diagnosis, checked the device’s hardware and software functionality, and ensured that all essential features were working correctly. I particularly appreciated their transparent communication, technical expertise, and attention to detail throughout the process. They also provided useful recommendations for improving battery performance, maintaining device health, and preventing similar issues in the future. The service centre maintained a well-organized environment, and the team handled the device with proper care. The overall turnaround time was reasonable, and the final service quality met my expectations. What made the experience especially satisfying was their willingness to answer technical questions and explain the solutions in simple, understandable language. I would recommend this service centre to anyone looking for reliable smartphone diagnostics, professional repairs, and helpful customer support. Overall, it was a smooth and trustworthy experience that reflected a strong commitment to service quality and customer satisfaction.
            Review by Nistish Singh
            """)

#response in dict type
#summry generte karke dega
#syyetempormpt generate krkedeta hai
#{'summary':"Hard...","seneitment":'negative'}
print(result)
print(result.keys())
print(result['name'])
print(result['summary'])
print(result['sentiment'])
print(type(result))