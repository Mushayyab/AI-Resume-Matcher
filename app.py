# External libraries for UI, PDF processing, and NLP math
from pypdf import PdfReader # type: ignore
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Resume Matcher", page_icon="📄", layout="wide")

# Function to loop through PDF pages and combine text into one string
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

# Uses Vectorization and Cosine Similarity to compare two strings of text
def calculate_similarity(resume_text, job_desc):
    content = [resume_text, job_desc]
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(content)
    similarity = cosine_similarity(count_matrix)
    return similarity[0][1] * 100

# Configure the browser tab and layout
with st.sidebar:
    st.title("Settings & Info")
    st.write("This tool uses **Natural Language Processing (NLP)** to compare your resume against job requirements.")
    st.info("Tip: Make sure your PDF is not password protected.")

st.title("🎯 AI Resume Matcher")

uploaded_file = st.file_uploader("Upload your Resume", type="pdf")
job_description = st.text_area("Paste your Job Description here")

# Main logic trigger: runs when the user clicks 'Compare Now'
if st.button("Compare Now"):
    if uploaded_file is not None and job_description:
        resume_text = extract_text_from_pdf(uploaded_file)
        score = calculate_similarity(resume_text,job_description)
        st.divider()
        st.metric(label="Match Quality", value=f"{score:.2f}%")
        st.progress(score / 100)
        if score >= 80:
            st.success("Strong Match! Your resume is highly optimized for this role.")
        elif score >= 50:
            st.warning("Moderate Match. Consider adding more specific keywords from the job description.")
        else:
            st.error("Low Match. You may need to significantly tailor your resume.")
    else:
        st.error("Please upload a resume and paste a job description first!")

