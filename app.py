import streamlit as st
from resume_parser import extract_text
from analyzer import analyze_resume
from job_matcher import recommend_jobs

st.title("AI-Powered Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

if uploaded_file:
    text = extract_text(uploaded_file.name)
    analysis = analyze_resume(text)
    
    st.subheader("Extracted Skills")
    st.write(analysis["skills"])
    
    st.subheader("Strengths")
    st.write(analysis["strengths"])
    
    st.subheader("Weaknesses")
    st.write(analysis["weaknesses"])
    
    st.subheader("Job Recommendations")
    jobs = recommend_jobs(analysis["skills"])
    st.write(jobs)
