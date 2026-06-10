import streamlit as st

st.title("🎯 Interview Preparation")

role = st.selectbox(
    "Select Role",
    [
        "Machine Learning Engineer",
        "Data Analyst",
        "Web Developer"
    ]
)

questions = {
    "Machine Learning Engineer": [
        "What is overfitting?",
        "Difference between bagging and boosting?",
        "Explain TF-IDF",
        "What is gradient descent?"
    ],

    "Data Analyst": [
        "What is SQL JOIN?",
        "Difference between WHERE and HAVING?",
        "Explain normalization",
        "What is Power BI?"
    ],

    "Web Developer": [
        "Difference between HTML and CSS?",
        "What is React?",
        "Explain API",
        "Difference between frontend and backend?"
    ]
}

st.subheader("Interview Questions")

for q in questions[role]:
    st.write(f"✅ {q}")