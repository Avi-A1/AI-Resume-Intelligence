import streamlit as st
import pandas as pd
from pypdf import PdfReader
import plotly.express as px
import joblib

from database import save_resume_analysis
from pdf_generator import create_resume_report

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="Resume Analysis",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Intelligence Dashboard")
st.write("Upload your resume for intelligent analysis.")

# ------------------------------------------------
# LOGIN CHECK
# ------------------------------------------------
if not st.session_state.get("logged_in"):

    st.warning(
        "Please login first from Home page."
    )

    st.stop()

# ------------------------------------------------
# LOAD MODEL
# ------------------------------------------------
@st.cache_resource
def load_model():

    model = joblib.load(
        "models/model.pkl"
    )

    tfidf = joblib.load(
        "models/tfidf.pkl"
    )

    return model, tfidf


# ------------------------------------------------
# PDF TEXT EXTRACTION
# ------------------------------------------------
def extract_resume_text(pdf_file):

    text = ""

    try:

        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    except Exception as e:

        st.error(
            f"Error reading PDF: {e}"
        )

    return text


# ------------------------------------------------
# SKILLS DATABASE
# ------------------------------------------------
skills_db = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy",
    "nlp",
    "opencv",
    "flask",
    "django",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "mongodb",
    "git",
    "github",
    "docker",
    "streamlit",
    "power bi",
    "excel",
    "data analysis",
    "aws",
    "linux",
    "java",
    "spring"
]


# ------------------------------------------------
# EXTRACT SKILLS
# ------------------------------------------------
def extract_skills(text):

    found = set()

    text = text.lower()

    for skill in skills_db:

        if skill in text:
            found.add(skill)

    return list(found)


# ------------------------------------------------
# ROLE BASED SKILLS
# ------------------------------------------------
role_skills = {

    "Data Science": [
        "python",
        "sql",
        "machine learning",
        "pandas",
        "numpy",
        "tensorflow",
        "github"
    ],

    "Python Developer": [
        "python",
        "django",
        "flask",
        "git",
        "github"
    ],

    "Web Designing": [
        "html",
        "css",
        "javascript",
        "react",
        "git"
    ],

    "Java Developer": [
        "java",
        "sql",
        "spring",
        "git"
    ],

    "DevOps Engineer": [
        "docker",
        "github",
        "linux",
        "aws"
    ]
}


# ------------------------------------------------
# FILE UPLOAD
# ------------------------------------------------
uploaded_file = st.file_uploader(
    "📂 Upload Resume PDF",
    type=["pdf"]
)

