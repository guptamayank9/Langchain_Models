from langchain_core.prompts import PromptTemplate


#template
template = PromptTemplate(
    template="""
    Please summarize the research paper titled "{paper_input}"
    with the following specifications:

    Explanation Style: {style_input}
    Explanation Length: {length_input}

    Instructions:
    1. Explain the main idea and objectives of the research paper.
    2. Explain the methodology used in the paper.
    3. Highlight the key findings and conclusions.
    4. Explain mathematical concepts in a simple way if applicable.
    5. Use relatable analogies wherever helpful.
    6. Adjust the explanation according to the selected style and length.
    7. If any information is unavailable, clearly mention it.
    """,
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True
)

template.save('template.json')