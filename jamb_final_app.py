import streamlit as st
import pandas as pd

file_path = "jamb_subjets_data.csv" 
df = pd.read_csv(file_path)

st.set_page_config(
    page_title="JAMB Subject Predictor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 JAMB Subject Combination Predictor")
st.write("Enter a Nigerian university course to see the recommended JAMB subjects.")

def text_similarity(a, b):
    a = set(a.lower().split())
    b = set(b.lower().split())
    if not a or not b:
        return 0
    return len(a & b) / len(a | b)

def get_jamb_subjects(course_name):
    best_score = 0
    best_subjects = None

    for _, row in df.iterrows():
        score = text_similarity(course_name, row["Course"])
        if score > best_score:
            best_score = score
            best_subjects = row["JAMB_Subjects"]

    if best_score >= 0.3:
        return best_subjects
    return None

course = st.text_input("Course name", placeholder="e.g. Computer Science")

if course:
    result = get_jamb_subjects(course)
    if result:
        st.success("Recommended JAMB Subjects:")
        st.write(result)
    else:
        st.error("Course not found in dataset.")

st.markdown("---")
st.caption("Built with Python & Streamlit")