# ------------------------------------------------
# ANALYSIS
# ------------------------------------------------
if uploaded_file:

    with st.spinner(
        "🔍 Analyzing Resume..."
    ):

        text = extract_resume_text(
            uploaded_file
        )

        model, tfidf = load_model()

        transformed = tfidf.transform(
            [text]
        )

        prediction = model.predict(
            transformed
        )[0]

        confidence = round(
            max(
                model.predict_proba(
                    transformed
                )[0]
            ) * 100,
            2
        )

        skills = extract_skills(
            text
        )

        # --------------------------------
        # ATS SCORE
        # --------------------------------
        score = 0

        if len(skills) >= 7:
            score += 35

        elif len(skills) >= 4:
            score += 20

        if "github" in text.lower():
            score += 15

        if "linkedin" in text.lower():
            score += 10

        if "project" in text.lower():
            score += 20

        if "internship" in text.lower():
            score += 20

        score = min(score, 100)

        # --------------------------------
        # CAREER READINESS
        # --------------------------------
        readiness = min(
            score + len(skills) * 3,
            100
        )

        # --------------------------------
        # SAVE HISTORY
        # --------------------------------
        save_resume_analysis(
            st.session_state.username,
            prediction,
            score,
            readiness,
            skills
        )

    # ------------------------------------------------
    # METRICS
    # ------------------------------------------------
    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🎯 Predicted Role",
            prediction
        )

    with col2:
        st.metric(
            "📊 ATS Score",
            f"{score}%"
        )

    with col3:
        st.metric(
            "🛠 Skills Found",
            len(skills)
        )

    with col4:
        st.metric(
            "🧠 Confidence",
            f"{confidence}%"
        )

    st.markdown("---")

    # ------------------------------------------------
    # DETECTED SKILLS
    # ------------------------------------------------
    st.subheader(
        "🛠 Skills Detected"
    )

    if skills:

        cols = st.columns(4)

        for i, skill in enumerate(
            skills
        ):

            cols[i % 4].success(
                skill.upper()
            )

    else:

        st.warning(
            "No major skills detected."
        )

    # ------------------------------------------------
    # SKILL GAP ANALYSIS
    # ------------------------------------------------
    st.subheader(
        "❌ Skill Gap Analysis"
    )

    recommended = role_skills.get(
        prediction,
        []
    )

    missing = []

    for skill in recommended:

        if skill not in skills:
            missing.append(skill)

    if missing:

        cols = st.columns(3)

        for i, skill in enumerate(
            missing
        ):

            cols[i % 3].warning(
                f"Missing: {skill.upper()}"
            )

    else:

        st.success(
            "No major skill gaps found 🚀"
        )

    # ------------------------------------------------
    # PROFILE CHECK
    # ------------------------------------------------
    st.subheader(
        "🔗 Professional Profiles"
    )

    col1, col2 = st.columns(2)

    with col1:

        if "github" in text.lower():

            st.success(
                "✅ GitHub Profile Found"
            )

        else:

            st.warning(
                "⚠ Add GitHub Profile"
            )

    with col2:

        if "linkedin" in text.lower():

            st.success(
                "✅ LinkedIn Profile Found"
            )

        else:

            st.warning(
                "⚠ Add LinkedIn Profile"
            )

    # ------------------------------------------------
    # ANALYTICS
    # ------------------------------------------------
    st.markdown("---")

    st.subheader(
        "📈 Resume Analytics"
    )

    col1, col2 = st.columns(2)

    with col1:

        fig = px.pie(
            values=[
                score,
                100 - score
            ],
            names=[
                "Strength",
                "Improvement"
            ],
            title="ATS Score Breakdown"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        if skills:

            skill_df = pd.DataFrame({
                "Skill": skills,
                "Count": [1] * len(skills)
            })

            fig2 = px.bar(
                skill_df,
                x="Skill",
                y="Count",
                title="Detected Skills"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

    # ------------------------------------------------
    # CAREER READINESS
    # ------------------------------------------------
    st.subheader(
        "🚀 Career Readiness"
    )

    st.progress(
        readiness
    )

    st.write(
        f"### {readiness}% Ready for Industry"
    )

    # ------------------------------------------------
    # FEEDBACK
    # ------------------------------------------------
    st.subheader(
        "💡 Resume Feedback"
    )

    feedback = []

    if score < 50:

        st.error(
            "Resume needs improvement"
        )

        feedback = [
            "Add technical projects",
            "Add GitHub profile",
            "Add LinkedIn profile",
            "Add internships",
            "Add measurable achievements"
        ]

    elif score < 80:

        st.info(
            "Good profile, but can improve"
        )

        feedback = [
            "Improve project descriptions",
            "Add certifications",
            "Add deployment experience"
        ]

    else:

        st.success(
            "Excellent Resume 🚀"
        )

        feedback = [
            "Strong profile",
            "Keep improving projects"
        ]

    for item in feedback:
        st.write(f"• {item}")

    # ------------------------------------------------
    # DOWNLOAD REPORT
    # ------------------------------------------------
    st.markdown("---")

    st.subheader(
        "📄 Download AI Report"
    )

    pdf_file = create_resume_report(
        st.session_state.username,
        prediction,
        score,
        confidence,
        skills,
        missing,
        readiness,
        feedback
    )

    with open(
        pdf_file,
        "rb"
    ) as file:

        st.download_button(
            label="📥 Download Resume Report",
            data=file,
            file_name=pdf_file,
            mime="application/pdf"
        )

    # ------------------------------------------------
    # RESUME PREVIEW
    # ------------------------------------------------
    with st.expander(
        "📄 Resume Preview"
    ):

        st.write(
            text[:2500]
        )