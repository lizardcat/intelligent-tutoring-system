import streamlit as st
import sqlite3
import random
import json
import pandas as pd

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect("db.sqlite3")
    conn.row_factory = sqlite3.Row
    return conn

# Fetch a random question from the database
def get_random_question():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 1")
    question = cursor.fetchone()
    conn.close()
    return question

# Store student performance
def store_student_performance(student_id, question_id, is_correct):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO student_progress (student_id, question_id, is_correct, timestamp)
        VALUES (?, ?, ?, datetime('now'))
    """, (student_id, question_id, is_correct))
    conn.commit()
    conn.close()

# Streamlit UI
def main():
    st.title("🧠 Intelligent Tutoring System")

    # Ensure user has a session-based ID
    if "student_id" not in st.session_state:
        st.warning("Session ID is missing. Please restart the app.")
        return

    student_id = st.session_state["student_id"]

    # Question Handling
    if "current_question" not in st.session_state or "answered" not in st.session_state:
        st.session_state.current_question = get_random_question()
        st.session_state.answered = False

    question = st.session_state.current_question

    if question:
        st.write("### Question:")
        st.write(question["question"])

        # If the question is MCQ, show buttons
        if question["type"] == "mcq":
            options = json.loads(question["options"])
            answer = st.radio("Select your answer:", options, key="answer_input")
        else:
            answer = st.text_input("Your answer:", key="answer_input")

        if st.button("Submit Answer") and not st.session_state.answered:
            correct_answer = question["answer"]
            is_correct = (str(answer).strip().lower() == str(correct_answer).strip().lower())

            # Store response
            store_student_performance(student_id, question["id"], int(is_correct))

            if is_correct:
                st.success("🎉 Correct!")
            else:
                st.error(f"❌ Incorrect. The correct answer is {correct_answer}")

            # Mark as answered
            st.session_state.answered = True

    if st.session_state.answered:
        if st.button("Next Question"):
            st.session_state.current_question = get_random_question()
            st.session_state.answered = False
            st.rerun()
    
    else:
        st.write("Please submit your answer before proceeding to the next question.")

    # Performance Tracking
    st.sidebar.subheader("📊 Your Performance")
    conn = get_db_connection()
    df = pd.read_sql_query(f"SELECT * FROM student_progress WHERE student_id = '{student_id}'", conn)
    conn.close()

    if not df.empty:
        correct_count = df[df['is_correct'] == 1].shape[0]
        total_attempts = df.shape[0]
        accuracy = (correct_count / total_attempts) * 100
        st.sidebar.metric("Accuracy", f"{accuracy:.2f}%")
    
if __name__ == "__main__":
    main()
