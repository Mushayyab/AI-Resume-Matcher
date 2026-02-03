# 🎯 AI Resume Matcher

A professional **NLP-powered** web application that compares PDF resumes against job descriptions to calculate a match percentage.

## 🚀 Features
* **PDF Text Extraction:** Uses `pypdf` to scrape text from multi-page resumes.
* **Natural Language Processing:** Implements `Scikit-Learn`'s `CountVectorizer` to turn text into mathematical vectors.
* **Similarity Scoring:** Uses **Cosine Similarity** to calculate the distance between resume content and job requirements.
* **Streamlit UI:** A clean, interactive dashboard with real-time feedback.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Frontend:** Streamlit
* **ML/NLP:** Scikit-Learn
* **PDF Processing:** PyPDF

## 💻 How to Run
1. **Clone the repo:**
   `git clone https://github.com/YOUR_USERNAME/ResumeMatcher.git`
2. **Install dependencies:**
   `pip install streamlit pypdf scikit-learn`
3. **Run the app:**
   `streamlit run app.py`

## ⚖️ License
This project is licensed under the MIT License.