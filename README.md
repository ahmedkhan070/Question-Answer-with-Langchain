# Question Answer System with Langchain and Streamlit

This project demonstrates how to build a question-answering system using Langchain and a Streamlit app. The app leverages PyPDF2 to extract text from PDF files and uses Langchain to answer questions related to the PDF content.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [References](#references)

## Introduction

The question-answering system allows you to upload a PDF document and ask questions related to the content of the PDF. The system uses PyPDF2 to extract text from the PDF and Langchain to answer questions based on the extracted text.

## Features

- Upload PDF documents for text extraction.
- Use Langchain for answering questions related to the PDF content.
- Streamlit-based user interface for easy interaction.

## Setup and Installation

1. **Clone the Repository**:
    - Clone the project repository to your local machine.
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a Virtual Environment**:
    - Create and activate a virtual environment (recommended).
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:
    - Install the required Python packages using the provided `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit App**:
    - Start the Streamlit app.
    ```bash
    streamlit run app.py
    ```

## Usage

- Once the app is running, you can upload a PDF document using the file uploader in the app.
- Enter a question related to the content of the PDF in the provided text input box.
- The app will extract text from the uploaded PDF, process the question, and display the answer based on the content of the PDF.

## Code Explanation

- **app.py**:
    - The main Streamlit app file.
    - Imports necessary libraries including PyPDF2 and Langchain.
    - Uses Streamlit to create the user interface.
    - Handles file uploading, text extraction, question processing, and answer generation.

- **Langchain**:
    - Langchain is used for processing the input question and generating an answer based on the extracted text from the PDF.
    - It integrates language models and various other NLP techniques to answer the questions.

- **PyPDF2**:
    - PyPDF2 is used to extract text from the uploaded PDF file.
    - The extracted text is then passed to Langchain for question-answering.

## References

- [Langchain Documentation](https://docs.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [PyPDF2 Documentation](https://pypi.org/project/PyPDF2/)

## Conclusion

This project provides an example of how to build a question-answering system using Langchain and Streamlit. The integration of PyPDF2 allows for easy text extraction from PDF documents, and Langchain enables advanced question-answering capabilities based on the extracted content. Feel free to customize and extend this project to suit your needs.
