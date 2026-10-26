#pdf reader
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


#load the documetn
#abhi ke liye text load ha ina ki pdf
loader = TextLoader('learning.txt') #ensure docs.text exits
documents = loader.load()


#split the text into smaller chunks
#RecursiveCharacterTextSplitter ye ek components hai
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

#convert text into embeddings and store in FAIss

vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

#craeate ta reetriver (fetches a relveant documents)
retriever = vectorstore.as_retriever()


#manually the retrieve relevant documents
query = 'What are the key takeways from the documents ? '
retrieved_docs = retriever.get_relevant_documents(query)

#combine retrieverd text into a single Promt, jo close hai text k , pdf se nikal ke lya
retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])

#intialize the llm
llm = OpenAI(model_name = 'gpt-3.5-turbo', temperature=0.7)

#manually the pass returve text to llm

prompt = f""" Based on the follwing text, answer the question : {query}\n\n{retrieved_text} """
answer = llm.invoke(prompt)

#print the ans
print("Answer : ",answer)

