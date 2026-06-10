import streamlit as st

st.title("🚀 Career Roadmap Generator")

role = st.selectbox(
    "Choose Target Role",
    [
        "Machine Learning Engineer",
        "Data Scientist",
        "Data Analyst",
        "Web Developer"
    ]
)

st.subheader(f"Roadmap for {role}")

if role == "Machine Learning Engineer":
    st.write("1️⃣ Python")
    st.write("2️⃣ NumPy + Pandas")
    st.write("3️⃣ SQL")
    st.write("4️⃣ Machine Learning")
    st.write("5️⃣ Deep Learning")
    st.write("6️⃣ Deployment")
    st.write("7️⃣ Projects")

elif role == "Data Scientist":
    st.write("1️⃣ Python")
    st.write("2️⃣ Statistics")
    st.write("3️⃣ SQL")
    st.write("4️⃣ Machine Learning")
    st.write("5️⃣ Data Visualization")
    st.write("6️⃣ Projects")

elif role == "Data Analyst":
    st.write("1️⃣ Excel")
    st.write("2️⃣ SQL")
    st.write("3️⃣ Python")
    st.write("4️⃣ Power BI")
    st.write("5️⃣ Projects")

elif role == "Web Developer":
    st.write("1️⃣ HTML")
    st.write("2️⃣ CSS")
    st.write("3️⃣ JavaScript")
    st.write("4️⃣ React")
    st.write("5️⃣ Backend")
    st.write("6️⃣ Projects")