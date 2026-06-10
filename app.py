import streamlit as st
from database import *

st.set_page_config(
    page_title="AI Career Platform",
    page_icon="🚀",
    layout="wide"
)

create_tables()

st.title("🚀 AI Career Intelligence Platform")

menu = [
    "Login",
    "Signup"
]

choice = st.sidebar.selectbox(
    "Menu",
    menu
)

# --------------------------
# SIGNUP
# --------------------------
if choice == "Signup":

    st.subheader("Create Account")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Signup"):

        success = add_user(
            username,
            password
        )

        if success:
            st.success(
                "Account Created!"
            )
        else:
            st.error(
                "Username already exists."
            )

# --------------------------
# LOGIN
# --------------------------
elif choice == "Login":

    st.subheader("Login")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        user = login_user(
            username,
            password
        )

        if user:

            st.session_state.logged_in = True
            st.session_state.username = username

            st.success(
                f"Welcome {username}"
            )

        else:

            st.error(
                "Invalid credentials"
            )

# --------------------------
# DASHBOARD
# --------------------------
if st.session_state.get(
    "logged_in"
):

    st.success(
        f"Logged in as {st.session_state.username}"
    )

    st.write(
        "Use sidebar pages for Resume Analysis, AI Assistant, etc."
    )

    history = get_resume_history(
        st.session_state.username
    )

    st.subheader(
        "📄 Resume Analysis History"
    )

    if history:

        for item in history:

            st.info(f"""
Role: {item[0]}

ATS Score: {item[1]}

Readiness: {item[2]}

Skills: {item[3]}
""")

    else:

        st.warning(
            "No history yet."
        )

    if st.button("Logout"):

        st.session_state.logged_in = False
        st.rerun()