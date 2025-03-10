import sqlite3
import pytest

def test_hw27_sqlite():
    # Подключаемся к базе данных (создаст файл, если его нет)
    conn = sqlite3.connect("university.db")
    cursor = conn.cursor()  # Создаем курсор - это специальный объект который делает запросы и получает их результаты

    # Создаем таблицу
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER CHECK (age >= 0),
        country TEXT DEFAULT 'Unknown'
    );
    """)
    # Фиксируем изменения
    conn.commit()

    # Добавляем юзера
    cursor.execute("INSERT INTO users (name, email, age, country) VALUES (?, ?, ?, ?)",
                   ("test_user", "test_user@gmail.com", 41, "Belarus"))

    # Фиксируем изменения
    conn.commit()

    # Проверяем результат добавления пользователя
    cursor.execute("SELECT * FROM users WHERE name = 'test_user'")
    rows = cursor.fetchall()
    for row in rows:
        print("Next user was added: ", row)
    if len(rows) != 0:
        print('Пользователь успешно добавлен')

    # Удаляем добавленного пользователя
    cursor.execute("DELETE FROM users WHERE name = 'test_user'")

    # Фиксируем изменения
    conn.commit()

    # Проверяем результат удаления пользователя
    cursor.execute("SELECT * FROM users WHERE name = 'test_user'")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print('Пользователь успешно удален')

    conn.close()
