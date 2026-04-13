import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="resume_db"
    )

def insert_candidate(candidate):
    conn = connect()
    cursor = conn.cursor()

    query = """
    INSERT INTO candidates (name, email, skills, experience)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (
        candidate["name"],
        candidate["email"],
        candidate["skills"],
        candidate["experience"]
    ))

    conn.commit()
    conn.close()

def get_candidates():
    conn = connect()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM candidates")
    data = cursor.fetchall()

    conn.close()
    return data
