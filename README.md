# 📄 Smart Resume Analyzer (Python + MySQL)

A resume analysis system built using Python and MySQL that parses PDF resumes, extracts structured candidate data, stores it in a relational database, and ranks candidates based on job-specific criteria using a rule-based scoring engine.

---

## 🚀 Features

* 🔹 PDF resume parsing using PyPDF2
* 🔹 Automatic extraction of name, email, skills, and experience
* 🔹 MySQL database integration for persistent storage
* 🔹 Multi-candidate ranking system
* 🔹 CLI-based admin panel
* 🔹 Rule-based scoring (transparent and explainable)

---

## 🧠 Concepts Used

* File handling and PDF parsing
* Regular expressions (data extraction)
* Relational databases (MySQL)
* SQL queries (INSERT, SELECT)
* Data processing and ranking algorithms
* CLI-based application design

---

## 🏗️ Project Structure

```
resume-analyzer/
│
├── main.py            # CLI interface
├── parser.py          # Resume parsing logic
├── analyzer.py        # Scoring and ranking
├── db.py              # Database operations
├── schema.sql         # MySQL schema
├── sample_resumes/    # Test resumes
└── README.md
```

---

## ⚙️ How It Works

1. Upload or provide a resume (PDF format)
2. Extract raw text from the resume
3. Parse key details (name, email, skills, experience)
4. Store candidate data in MySQL database
5. Compare candidates against job requirements
6. Rank candidates based on matching score

---

## ▶️ How to Run

### 🔧 Install Dependencies

```bash
pip install PyPDF2 mysql-connector-python
```

### 🗄️ Setup Database

```sql
CREATE DATABASE resume_db;
USE resume_db;

CREATE TABLE candidates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    skills TEXT,
    experience INT
);
```

### ▶️ Run Application

```bash
python main.py
```

---

## 🖼️ Sample CLI

```
1. Add Candidate
2. View Candidates
3. Rank Candidates
4. Exit
```

---

## 📊 Scoring Logic

* Skill match → +15 per matching skill
* Experience match → +25 if requirement met
* Experience below requirement → -10 penalty

---

## 🔥 Future Improvements

* Web interface using Flask
* Resume upload via browser
* Advanced NLP-based skill extraction
* Weighted scoring system
* Export rankings to CSV
* Authentication system for admin

---

## 💡 Why This Project?

This project demonstrates practical backend development skills by combining data extraction, database management, and algorithmic ranking into a real-world use case.

It is ideal for:

* Learning backend systems
* Understanding data pipelines
* Showcasing full-stack potential (with future UI)
* Strengthening GitHub portfolio

---

## 📌 Author

**Atharva Sable**

---

## ⭐ Contributing

Contributions are welcome! Fork the repo and submit pull requests.

---

## 📄 License

This project is open-source under the MIT License.
