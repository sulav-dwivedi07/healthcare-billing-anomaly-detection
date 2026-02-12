import sqlite3
from src.config import DB_PATH


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        hospital TEXT,
        treatment TEXT,
        amount REAL,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()
