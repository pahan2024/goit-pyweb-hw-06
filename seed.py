import sqlite3
import random
from datetime import datetime, timedelta
from faker import Faker

# Ініціалізуємо Faker
fake = Faker('uk_UA')

# Підключаємося до вашої бази даних SQLite
conn = sqlite3.connect('pyweb-hw-06.sqlite')
cur = conn.cursor()

try:
    # 1. Заповнюємо групи
    groups = ['Група А', 'Група Б', 'Група В']
    for group_name in groups:
        cur.execute("INSERT INTO groups (name) VALUES (?);", (group_name,))
    
    # 2. Заповнюємо викладачів (від 3 до 5)
    for _ in range(4):
        cur.execute("INSERT INTO teachers (name) VALUES (?);", (fake.name(),))
        
    # 3. Заповнюємо предмети (від 5 до 8 за умовою)
    # Кожен предмет прив'язуємо до випадкового викладача (ID від 1 до 4)
    subjects = ['Математика', 'Фізика', 'Історія', 'Програмування', 'Хімія', 'Біологія']
    for subject_name in subjects:
        teacher_id = random.randint(1, 4)
        cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?);", (subject_name, teacher_id))
        
    # 4. Заповнюємо студентів (від 30 до 50 за умовою)
    # Кожного студента розподіляємо у випадкову групу (ID від 1 до 3)
    for _ in range(40):
        group_id = random.randint(1, 3)
        cur.execute("INSERT INTO students (name, group_id) VALUES (?, ?);", (fake.name(), group_id))
        
    # 5. Заповнюємо оцінки (до 20 оцінок у КОЖНОГО студента)
    # Генеруємо дати за останні 3 місяці (90 днів)
    start_date = datetime.now() - timedelta(days=90)
    
    for student_id in range(1, 41):  # Для кожного з 40 студентів
        num_of_grades = random.randint(15, 20)  # Кількість оцінок (до 20)
        for _ in range(num_of_grades):
            subject_id = random.randint(1, 6)   # Випадковий предмет
            grade = random.randint(4, 12)       # Оцінка (від 4 до 12)
            
            # Випадкова дата отримання оцінки
            random_days = random.randint(0, 90)
            date_received = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
            
            cur.execute(
                "INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?);",
                (student_id, subject_id, grade, date_received)
            )
            
    # Зберігаємо зміни в базі даних
    conn.commit()
    print("Базу даних успішно заповнено випадковими даними!")

except sqlite3.Error as error:
    print(f"Помилка при роботі з SQLite: {error}")
    conn.rollback()

finally:
    cur.close()
    conn.close()
