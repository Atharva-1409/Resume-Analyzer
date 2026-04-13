from parser import extract_text_from_pdf, extract_data
from db import insert_candidate, get_candidates
from analyzer import rank_candidates

def add_candidate():
    path = input("Enter resume PDF path: ")
    text = extract_text_from_pdf(path)
    data = extract_data(text)
    insert_candidate(data)
    print("Candidate added:", data["name"])

def view_candidates():
    data = get_candidates()
    for c in data:
        print(c)

def rank():
    job = {
        "title": "Software Intern",
        "required_skills": "python,sql,java",
        "min_experience": 1
    }

    candidates = get_candidates()
    ranked = rank_candidates(candidates, job)

    print("\n--- Ranking ---")
    for name, score in ranked:
        print(name, "→", score)

def main():
    while True:
        print("\n1. Add Candidate")
        print("2. View Candidates")
        print("3. Rank Candidates")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_candidate()
        elif choice == "2":
            view_candidates()
        elif choice == "3":
            rank()
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
