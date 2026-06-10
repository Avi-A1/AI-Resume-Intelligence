import sqlite3
import os

# -----------------------------------
# DATABASE SETUP
# -----------------------------------
DB_FOLDER = "database"

# Create database folder if missing
if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)

DB_NAME = os.path.join(
    DB_FOLDER,
    "users.db"
)


# -----------------------------------
# CONNECTION
# -----------------------------------
def get_connection():

    conn = sqlite3.connect(
        DB_NAME,
        check_same_thread=False
    )

    return conn


# -----------------------------------
# CREATE TABLES
# -----------------------------------
def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    # -------------------------------
    # USERS TABLE
    # -------------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE,

            password TEXT
        )
    """)

    # -------------------------------
    # RESUME ANALYSIS TABLE
    # -------------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resume_analysis (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT,

            role TEXT,

            ats_score INTEGER,

            readiness INTEGER,

            skills TEXT
        )
    """)

    conn.commit()
    conn.close()


# -----------------------------------
# USER AUTH
# -----------------------------------
def register_user(
    username,
    password
):

    try:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users (
                username,
                password
            )
            VALUES (?, ?)
            """,
            (
                username,
                password
            )
        )

        conn.commit()
        conn.close()

        return True

    except sqlite3.IntegrityError:

        return False


def login_user(
    username,
    password
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE username=?
        AND password=?
        """,
        (
            username,
            password
        )
    )

    user = cursor.fetchone()

    conn.close()

    return user


# -----------------------------------
# SAVE RESUME ANALYSIS
# -----------------------------------
def save_resume_analysis(
    username,
    role,
    ats_score,
    readiness,
    skills
):

    conn = get_connection()

    cursor = conn.cursor()

    skills_string = ", ".join(
        skills
    )

    cursor.execute(
        """
        INSERT INTO resume_analysis (

            username,
            role,
            ats_score,
            readiness,
            skills

        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            username,
            role,
            ats_score,
            readiness,
            skills_string
        )
    )

    conn.commit()
    conn.close()


# -----------------------------------
# GET USER HISTORY
# -----------------------------------
def get_resume_history(
    username
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role,
               ats_score,
               readiness,
               skills
        FROM resume_analysis
        WHERE username=?
        """,
        (username,)
    )

    data = cursor.fetchall()

    conn.close()

    return data