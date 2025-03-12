import streamlit as st
import uuid  # Generates unique session-based user IDs

# Set Streamlit page config (MUST be first)
st.set_page_config(page_title="Intelligent Tutoring System", page_icon="🧠")

# Import modules after setting the config
from student_performance import show_performance_dashboard
from admin_panel import admin_panel
from student_interface import main as student_main

# Assign a unique session ID if not set
if "student_id" not in st.session_state:
    st.session_state["student_id"] = str(uuid.uuid4())  # Assigns a random UUID

# Sidebar Navigation
st.sidebar.title("🧠 Intelligent Tutoring System")
st.sidebar.markdown("""
This is a project for a **Knowledge-Based Systems (KBS) class**, designed to provide an intelligent tutoring experience. Full implementation available on GitHub [here](https://github.com/lizardcat/intelligent_tutoring_system).

**Features:**
- 📚 Adaptive questioning: Adjusts difficulty based on performance.
- ✅ Immediate feedback: Provides instant results.
- 📊 Performance tracking: Tracks and visualizes progress.

**Navigation:**
- **Student Interface:** Answer questions and receive feedback.
- **Performance Dashboard:** View progress over time.
- **Admin Panel:** Manage and add new questions.
""")

page = st.sidebar.radio("**Go to:**", ["Student Interface", "Performance Dashboard", "Admin Panel"])

if page == "Student Interface":
    student_main()
elif page == "Performance Dashboard":
    show_performance_dashboard()
elif page == "Admin Panel":
    admin_panel()

# Logout Button (Clears Session)
if st.sidebar.button("Reset Session"):
    st.session_state.clear()  # Clears session state
    st.rerun()
