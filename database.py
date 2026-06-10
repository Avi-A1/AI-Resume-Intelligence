import sqlite3

DB_NAME = "database/users.db"


def create_tables():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resume_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        predicted_role TEXT,
        ats_score INTEGER,
        readiness INTEGER,
        skills TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_user(username, password):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )

        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()


def login_user(username, password):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user


def save_resume_analysis(
    username,
    predicted_role,
    ats_score,
    readiness,
    skills
):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO resume_history
    (
        username,
        predicted_role,
        ats_score,
        readiness,
        skills
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        username,
        predicted_role,
        ats_score,
        readiness,
        ",".join(skills)
    ))

    conn.commit()
    conn.close()


def get_resume_history(username):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT predicted_role,
           ats_score,
           readiness,
           skills
    FROM resume_history
    WHERE username=?
    """, (username,))

    data = cursor.fetchall()

    conn.close()

    return data