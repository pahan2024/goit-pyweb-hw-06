import sqlite3
import random
from datetime import datetime, timedelta
from faker import Faker

# Ініціалізуємо Faker 
fake = Faker('uk_UA')

# Підключаємося до бази даних (якщо файлу немає, SQLite створить його автоматично)
conn = sqlite3.connect('pyweb-hw-06.sqlite')
cur = conn.cursor()

try:
    # --- КРОК 0: СТВОРЕННЯ СТРУКТУРИ ТАБЛИЦЬ (DDL) ---
    print("Створення таблиць та зв'язків між ними...")
    
    # Тимчасово вмикаємо підтримку Foreign Keys в SQLite
    cur.execute("PRAGMA foreign_keys = ON;")
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        group_id INT REFERENCES groups(id) ON DELETE SET NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        teacher_id INT REFERENCES teachers(id) ON DELETE CASCADE
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INT REFERENCES students(id) ON DELETE CASCADE,
        subject_id INT REFERENCES subjects(id) ON DELETE CASCADE,
        grade INT NOT NULL,
        date_received DATE NOT NULL
    );
    """)

    # --- КРОК 1: ЗАПОВНЕННЯ ТАБЛИЦЬ ДАНИМИ (DML) ---
    print("Наповнення бази даних випадковими даними...")
    
    # 1. Заповнюємо групи
    groups = ['Група А', 'Група Б', 'Група В']
    for group_name in groups:
        cur.execute("INSERT INTO groups (name) VALUES (?);", (group_name,))
    
    # 2. Заповнюємо викладачів
    for _ in range(4):
        cur.execute("INSERT INTO teachers (name) VALUES (?);", (fake.name(),))
        
    # 3. Заповнюємо предмети
    subjects = ['Математика', 'Фізика', 'Історія', 'Програмування', 'Хімія', 'Біологія']
    for subject_name in subjects:
        teacher_id = random.randint(1, 4)
        cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?);", (subject_name, teacher_id))
        
    # 4. Заповнюємо студентів
    for _ in range(40):
        group_id = random.randint(1, 3)
        cur.execute("INSERT INTO students (name, group_id) VALUES (?, ?);", (fake.name(), group_id))
        
    # 5. Заповнюємо оцінки
    start_date = datetime.now() - timedelta(days=90)
    
    for student_id in range(1, 41):
        num_of_grades = random.randint(15, 20)
        for _ in range(num_of_grades):
            subject_id = random.randint(1, 6)
            grade = random.randint(4, 12)
            
            random_days = random.randint(0, 90)
            date_received = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
            
            cur.execute(
                "INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?);",
                (student_id, subject_id, grade, date_received)
            )
            
    conn.commit()
    print("Базу даних успішно створено та заповнено з нуля!")

except sqlite3.Error as error:
    print(f"Помилка при роботі з SQLite: {error}")
    conn.rollback()

finally:
    cur.close()
    conn.close()
