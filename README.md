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
│── frontend/                # Frontend-related code and UI components  
│   ├── app.py               # Main application script for the frontend  
│   ├── ui_components.py     # UI-related functions and components  
│   ├── utils.py             # Utility functions for frontend operations  
│── .gitignore               # Files and folders to be ignored by Git  
│── LICENSE                  # License information for the project  
│── linkedin_jobs.json       # JSON file containing scraped LinkedIn job data  
│── main.py                  # Main script which runs the streamlit application via cmd 
│── README.md                # Project documentation and instructions  
│── requirements.txt         # List of dependencies required for the project  
│── resume_matcher.py        # Script for matching resumes with job descriptions  
│── scraper.py               # Script for scraping job listings from LinkedIn  

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
python -u main.py
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

The **frontend/app.py** provides a web-based UI for user-friendly interaction.  
- Upload a resume in **PDF or TXT** format (*PDF support is not fully functional yet*).  
- Enter a **job keyword** to search LinkedIn.  
- View **job listings ranked by match score**.  
- Use the **advanced search function** (*currently not working*).  


---

## 🫵 Your Part In This

- The project currently opens the browser physically which can be avoided
- Some of the css selectors for scraping the job listings are missing without which the scraper wont function
- You'll have to dive into the inspect menu in your browser for Linkedin to find those selectors
- The selectors could be the class or the data test id
- optionally : You could always imporve the interface and the model performance, as well as make the scraper target more specific areas of interest
