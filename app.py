import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

# Workaround for CrewAI/Groq cache_breakpoint incompatibility
import crewai.llms.cache as crewai_cache

crewai_cache.mark_cache_breakpoint = lambda msg: msg

# Import the rest of your application below this line
import streamlit as st
from crew_setup import run_resume_agents

import streamlit as st
from pypdf import PdfReader
from crew_setup import run_resume_agents

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon=":bar_chart:",
    layout="wide"
)

st.title("AI Resume Analyzer")
st.markdown("Upload your resume in PDF format, and our AI agents will provide you with a detailed analysis, including feedback on your resume's content, ATS compatibility, and personalized career advice.")

uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])

def extract_text_from_pdf(file):
    reader= PdfReader(file)
    text=""
    for page in reader.pages:
        if page.extract_text():
            text+=page.extract_text()
    return text

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.success("Resume uploaded successfully!")

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing resume..."):
            result = run_resume_agents(resume_text)
        st.success("Analysis complete!")
        col1 , col2, col3 = st.columns(3)
        with col1:
            st.subheader("Resume Roast")
            st.write(result.tasks_output[0].raw)
        with col2:
            st.subheader("ATS Compatibility")
            st.write(result.tasks_output[1].raw)
        with col3:
            st.subheader("Career Advice")
            st.write(result.tasks_output[2].raw)
        st.balloons()

           