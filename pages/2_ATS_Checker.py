import streamlit as st

st.title("📊 ATS Resume Checker")

st.write("Analyze resume quality for ATS systems.")

skills = st.multiselect(
    "Select Skills You Have",
    [
        "Python", "SQL", "Machine Learning",
        "TensorFlow", "Pandas",
        "GitHub", "Docker",
        "Data Analysis", "NLP"
    ]
)

projects = st.slider("Projects Completed", 0, 10, 2)

internships = st.slider("Internships", 0, 5, 0)

github = st.checkbox("GitHub Profile Added")
linkedin = st.checkbox("LinkedIn Added")

score = 0

score += len(skills) * 5
score += projects * 5
score += internships * 10

if github:
    score += 10

if linkedin:
    score += 10

score = min(score, 100)

st.subheader("📈 ATS Score")

st.progress(score)

st.write(f"### {score}/100")

st.subheader("💡 Suggestions")

if score < 50:
    st.warning("Resume needs improvement")
    st.write("• Add more projects")
    st.write("• Include GitHub profile")
    st.write("• Learn SQL")
    st.write("• Add internship experience")

elif score < 80:
    st.info("Good resume profile")
    st.write("• Improve project descriptions")
    st.write("• Add measurable achievements")

else:
    st.success("Excellent Resume 🚀")