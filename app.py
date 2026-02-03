from pypdf import PdfReader # type: ignore
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

def calculate_similarity(resume_text, job_desc):
    content = [resume_text, job_desc]
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(content)
    similarity = cosine_similarity(count_matrix)
    return similarity[0][1] * 100

st.title("AI Resume Matcher")
st.write("This app helps you check if your Resume matches a Job Description.")

uploaded_file = st.file_uploader("Upload your Resume", type="pdf")
job_description = st.text_area("Paste your Job Description here")

if st.button("Compare Now"):
    if uploaded_file is not None and job_description:
        resume_text = extract_text_from_pdf(uploaded_file)
        score = calculate_similarity(resume_text,job_description)
        st.subheader(f"Match Score: {score:.2f}%")
    else:
        st.error("Please upload a resume and paste a job description first!")

