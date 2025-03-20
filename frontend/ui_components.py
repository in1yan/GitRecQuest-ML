import streamlit as st

def apply_custom_styles():
    """Apply custom CSS styling to the Streamlit app"""
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #0077B5;
        margin-bottom: 1rem;
    }
    .job-card {
        background-color: #f7f9fc;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        border-left: 5px solid #0077B5;
    }
    .job-title {
        color: #0077B5;
        margin-bottom: 5px;
    }
    .company-name {
        font-weight: 500;
        color: #333;
    }
    .match-score-high {
        color: #28a745;
        font-weight: bold;
    }
    .match-score-medium {
        color: #ffc107;
        font-weight: bold;
    }
    .match-score-low {
        color: #dc3545;
        font-weight: bold;
    }
    .section-header {
        background-color: #0077B5;
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def render_job_card(job, idx, resume_text=""):
    """
    Render a job listing as a card
    
    Args:
        job (dict): Job listing information
        idx (int): Index for unique keys
        resume_text (str): Resume text if provided
    """
    with st.container():
        st.markdown(f"""
        <div class='job-card'>
            <h3 class='job-title'>{job["title"]}</h3>
            <p class='company-name'>🏢 {job["company"]}</p>
        </div>
        """, unsafe_allow_html=True)
        
        score = job.get("similarity_score", 0)
        score_class = "match-score-high" if score >= 0.7 else "match-score-medium" if score >= 0.4 else "match-score-low"
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if resume_text:
                st.markdown(f"<p>📊 <span class='{score_class}'>Resume Match: {score:.0%}</span></p>", unsafe_allow_html=True)
        with col2:
            st.button(f"Apply Now", key=f"apply_{idx}")
        
        with st.expander("View Job Description"):
            st.write(job["description"])
        
        if resume_text:
            skill_col1, skill_col2 = st.columns(2)
            
            with skill_col1:
                if job.get("matched_skills"):
                    st.markdown("✅ **Matched Skills:**")
                    st.write(", ".join(job["matched_skills"]))
                else:
                    st.info("No skill matches found.")
                    
            with skill_col2:
                if job.get("missing_skills"):
                    st.markdown("⚠️ **Skills to Develop:**")
                    st.write(", ".join(job["missing_skills"]))
                else:
                    st.success("You match all the required skills!")
        
        st.markdown("---")