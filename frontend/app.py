import streamlit as st
import time
import pandas as pd
from utils import extract_text_from_file
from scraper import detect_job_cards_with_description
from resume_matcher import ResumeMatcher
from ui_components import apply_custom_styles, render_job_card

# Page configuration
st.set_page_config(
    page_title="LinkedIn Job Scraper with Resume Matching",
    page_icon="🔍",
    layout="wide"
)

# Apply custom styles
apply_custom_styles()

# Header
st.markdown("<h1 class='main-header'>🔍 LinkedIn Job Scraper with Resume Matcher</h1>", unsafe_allow_html=True)
st.markdown("Find the perfect job match based on your resume and LinkedIn job listings")

# Create two columns for search parameters
col1, col2 = st.columns([2, 1])

with col1:
    # Job search parameters
    st.markdown("<div class='section-header'>🔎 Job Search Parameters</div>", unsafe_allow_html=True)
    keyword = st.text_input("Enter job title or keyword:", placeholder="e.g., Web Developer, Data Scientist")
    
    # Additional filters in an expander
    with st.expander("Advanced Search Options"):
        location = st.text_input("Location:", placeholder="e.g., New York, Remote")
        experience_level = st.multiselect(
            "Experience Level:",
            ["Entry level", "Associate", "Mid-Senior level", "Director", "Executive"],
            default=None
        )
        job_type = st.multiselect(
            "Job Type:",
            ["Full-time", "Part-time", "Contract", "Temporary", "Internship"],
            default=["Full-time"]
        )

with col2:
    st.markdown("<div class='section-header'>📄 Resume Upload</div>", unsafe_allow_html=True)
    
    upload_option = st.radio("Choose resume input method:", ("Upload File", "Paste Text"))
    st.markdown("<p style='color: red; font-weight: 600;'>Note that the document uploading function is not working</p>", unsafe_allow_html=True)
    
    resume_text = ""
    if upload_option == "Upload File":
        resume_file = st.file_uploader("Upload your resume", type=["pdf", "docx", "txt"])
        
        if resume_file is not None:
            file_details = {"Filename": resume_file.name, "FileType": resume_file.type, "FileSize": f"{resume_file.size / 1024:.2f} KB"}
            st.write(file_details)
            
            try:
                resume_text = extract_text_from_file(resume_file)
                st.success("Resume successfully processed!")
            except Exception as e:
                st.error(f"Error processing file: {str(e)}")
    else:
        resume_text = st.text_area("Paste your resume text:", height=200, placeholder="Copy and paste your resume here...")

search_col1, search_col2 = st.columns([3, 1])
with search_col1:
    search_button = st.button("🔍 Search Jobs", use_container_width=True)

if search_button:
    if keyword.strip():
        with st.spinner("Fetching and analyzing job listings... This may take a moment."):
            #calling scraper
            job_listings = detect_job_cards_with_description(keyword, location=location)
            
            if job_listings:
                #resume matcher
                for job in job_listings:
                    if resume_text:
                        matcher = ResumeMatcher(job["description"])
                        match_result = matcher.match_resume(resume_text)
                        job["similarity_score"] = match_result["similarity_score"]
                        job["missing_skills"] = match_result["missing_skills"]
                        job["matched_skills"] = match_result.get("matched_skills", [])
                    else:
                        job["similarity_score"] = 0
                        job["missing_skills"] = []
                        job["matched_skills"] = []
                
                #Sorting by % match
                print(job["missing_skills"], job["matched_skills"])
                if resume_text:
                    job_listings.sort(key=lambda x: x["similarity_score"], reverse=True)
                
                st.markdown(f"<div class='section-header'>📊 Results: Found {len(job_listings)} Job Listings</div>", unsafe_allow_html=True)
                tab1, tab2 = st.tabs(["Card View", "Table View"])
                
                with tab1:
                    for idx, job in enumerate(job_listings):
                        render_job_card(job, idx, resume_text)
                
                with tab2:
                    job_df = pd.DataFrame(job_listings)
                    if "similarity_score" in job_df.columns:
                        job_df["match_percentage"] = job_df["similarity_score"].apply(lambda x: f"{x:.0%}")
                    
                    display_cols = ["title", "company"]
                    if resume_text:
                        display_cols.append("match_percentage")
                    
                    st.dataframe(
                        job_df[display_cols],
                        use_container_width=True,
                        column_config={
                            "title": "Job Title",
                            "company": "Company",
                            "match_percentage": "Match Score"
                        }
                    )
            else:
                st.warning("⚠️ No jobs found matching your search criteria. Try broadening your search.")
    else:
        st.error("⚠️ Please enter a valid job keyword to start your search.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center">
    <p>Built with Streamlit | Data sourced from LinkedIn</p>
    <p>Remember to use this tool responsibly and in accordance with LinkedIn's terms of service.</p>
</div>
""", unsafe_allow_html=True)
