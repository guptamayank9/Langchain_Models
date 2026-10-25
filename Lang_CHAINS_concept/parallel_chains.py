#from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv


load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.4
)


prompt1 = PromptTemplate(
    template = 'Generate short and simple notes from the followind text \n {text}', 
    input_variables=['text']
)

prompt2  = PromptTemplate(
    template='Generate 5 shorts question answers from the following text \n {text}',
    input_variables=['text']
)

#dono p ko merge
prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n nots -> {notes} nad quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

#parese ceate

parser = StrOutputParser()

#chain create
#parallel chain create krne ke liuye runable parllel import
#larna hoga jo help krata hai run kren me parallel chains ko

#phle generate wla chain create krnege
#dict provide krana hai dono name dena hai bahut sarri ha gnerate krt kte hai
parallel_chain = RunnableParallel({
    #dict create krna hot hai
    'notes': prompt1 | model | parser,

    'quiz' : prompt2 | model | parser

})

#now we merge
merge_chain = prompt3 | model | parser


#final chain creaete kenre

#chain merge wla kegenr
chain = parallel_chain | merge_chain 

text = """ Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression tasks. It is widely used in data science and machine learning because of its ability to handle complex datasets.

The main objective of SVM is to find the best decision boundary, called a hyperplane, that separates data points belonging to different classes. SVM tries to maximize the margin between the hyperplane and the nearest data points from each class. These nearest data points are known as support vectors, and they play an important role in determining the position of the hyperplane.

One of the major advantages of SVM is that it can work effectively with high-dimensional data. It also supports different kernel functions, such as linear, polynomial, and radial basis function (RBF) kernels. These kernels help SVM classify data that cannot be separated using a simple straight line.

SVM is commonly used in applications such as spam email detection, image classification, text categorization, and handwriting recognition. For example, an SVM model can classify emails as spam or not spam by analyzing their features.

However, SVM can be computationally expensive for very large datasets, and selecting the appropriate kernel and parameters may require experimentation.

In conclusion, SVM is a powerful machine learning algorithm that provides effective classification results when its parameters are selected appropriately."""

result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()



