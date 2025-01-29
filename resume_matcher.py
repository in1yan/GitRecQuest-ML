import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


SKILL_SET = [
    "Art/Creative", "Design", "Advertising", "Product Management", "Distribution",
    "Education", "Training", "Project Management", "Consulting", "Purchasing",
    "Supply Chain", "Analyst", "Health Care Provider", "Research", "Science",
    "General Business", "Customer Service", "Strategy/Planning", "Finance", "Other",
    "Legal", "Engineering", "Quality Assurance", "Business Development",
    "Information Technology", "Administrative", "Production", "Marketing",
    "Public Relations", "Writing/Editing", "Accounting/Auditing", "Human Resources",
    "Manufacturing", "Sales", "Management"
]

class ResumeMatcher:
    def __init__(self, job_description):
        self.job_description = job_description
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.job_tfidf = self.vectorizer.fit_transform([job_description])

    def match_resume(self, resume_text):
        if not resume_text.strip():
            return {"similarity_score": 0.0, "missing_skills": []}

        resume_tfidf = self.vectorizer.transform([resume_text])
        similarity = cosine_similarity(self.job_tfidf, resume_tfidf)[0][0]

        job_skills = self.extract_skills(self.job_description)
        resume_skills = self.extract_skills(resume_text)
        missing_skills = job_skills - resume_skills

        return {
            "similarity_score": similarity,
            "missing_skills": list(missing_skills)
        }

    @staticmethod
    def extract_skills(text):
        text = text.lower()
        return {skill.lower() for skill in SKILL_SET if skill.lower() in text}
