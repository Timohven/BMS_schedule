import sqlite3
import csv, os
#import for students
"""
with open("students.csv", "r", encoding="utf-8", newline="") as csv_file:
    reader = csv.reader(csv_file)
    print(reader)
    headers = next(reader)
    data = list(reader)
    print(headers)
    print(data)
try:
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")
    for line in data:
        sqlite_insert_query = """INSERT INTO schedule_student
                          (surname, name, birthday, contact, messenger, source,
                          comments, agent_name, agent_type, agent_contact)
                          VALUES
                          (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        line[3] = "+" + line[3]
        if line[9]!="":
            line[9] = "+" + line[9]
        print("Строка :", line, " добавлена в БД")
        count = cursor.execute(sqlite_insert_query, line)
        sqlite_connection.commit()
    cursor.close()
"""
#import for teachers
with open("teachers.csv", "r", encoding="utf-8", newline="") as csv_file:
    reader = csv.reader(csv_file)
    print(reader)
    headers = next(reader)
    data = list(reader)
    print(headers)
    print(data)
try:
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")
    for line in data:
        sqlite_insert_query = """INSERT INTO schedule_teacher
                          (surname, name, birthday, contact, messenger, comments)
                          VALUES
                          (?, ?, ?, ?, ?, ?);"""
        line[3] = "+" + line[3]
        print("Строка :", line, " добавлена в БД")
        count = cursor.execute(sqlite_insert_query, line)
        sqlite_connection.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")