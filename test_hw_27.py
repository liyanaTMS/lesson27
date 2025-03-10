import sqlite3
import pytest

def test_work_sql():
    conn = sqlite3.connect("university.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER CHECK (age >= 0),
        country TEXT DEFAULT 'Unknown'
    );
    """)
    conn.commit()

    cursor.execute("""
    INSERT OR REPLACE INTO users (name, email, age, country) VALUES (?, ?, ?, ?)
    """,("Mike", "mike@example.com", 26, "England"))

    conn.commit()
    print("Успешно, возможно заменено")

    cursor.execute("SELECT email FROM users WHERE email = 'mike@example.com'")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.execute("DELETE FROM users WHERE email = 'mike@example.com'")
    conn.commit()

    cursor.execute("SELECT email FROM users WHERE email = 'mike@example.com'")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print('Успешно удалено')


    conn.close()
