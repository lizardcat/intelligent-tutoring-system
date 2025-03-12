import streamlit as st
import sqlite3
import json
import pandas as pd

# Connect to database
def get_db_connection():
    conn = sqlite3.connect("db.sqlite3")
    return conn

# Insert new question into database
def add_question(q_type, question, options, answer, difficulty):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO questions (type, question, options, answer, difficulty)
            VALUES (?, ?, ?, ?, ?)
        """, (q_type, question, json.dumps(options), answer, difficulty))
        conn.commit()

        st.success("✅ Question added successfully!")

        update_questions_json()

        # Refresh UI
        st.rerun()
    except Exception as e:
        st.error(f"❌ Error adding question: {e}")
    
    conn.close()

# Fetch all questions
def get_all_questions():
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM questions", conn)
    conn.close()
    return df

# Delete a question
def delete_question(question_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM questions WHERE id = ?", (question_id,))
    conn.commit()
    conn.close()

    st.warning("⚠️ Question deleted!")
    update_questions_json()  # Update JSON after deletion
    st.rerun()

# ✅ Function to update questions.json after changes
def update_questions_json():
    df = get_all_questions()
    questions = df.to_dict(orient="records")

    # Convert options back to list format
    for q in questions:
        if q["type"] == "mcq":
            q["options"] = json.loads(q["options"])

    with open("data/questions.json", "w", encoding="utf-8") as file:
        json.dump({"questions": questions}, file, indent=4)

# Streamlit UI for Admin Panel
def admin_panel():
    st.title("🧙‍♂️ Admin Panel - Manage Questions")
    st.subheader("Add a New Question")

    # Question form
    q_type = st.selectbox("Select Question Type", ["mcq", "fill_in_blank", "word_problem"])
    question = st.text_area("Enter the question:")
    
    options = []
    if q_type == "mcq":
        st.write("Enter MCQ options:")
        option1 = st.text_input("Option 1")
        option2 = st.text_input("Option 2")
        option3 = st.text_input("Option 3")
        option4 = st.text_input("Option 4")
        
        # Ensure no empty options
        options = [opt.strip() for opt in [option1, option2, option3, option4] if opt.strip()]
        if len(options) < 2:
            st.warning("⚠️ MCQ must have at least two valid options.")

    answer = st.text_input("Enter the correct answer:")
    difficulty = st.selectbox("Select Difficulty", ["easy", "medium", "hard"])
    
    if st.button("Add Question"):
        if not question.strip():
            st.error("❌ Question cannot be empty!")
        elif q_type == "mcq" and len(options) < 2:
            st.error("❌ MCQ must have at least two valid options!")
        elif not answer.strip():
            st.error("❌ Answer cannot be empty!")
        else:
            add_question(q_type, question, options, answer, difficulty)

    st.subheader("Existing Questions")
    df = get_all_questions()

    if not df.empty:
        for index, row in df.iterrows():
            with st.expander(f"{row['question']} (ID: {row['id']})"):
                st.write(f"**Type:** {row['type']}")
                st.write(f"**Difficulty:** {row['difficulty']}")
                
                if row['type'] == "mcq":
                    options = json.loads(row['options'])
                    st.write(f"**Options:** {', '.join(options)}")
                
                st.write(f"**Answer:** {row['answer']}")

                # Delete Button
                if st.button(f"❌ Delete", key=f"delete_{row['id']}"):
                    delete_question(row['id'])
    else:
        st.write("No questions added yet.")

if __name__ == "__main__":
    admin_panel()
