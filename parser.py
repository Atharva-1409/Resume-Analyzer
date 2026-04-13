import re
import PyPDF2

SKILLS_DB = [
    "python", "java", "c++", "sql", "html", "css",
    "javascript", "react", "node", "mysql", "mongodb"
]

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_data(text):
    name = text.split("\n")[0]

    email = re.findall(r'\S+@\S+', text)
    email = email[0] if email else ""

    skills = [skill for skill in SKILLS_DB if skill in text.lower()]

    experience = len(re.findall(r"year", text.lower()))

    return {
        "name": name,
        "email": email,
        "skills": ",".join(skills),
        "experience": experience
    }
