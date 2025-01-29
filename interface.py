import streamlit as st
import time
from scraper import detect_job_cards_with_description
from resume_matcher import ResumeMatcher



st.title("🔍 LinkedIn Job Scraper with Resume Matching")

keyword = st.text_input("Enter a job keyword:", placeholder="e.g., Web Developer")
resume_text = st.text_area("Paste your resume (optional):", placeholder="Copy and paste your resume here...")

if st.button("Search Jobs"):
    if keyword.strip():
        with st.spinner("Fetching job listings..."):
            job_listings = detect_job_cards_with_description(keyword)

        if job_listings:
            st.success(f"✅ Found {len(job_listings)} job(s) for '{keyword}'")

            for job in job_listings:
                matcher = ResumeMatcher(job["description"])
                match_result = matcher.match_resume(resume_text)

                job["similarity_score"] = match_result["similarity_score"]
                job["missing_skills"] = match_result["missing_skills"]

            job_listings.sort(key=lambda x: x["similarity_score"], reverse=True)

            for job in job_listings:
                st.subheader(job["title"])
                st.text(f"🏢 Company: {job['company']}")
                st.write(f"📝 **Description:** {job['description']}")
                st.write(f"📊 **Resume Match Score:** {job['similarity_score']:.2f}")

                if job["missing_skills"]:
                    st.warning(f"⚠️ **Missing Skills:** {', '.join(job['missing_skills'])}")
                else:
                    st.success("✅ You match all the listed skills!")

                st.write("---")
        else:
            st.warning("No jobs found.")
    else:
        st.error("Please enter a valid keyword.")
