#from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings


from dotenv import load_dotenv
# Do vectors ke beech cosine similarity calculate karne ke liye
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L12-v2')
#embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

# Kuch sample documents banaye hain
# In documents mein cricket aur IPL se related information hai
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and chasing ability.",
    "MS Dhoni captained India to victory in the 2007 T20 World Cup and the 2011 ODI World Cup.",
    "Rohit Sharma is known for scoring three double centuries in One Day Internationals.",
    "Jasprit Bumrah is a fast bowler famous for his unusual action and accurate yorkers.",
    "The IPL is a T20 cricket league in India that started in 2008.",
]
# User ka question ya search query
query = 'tell me about ipl'

# Har document ko numerical vector mein convert kar rahe hain
# Har document ke liye ek alag embedding generate hogi
doc_embeddings = embedding.embed_documents(documents)

# Query ko bhi numerical vector mein convert kar rahe hain
# Ab query aur documents ko vectors ke form mein compare kar sakte hain
query_embedding = embedding.embed_query(query)


# Query embedding aur sabhi document embeddings ki similarity calculate karo
# [query_embedding] se query ko 2D list mein convert kiya hai
# [0] se pehli row ke similarity scores nikal rahe hain
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

#1d lst ko enumarate me bhj denge like a idx postion not chagne this
# enumerate() har score ke saath uska index jodta hai
# Example: [(0, 0.25), (1, 0.30), (2, 0.20)]
# Actual scores model run hone par milenge

print(list(enumerate(scores)))

#sort ho gye sort on similarity scores , soncd wle basis pe sort krenge
#ex -> [2,4.24543]
#hume asbse bada  lwlla chahuey toh [-1] kr denege
# enumerate(scores) se (index, score) pairs bante hain
# sorted() ko score ke basis par ascending order mein sort karte hain
# x[1] ka matlab har pair ka similarity score hai
# [-1] sorted list ka last element deta hai, yaani highest score

index ,score = (sorted(list(enumerate(scores)), key=lambda x:x[1])[-1])


# Sabse relevant document print karo
# index us document ki original list wali position ha
# Selected document ka cosine similarity score print karo
print(query)
print(documents[index])
print("similarity score is : ",score)
