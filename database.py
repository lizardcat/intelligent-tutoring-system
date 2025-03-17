import sqlite3
import json
import os

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect("db.sqlite3")
    return conn
#qwerty
# Create tables for questions and student progress
def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Table for storing questions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            question TEXT NOT NULL UNIQUE,
            options TEXT,
            answer TEXT NOT NULL,
            difficulty TEXT
        )
    ''')
    
    # Table for tracking student responses
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,  -- Using session-based IDs
            question_id INTEGER NOT NULL,
            is_correct INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

# Load default questions from JSON file
def load_default_questions():
    json_path = "data/questions.json"
    
    if not os.path.exists(json_path):
        print("⚠️ No default questions file found. Skipping loading questions.")
        return
    
    with open(json_path, "r", encoding="utf-8") as file:
        questions = json.load(file).get("questions", [])

    conn = get_db_connection()
    cursor = conn.cursor()

    for q in questions:
        options = json.dumps(q.get("options", []))  # Defaults to [] if "options" key is missing

        try:
            cursor.execute("""
                INSERT INTO questions (type, question, options, answer, difficulty) 
                VALUES (?, ?, ?, ?, ?)""",
                (q["type"], q["question"], options, q["answer"], q.get("difficulty", "medium"))
            )
        except sqlite3.IntegrityError:
            print(f"⚠️ Question already exists: {q['question']}")

    conn.commit()
    conn.close()

# Ensure tables are created on every run
create_tables()

if __name__ == "__main__":
    load_default_questions()
    print("✅ Database setup complete!")
