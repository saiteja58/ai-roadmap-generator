import streamlit as st
import random
import google.generativeai as genai

genai.configure(api_key='AIzaSyCBJqOQHl-I-dM3Y9TJKwPjSFpSSwDH2Xg')
model = genai.GenerativeModel("gemini-1.5-flash")
image_path = 'logo.png'

# Display image
st.image(image_path, caption="Select you Path By your own way", width=250)

# Initialize session state
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False
if 'selected_questions' not in st.session_state:
    st.session_state.selected_questions = []
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

# ... [Keep your existing questions_data and roadmap_data dictionaries] ...


import json

# Load questions from JSON file
with open('questions.json', 'r', encoding='utf-8') as f:
    questions_data = json.load(f)

# Remove the original questions_data dictionary from your code

# Roadmap steps for each course based on score percentage
roadmap_data = {
    'Data Science': {
        'low': ["Step 1: Learn Python Basics", "Step 2: Learn Data Structures and Algorithms", "Step 3: Learn Data Analysis with Pandas", "Step 4: Learn Visualization with Matplotlib"],
        'medium': ["Step 1: Learn Machine Learning Algorithms", "Step 2: Learn Deep Learning Fundamentals", "Step 3: Learn Data Science Tools (Jupyter, NumPy, etc.)"],
        'high': ["Step 1: Master Advanced Machine Learning", "Step 2: Learn Natural Language Processing", "Step 3: Get Hands-on with Data Science Projects", "Step 4: Contribute to Open-Source Data Science Projects"]
    },
    'Software Development': {
        'low': ["Step 1: Learn Programming Fundamentals", "Step 2: Learn Object-Oriented Programming", "Step 3: Learn Web Development Basics (HTML, CSS, JavaScript)"],
        'medium': ["Step 1: Learn Backend Development (Node.js, Django, etc.)", "Step 2: Learn Full-Stack Development", "Step 3: Work on Projects"],
        'high': ["Step 1: Learn Advanced Topics (Microservices, Cloud computing)", "Step 2: Work on High-Scale Applications", "Step 3: Contribute to Open-Source Projects"]
    },
    'AI Engineer': {
        'low': ["Step 1: Learn Python for AI", "Step 2: Learn Data Science and Basic ML Algorithms", "Step 3: Get Hands-on with Neural Networks and Deep Learning"],
        'medium': ["Step 1: Learn Reinforcement Learning", "Step 2: Work on AI Projects", "Step 3: Learn Advanced Machine Learning Algorithms"],
        'high': ["Step 1: Master AI Deployment", "Step 2: Contribute to AI Research", "Step 3: Develop State-of-the-Art AI Models"]
    }
}

def main():
    st.title('AI Roadmap Generator')
    course = st.selectbox('Select your course:', ['Data Science', 'Software Development', 'AI Engineer'])

    if not st.session_state.quiz_started:
        if st.button('Start Quiz'):
            st.session_state.quiz_started = True
            questions = questions_data.get(course, [])
            st.session_state.selected_questions = random.sample(questions, 15) if len(questions) > 15 else questions
            st.session_state.user_answers = {}

    if st.session_state.quiz_started and not st.session_state.quiz_submitted:
        display_quiz(course)
        if st.button('Submit Quiz'):
            st.session_state.quiz_submitted = True
            calculate_and_display_results(course)

    if st.session_state.quiz_submitted:
        if st.button('Restart Quiz'):
            st.session_state.quiz_started = False
            st.session_state.quiz_submitted = False
            st.session_state.selected_questions = []
            st.session_state.user_answers = {}
            st.rerun()

def display_quiz(course):
    st.write(f"### Quiz for {course}")
    for i, q in enumerate(st.session_state.selected_questions, 1):
        st.write(f"{i}. {q['question']}")
        answer = st.radio(
            f"Select answer for Question {i}",
            q['options'],
            key=f"q{i}",
            index=None  # Add this to show unselected state
        )
        st.session_state.user_answers[f"q{i}"] = answer

def calculate_and_display_results(course):
    correct_answers = 0
    for i, q in enumerate(st.session_state.selected_questions, 1):
        if st.session_state.user_answers.get(f"q{i}") == q["answer"]:
            correct_answers += 1
    
    total_questions = len(st.session_state.selected_questions)
    percentage = (correct_answers / total_questions) * 100
    st.write(f"### Your Score: {correct_answers}/{total_questions} ({percentage:.2f}%)")
    
    if percentage >= 80:
        stage = 'high'
    elif percentage >= 50:
        stage = 'medium'
    else:
        stage = 'low'
    
    display_roadmap(course, stage)

def display_roadmap(course, stage):
    prompt = f"I have {stage} knowledge on {course} and want to master it. Provide a step-by-step guide with resources."
    response = model.generate_content(prompt)
    
    st.write("### AI-Generated Roadmap:")
    st.write(response.text)
    
    st.write("### Structured Roadmap:")
    for step in roadmap_data[course][stage]:
        st.write(f"- {step}")

if __name__ == "__main__":
    main()