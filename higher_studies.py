import streamlit as st
import json

# Updated Data with multiple exam types and questions
data = {
    "ielts": {
        "what is ielts": "IELTS (International English Language Testing System) is a globally recognized English proficiency test for study, work, and migration.",
        "ielts exam fees": "The IELTS exam fee varies by country but is typically around $245–$255 (USD). Check your local test center for exact pricing.",
        "ielts eligibility": "Anyone can take the IELTS exam, but it is mainly for non-native English speakers who need to demonstrate English proficiency.",
        "ielts exam format": "IELTS has four sections: Listening (30 min), Reading (60 min), Writing (60 min), and Speaking (11–14 min).",
        "ielts preparation tips": "Practice listening to English accents, read academic texts, write essays, and speak English daily.",
        "ielts score range": "IELTS scores range from 0 to 9. Most universities require a minimum band score of 6.5 or 7.0.",
        "ielts test frequency": "IELTS is conducted multiple times a month, and you can choose your test date when booking.",
        "ielts validity": "The IELTS score is valid for 2 years from the date of the test.",
        "ielts vs toefl": "IELTS uses British English and includes a face-to-face Speaking test, while TOEFL uses American English and is fully computer-based.",
        "how to register for ielts": "Register for IELTS through the official IELTS website or authorized test centers."
    },
    "toefl": {
        "what is toefl": "TOEFL (Test of English as a Foreign Language) is an English proficiency test used for admissions to English-speaking universities.",
        "toefl exam fees": "The TOEFL exam fee varies by location, but it generally ranges from $180 to $300 (USD).",
        "toefl eligibility": "Anyone can take the TOEFL exam, though it is typically taken by non-native English speakers seeking university admission.",
        "toefl exam format": "TOEFL consists of four sections: Reading, Listening, Speaking, and Writing, totaling about 4 hours.",
        "toefl preparation tips": "Focus on listening to academic English, improve reading comprehension, and practice essay writing.",
        "toefl score range": "TOEFL scores range from 0 to 120. Each section is scored from 0 to 30.",
        "toefl test frequency": "TOEFL is available throughout the year with multiple test dates to choose from.",
        "toefl validity": "TOEFL scores are valid for two years from the test date.",
        "how to register for toefl": "To register for TOEFL, visit the official TOEFL website and choose your nearest test center."
    },
    "gre": {
        "what is gre": "GRE (Graduate Record Examinations) is a standardized test for admissions to graduate schools in the United States.",
        "gre exam fees": "GRE exam fees are around $205 to $230 (USD) depending on the test center and region.",
        "gre eligibility": "The GRE exam is open to anyone who wishes to apply to graduate school, but it is not mandatory for all programs.",
        "gre exam format": "The GRE has three sections: Verbal Reasoning, Quantitative Reasoning, and Analytical Writing.",
        "gre preparation tips": "Practice with GRE prep books, take mock tests, and work on improving time management during the exam.",
        "gre score range": "GRE scores range from 130 to 170 for both Verbal and Quantitative sections. Analytical Writing is scored from 0 to 6.",
        "gre test frequency": "GRE is available throughout the year. You can select your preferred test date during registration.",
        "gre validity": "The GRE score is valid for five years from the test date.",
        "how to register for gre": "Visit the official ETS GRE website to register for the GRE exam."
    },
    "pte": {
        "what is pte": "PTE (Pearson Test of English) is an English language proficiency test for non-native speakers, commonly used for study abroad purposes.",
        "pte exam fees": "The PTE exam costs approximately $150–$250 (USD), depending on the location.",
        "pte eligibility": "The PTE is available to non-native English speakers who wish to study, work, or migrate to English-speaking countries.",
        "pte exam format": "PTE consists of three sections: Speaking & Writing, Reading, and Listening.",
        "pte preparation tips": "Focus on improving your English speaking and writing skills, and practice with PTE-specific materials.",
        "pte score range": "PTE scores range from 10 to 90, with higher scores reflecting better language proficiency.",
        "pte test frequency": "PTE is available multiple times a week at test centers around the world.",
        "pte validity": "PTE scores are valid for two years.",
        "how to register for pte": "Register for PTE through the official Pearson website."
    }
    # Continue adding more exams as needed
}

# Streamlit App Layout
st.set_page_config(page_title="General Study Queries", layout="centered")

# Header
st.title("General Study Queries")
st.subheader("Get answers to your questions about exams like IELTS, TOEFL, GRE, and more!")

# Dropdown for selecting exam type
exam_type = st.selectbox(
    "Select Exam Type",
    options=["IELTS", "TOEFL", "GRE", "PTE"]
)

# List of questions related to the selected exam
questions = list(data[exam_type.lower()].keys())

# Dropdown for selecting a specific question
selected_question = st.selectbox("Select a question", options=questions)

# Display the answer to the selected question
if selected_question:
    st.write("**Answer**:")
    st.write(data[exam_type.lower()][selected_question])

# Custom Styling
st.markdown("""
<style>
    .css-1d391kg {
        background-color: #f4f4f9;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .css-14xtw13 {
        font-size: 20px;
    }
    .css-1jjc5md {
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("### Powered by Streamlit 💻")
