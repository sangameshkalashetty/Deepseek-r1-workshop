from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

import streamlit as st

st.title("Deepseek-R1 chart bot")


template = """question: {question}
Answer = Generate the answer step by step"""

prompt = ChatPromptTemplate.from_template(template)

model = Ollama(model="deepseek-r1")  

chain = prompt | model

question = st.text_input("Enter your question here: ")
if question:
    try:
        formatted_prompt=prompt.format(question=question)

        response = chain.invoke({"question": question})
        
        #print("response:",response)
        st.write(response)

    except Exception as e:
        #print(f"Error:{e}")
        st.write(f"Error:{e}")

