# Resume Matcher with LinkedIn Job Scraper

## 🚀 Overview

This open-source project provides a **LinkedIn Job Scraper** combined with a **Resume Matcher** that evaluates how well a given resume aligns with job descriptions. It helps job seekers find relevant job postings and assess their suitability using a **TF-IDF-based similarity model**.

## 🔧 Features

- 🔍 **LinkedIn Job Scraper**: Extracts job listings based on a keyword search.
- 📊 **Resume Matching**: Uses TF-IDF and cosine similarity to compare job descriptions with a user's resume.
- 🏆 **Skill Analysis**: Identifies missing skills from the resume compared to the job description.
- 🖥 **Streamlit Interface**: A user-friendly web UI for easy interaction.

---

## 📁 Project Structure

```
resume-matcher/
│── scraper.py          # Scrapes LinkedIn job postings based on a keyword
│── resume_matcher.py   # Matches resume content with job descriptions using TF-IDF
│── interface.py        # Streamlit-based UI for user interaction
│── requirements.txt    # Dependencies required to run the project
│── README.md           # Project documentation
```

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/resume-matcher.git
cd resume-matcher
```

### 2️⃣ Install Dependencies

Ensure you have Python installed (>=3.7), then install required libraries:

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

- in your command prompt, run :

```
streamlit run interface.py
```

---

## 📜 How It Works

### 🕵️ 1. Scraping LinkedIn Jobs

- The **scraper.py** fetches job listings based on a given keyword.
- It requires the correct selectors from the HTML of Linkedin
- The extracted data includes:
  - Job Title
  - Company Name
  - Job Description

### 🎯 2. Resume Matching

- The **resume_matcher.py** applies **TF-IDF** and **cosine similarity** to measure how well a resume aligns with a job description.
- Outputs:
  - **Match Score** (0-1 scale)
  - **Missing Skills** (skills in the job description but absent in the resume)

### 🖥️ 3. Streamlit UI

- The **interface.py** provides a web-based UI for user-friendly interaction.
- Users can:
  - Enter a job keyword to search LinkedIn.
  - Paste their resume.
  - View job listings ranked by match score.
  - See missing skills in their resume.

---

## 🫵 Your Part In This

- The project currently opens the browser physically which can be avoided
- Some of the css selectors for scraping the job listings are missing without which the scraper wont function
- You'll have to dive into the inspect menu in your browser for Linkedin to find those selectors
- The selectors could be the class or the data test id
- optionally : You could always imporve the interface and the model performance, as well as make the scraper target more specific areas of interest
