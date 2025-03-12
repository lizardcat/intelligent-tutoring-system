import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect("db.sqlite3")
    return conn

# Fetch student performance data
def get_student_performance(student_id):
    conn = get_db_connection()
    df = pd.read_sql_query(f"SELECT * FROM student_progress WHERE student_id = '{student_id}'", conn)
    conn.close()
    return df

# Display performance trends
def show_performance_dashboard():
    st.title("📊 Student Performance Dashboard")
    
    # Ensure user has a session-based ID
    if "student_id" not in st.session_state:
        st.warning("Session ID is missing. Please restart the app.")
        return

    student_id = st.session_state["student_id"]

    df = get_student_performance(student_id)
    
    if df.empty:
        st.warning("No performance data found.")
        return
    
    # Calculate key metrics
    total_attempts = df.shape[0]
    correct_attempts = df[df['is_correct'] == 1].shape[0]
    accuracy = (correct_attempts / total_attempts) * 100 if total_attempts > 0 else 0
    
    st.metric("Total Attempts", total_attempts)
    st.metric("Correct Answers", correct_attempts)
    st.metric("Accuracy", f"{accuracy:.2f}%")
    
    # Performance trend graph
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')
    df['correct_count'] = df['is_correct'].cumsum()
    
    fig, ax = plt.subplots()
    ax.plot(df['timestamp'], df['correct_count'], marker='o', linestyle='-')
    ax.set_title("Performance Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Cumulative Correct Answers")
    ax.grid(True)
    
    st.pyplot(fig)

if __name__ == "__main__":
    show_performance_dashboard()
