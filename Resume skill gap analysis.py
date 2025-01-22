import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Predefined list of skill categories
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
        # Fit the vectorizer on the job description
        self.job_tfidf = self.vectorizer.fit_transform([job_description])

    def match_resume(self, resume_text):
        # Transform the resume using the same vectorizer
        resume_tfidf = self.vectorizer.transform([resume_text])
        # Compute cosine similarity
        similarity = cosine_similarity(self.job_tfidf, resume_tfidf)[0][0]

        # Extract skills from job description and resume
        job_skills = self.extract_skills(self.job_description)
        resume_skills = self.extract_skills(resume_text)

        # Identify missing skills
        missing_skills = job_skills - resume_skills

        return {
            "similarity_score": similarity,
            "missing_skills": list(missing_skills)
        }

    @staticmethod
    def extract_skills(text):
        # Extract skills from text by checking for matches with predefined SKILL_SET
        text = text.lower()
        skills = {skill.lower() for skill in SKILL_SET if skill.lower() in text}
        return skills

# Example usage
job_description = """
We are looking for a candidate with strong expertise in Project Management,
Marketing, Design, and Quality Assurance. The candidate should also have experience in Sales
and Information Technology. Strong communication skills and teamwork are a plus.
"""

resume_text = """
Experienced marketing professional with expertise in Sales and Quality Assurance.
Skilled in communication and teamwork, with a focus on customer service.
"""

matcher = ResumeMatcher(job_description)
result = matcher.match_resume(resume_text)

print(f"Similarity Score: {result['similarity_score']:.2f}")
print(f"Missing Skills: {', '.join(result['missing_skills'])}")

