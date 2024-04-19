import streamlit as st
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "enter ur openai api key"

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    pdfreader = PdfReader(pdf_path)
    raw_text = ''
    for page in pdfreader.pages:
        content = page.extract_text()
        if content:
            raw_text += content
    return raw_text

# Function to split text
def split_text(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=800,
        chunk_overlap=200,
        length_function=len,
    )
    return text_splitter.split_text(raw_text)

# Function to load embeddings and create FAISS index
def load_embeddings_and_index(texts):
    embeddings = OpenAIEmbeddings()
    document_search = FAISS.from_texts(texts, embeddings)
    return document_search

# Function to load QA chain
def load_my_qa_chain():
    return load_qa_chain(OpenAI(), "stuff")

# Main function for Streamlit app
def main():
    st.title("PDF Text Search and Question Answering")

    # File upload section
    uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"])
    if uploaded_file:
        st.write("PDF file uploaded successfully!")

        # Extract text from uploaded PDF
        raw_text = extract_text_from_pdf(uploaded_file)
        #st.write("Text extracted from PDF:")
        #st.write(raw_text)

        # Split text
        texts = split_text(raw_text)

        # Load embeddings and create FAISS index
        document_search = load_embeddings_and_index(texts)

        # Load QA chain
        chain = load_my_qa_chain()

        # User prompt input
        prompt = st.text_input("Write your prompt:")

        if st.button("Get Answer"):
            # Perform similarity search
            docs = document_search.similarity_search(prompt)

            # Run QA chain
            answer = chain.run(input_documents=docs, question=prompt)
            st.write("Answer:", answer)

# Run the Streamlit app
if __name__ == "__main__":
    main()
