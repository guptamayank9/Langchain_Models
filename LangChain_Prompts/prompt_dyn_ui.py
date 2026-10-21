from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
model = ChatOpenAI();

st.header('Research Tool')

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Select...",
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)
# #template
# template = PromptTemplate(
#     template="""
#     Please summarize the research paper titled "{paper_input}"
#     with the following specifications:

#     Explanation Style: {style_input}
#     Explanation Length: {length_input}

#     Instructions:
#     1. Explain the main idea and objectives of the research paper.
#     2. Explain the methodology used in the paper.
#     3. Highlight the key findings and conclusions.
#     4. Explain mathematical concepts in a simple way if applicable.
#     5. Use relatable analogies wherever helpful.
#     6. Adjust the explanation according to the selected style and length.
#     7. If any information is unavailable, clearly mention it.
#     """,
#     input_variables=["paper_input", "style_input", "length_input"]
# )

#now we use like as template file

template = load_prompt('template.json')

#fill the place holder
prompt = template.invoke({
    'paper_input':paper_input,
    "style_input":style_input,
    "length_input":length_input
})

#button
if st.button("summarize"):
   result= model.invoke(prompt)
   st.write(result.content)
   