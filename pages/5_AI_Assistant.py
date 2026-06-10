import streamlit as st
import random

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Career Assistant")
st.write(
    "Ask anything about placements, AIML, careers, interviews, projects, or skills."
)

# ------------------------------------------------
# CHAT HISTORY
# ------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ------------------------------------------------
# USER INPUT
# ------------------------------------------------
prompt = st.chat_input(
    "Ask a career question..."
)

if prompt:

    # user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    question = prompt.lower()

    # ------------------------------------------------
    # AI RESPONSES
    # ------------------------------------------------
    response = ""

    # AIML projects
    if "project" in question or "aiml project" in question:

        projects = [
            "🤖 AI Resume Analyzer",
            "📰 Fake News Detection",
            "🎬 Movie Recommendation System",
            "💬 NLP Chatbot",
            "🧠 Disease Prediction System",
            "📈 Stock Price Prediction",
            "🎤 Voice Assistant",
            "📷 Face Recognition Attendance System"
        ]

        response = (
            "Here are strong AIML projects for your resume:\n\n"
            + "\n".join(projects)
        )

    # ML roadmap
    elif "machine learning" in question or "ml roadmap" in question:

        response = """
### 🚀 Machine Learning Roadmap

1️⃣ Python Basics  
2️⃣ NumPy + Pandas  
3️⃣ SQL  
4️⃣ Statistics  
5️⃣ Machine Learning Algorithms  
6️⃣ Deep Learning  
7️⃣ Projects  
8️⃣ Deployment  
9️⃣ Kaggle Practice
"""

    # Data scientist roadmap
    elif "data scientist" in question:

        response = """
### 📊 Data Scientist Roadmap

1️⃣ Python  
2️⃣ SQL  
3️⃣ Statistics  
4️⃣ Data Visualization  
5️⃣ Machine Learning  
6️⃣ Deep Learning  
7️⃣ Projects  
8️⃣ Portfolio Building
"""

    # Placement prep
    elif "placement" in question:

        response = """
### 🎯 Placement Preparation

✅ DSA (Leetcode)  
✅ Aptitude  
✅ Resume Projects  
✅ SQL + Python  
✅ Mock Interviews  
✅ Communication Skills
"""

    # internship advice
    elif "internship" in question:

        response = """
### 💼 Internship Advice

1️⃣ Build 2–3 strong projects  
2️⃣ Improve LinkedIn profile  
3️⃣ Apply daily on Internshala, LinkedIn, Wellfound  
4️⃣ Practice interviews  
5️⃣ Build GitHub portfolio
"""

    # interview questions
    elif "interview" in question:

        response = """
### 🎤 Common ML Interview Questions

1. What is overfitting?  
2. Bias vs Variance?  
3. Explain TF-IDF  
4. Difference between CNN and ANN?  
5. What is Gradient Descent?  
6. Explain Precision vs Recall
"""

    # skills advice
    elif "skill" in question:

        response = """
### 🛠 Important Skills for AIML

✅ Python  
✅ SQL  
✅ Machine Learning  
✅ Deep Learning  
✅ NLP  
✅ Data Structures  
✅ Git/GitHub  
✅ Streamlit / Flask
"""

    # resume help
    elif "resume" in question:

        response = """
### 📄 Resume Tips

✅ Add measurable achievements  
✅ Mention tech stack in projects  
✅ Add GitHub & LinkedIn  
✅ Keep resume 1 page  
✅ Highlight internships & projects
"""

    # greeting
    elif any(word in question for word in [
        "hi", "hello", "hey"
    ]):

        greetings = [
            "Hey 👋 How can I help with your career?",
            "Hello! Ask me anything about placements or AIML 🚀",
            "Hi! Need project or placement advice?"
        ]

        response = random.choice(greetings)

    else:

        response = """
I can help with:

🚀 AIML Projects  
📄 Resume Advice  
🎯 Placement Preparation  
💼 Internship Guidance  
🧠 Machine Learning Roadmaps  
🎤 Interview Questions
"""

    # assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)