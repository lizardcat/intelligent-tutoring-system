# Intelligent Tutoring System

The Intelligent Tutoring System is a web-based application that provides an adaptive learning experience using a knowledge-based system. It allows students to answer questions, receive instant feedback, and track their performance. Administrators can add and manage questions dynamically.

## Features
- Adaptive questioning based on student performance
- Immediate feedback on submitted answers
- Performance tracking with visual analytics
- Admin panel for managing questions
- Supports multiple question types (MCQs, fill-in-the-blank, and word problems)

## Live Demo
The application is deployed on Streamlit Cloud. You can access it here:  
[https://intelligent-tutoring-system.streamlit.app/](https://intelligent-tutoring-system.streamlit.app/)

## Installation and Setup

### 1. Clone the Repository
```sh
git clone https://github.com/lizardcat/intelligent_tutoring_system.git
```
```sh
cd intelligent_tutoring_system
```

### 2. Install Dependencies

Ensure you have Python installed, then install the required packages:

```sh
pip install -r requirements.txt
```

### 3. Set Up the Database

Initialize the SQLite database and load default questions:
```sh
python database.py
```

### 4. Run the Application

Start the Streamlit server:
```sh
streamlit run main.py
```

### 5. Access the App

Once the server is running, open the displayed URL in your browser to interact with the system.