import sqlite3
from datetime import timedelta, datetime
from random import randint
import faker


STUDENTS = 30
TEACHERS = 3
GRADES = 20
SUBJECTS = ['Вища математика', 'Алгоритми', 'Візуальне програмування', 'Комп\'ютерна логіка', 'Філософія']
GROUPS = ['1КІ-21б', '2КІ-21б', '1СП-21б']


def create_db():
    with open('hw8web.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('hw8web.db') as conn:
        cur = conn.cursor()
        cur.executescript(sql)


def date_range(start, end):
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result


def fill_data():
    fake_data = faker.Faker('uk-UA')
    connection = sqlite3.connect('hw8web.db')
    cursor = connection.cursor()

    def seed_teachers():
        teachers = []
        for _ in range(TEACHERS):
            teachers.append(fake_data.name())
        sql_teachers = 'INSERT INTO teachers(fullname) VALUES (?)'
        cursor.executemany(sql_teachers, zip(teachers, ))

    def seed_subjects():
        sql_disc = 'INSERT INTO subjects(name, teachers_id) VALUES (?, ?)'
        cursor.executemany(sql_disc, zip(SUBJECTS, iter(randint(1, TEACHERS) for _ in range(len(SUBJECTS)))))

    def seed_groups():
        sql_groups = 'INSERT INTO groups(name) VALUES (?)'
        cursor.executemany(sql_groups, zip(GROUPS,))

    def seed_students():
        students = []  # создаем пустой список студентов
        # заполняем его случайными именами из объекта fake
        for _ in range(STUDENTS):
            students.append(fake_data.name())
        sql_students = 'INSERT INTO students(fullname, group_id) VALUES (?,?)'
        cursor.executemany(sql_students, zip(students, iter(randint(1, len(GROUPS)) for _ in range(len(students)))))

    def seed_grades():
        start_date = datetime.strptime("2022-09-19", "%Y-%m-%d")
        end_date = datetime.strptime("2023-06-30", "%Y-%m-%d")
        d_range = date_range(start=start_date, end=end_date)

        grades = []

        for d in d_range:
            r_disc = randint(1, len(SUBJECTS))
            r_students = [randint(1, STUDENTS) for _ in range(3)]
            for student in r_students:
                grades.append((student, r_disc, d.date(), randint(1, 12)))
        sql_ratings = 'INSERT INTO grades(students_id, subjects_id, date_of, grade) VALUES (?, ?, ?, ?)'
        cursor.executemany(sql_ratings, grades)

    try:
        seed_teachers()
        seed_subjects()
        seed_groups()
        seed_students()
        seed_grades()
        connection.commit()

    except sqlite3.IntegrityError as err:
        print(err)

    finally:
        connection.close()


if __name__ == "__main__":
    create_db()
    fill_data()