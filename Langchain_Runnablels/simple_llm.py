from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

llms = OpenAI(model_name = 'gpt-3.5-turbo', temperature=0.7)


#creaet a prompt  template
prompt = PromptTemplate(
    input_variables = ['topic'],
    template = 'Suggest a catchy blog title about {topic}',
)

#define the input

topic = input('Enter a topic')

#foramt the prompt manually using PromptTempalte
formatted_prompt=  prompt.format(topic=topic)

#call the llm directlt

blog_title = llms.predict(formatted_prompt)

#print the output
print("Generated Blog Title: ", blog_title)