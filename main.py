import streamlit as st
import google.generativeai as genai
import os
from PyPDF2 import PdfReader

from dotenv import load_dotenv

# Loading all environmenmt variables
load_dotenv()

# Important Instruction -
# Create a .env file and store your API key in GOOGLE_API_KEY variable. 
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# Getting Gemini Pro Response
def generate_response(input):
    """
    generates response based on the input.

    Args:
        input (str): job description input prompt

    Returns:
        str: generated output by gemini
    """
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


##### Streamlit app ######
with st.sidebar:
    mode = st.radio(
            label="Select Mode",
            options=["ATS Resume Checker", "Expert Guidance"],
            key="visibility",
            on_change=st.cache_data.clear(),
    )

#### Chat Mode ######################
if mode == "Expert Guidance":

    # Creating message list.
    if 'messages' not in st.session_state:
        st.session_state.messages = []


    st.header("Jacob Peralta")
    st.caption('Gemini Agent ID: 007')
    st.divider()

    # Initial Greeting message
    st.chat_message('assistant').markdown(" Hey there! how may I help you today?")

    for message in st.session_state.messages:
        st.chat_message(message['role']).markdown(message['content'])

    # getting user prompt as input
    prompt = st.chat_input("Enter query")
    # adding Prompt to prompt template
    in_prompt = f"System: your name is Jake and you are an Resume Expert and offer guidance on improving resume and portfolio. you are asked the following query: {prompt}"

    if prompt:
        st.chat_message('user').markdown(prompt)
        st.session_state.messages.append({'role':'user', 'content':prompt})
        
        with st.spinner("Loading..."):
            response = generate_response(in_prompt)
        st.chat_message('assistant').markdown(response)
        st.session_state.messages.append({'role':'assistant', 'content':response})


#### ATS Resume Checker Mode ######################
if mode == "ATS Resume Checker":
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
    st.title("ATS Resume Checker")
    uploaded_file = st.file_uploader("Upload Your Resume", type = 'pdf', help='Please upload the pdf')
    st.divider()

    jd = st.chat_input("Paste the Job Description")
    if jd:
        st.text("Job Description: " + jd)
        if uploaded_file is not None:
            text = pdf_to_text(uploaded_file)
            with st.spinner("Loading..."):
                response = generate_response(input_prompt)
            st.success('Done!', icon="✅")
            st.subheader(response)
