import sqlite3
import json
import hashlib  # For password hashing

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect("db.sqlite3")
    return conn

# Create tables for questions, student progress, and student accounts
def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Table for storing questions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            question TEXT NOT NULL,
            options TEXT,
            answer TEXT NOT NULL,
            difficulty TEXT
        )
    ''')
    
    # Table for tracking student responses
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            question_id INTEGER NOT NULL,
            is_correct INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

# Load default questions from JSON file
def load_default_questions():
    with open("data/questions.json", "r", encoding="utf-8") as file:
        questions = json.load(file)["questions"]

    conn = get_db_connection()
    cursor = conn.cursor()

    for q in questions:
        options = json.dumps(q.get("options", []))  # Defaults to [] if "options" key is missing

        cursor.execute("""
            INSERT INTO questions (type, question, options, answer, difficulty) 
            VALUES (?, ?, ?, ?, ?)""",
            (q["type"], q["question"], options, q["answer"], q.get("difficulty", "medium"))
        )

    conn.commit()
    conn.close()

# Hash passwords for security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Add a new student (Register)
def add_student(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO students (username, password) VALUES (?, ?)", (username, hash_password(password)))
        conn.commit()
        print(f"✅ Student '{username}' registered successfully!")
    except sqlite3.IntegrityError:
        print(f"⚠️ Username '{username}' already exists!")
    
    conn.close()

# Authenticate student login
def authenticate_student(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, password FROM students WHERE username=?", (username,))
    student = cursor.fetchone()
    
    conn.close()
    
    if student and student[1] == hash_password(password):
        return student[0]  # Return student ID if credentials match
    else:
        return None  # Invalid login

if __name__ == "__main__":
    create_tables()
    load_default_questions()
    print("✅ Database setup complete!")