import streamlit as st
import google.generativeai as genai
import os
from PyPDF2 import PdfReader

from dotenv import load_dotenv

# Loading all environmenmt variables
load_dotenv()

# Create a .env file and store your API key in GOOGLE_API_KEY variable. 
# Loading gemini using API key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# Getting Gemini Pro Response
def generate_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Reading Resume PDF File
def pdf_to_text(uploaded_file):
    pdf = PdfReader(uploaded_file)
    text = ""
    for pg_no in range(len(pdf.pages)):
        page = pdf.pages[pg_no]
        text += str(page.extract_text())
    return text


# Prompt Template
input_prompt = """
Act like a skilled or very experienced ATS (Application Tracking System) with a deep understanding of tech field, software engineering, data science, data analyst and big data engineer. Your task is to evaluate the resume based on the given job description. You must consider the job market is very competitive and you should provide best assistance for improving the resumes. Assign the percentage Matching based on Jd and the missing keywords with high accuracy. Also provide suggestions on how to improve the given resume.
resume: {text}
description: {jd}

I want the response in one single string having the structure with JD Match as heading, Missing Keywords as subheading and Profile Summary as paragraph: 
JD Match: %, 
Missing Keywords : [], 
Profile Summary : 
Improvement Suggestions:    
"""

st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type = 'pdf', help='Please upload the pdf')

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = pdf_to_text(uploaded_file)
        response = generate_response(input_prompt)
        st.subheader(response)
