import sqlite3
import csv, os
from datetime import datetime, timedelta

def clone_week(cur_mon, cur_sun):
    try:
        sqlite_connection = sqlite3.connect('db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        #sqlite_insert_query = """INSERT * INTO schedule_schedule SELECT * FROM schedule_schedule WHERE time BETWEEN cur_mon AND cur_sun """
        sqlite_select_query = """SELECT * FROM schedule_schedule WHERE time BETWEEN ? AND ? """
        cursor.execute(sqlite_select_query, (cur_mon,cur_sun,))
        records = cursor.fetchall()
        for record in records:
            #print(type(record[1]))
            new_time = datetime.strptime(record[1], "%Y-%m-%d %H:%M:%S") + timedelta(days=7)
            record = list(record)
            record.pop(0)
            record[0] = new_time.strftime("%Y-%m-%d %H:%M:%S")
            record[3] = 1 #set the status "ожидается"
            print(record)
            sqlite_insert_query = """INSERT INTO schedule_schedule (time, duration, type, state, contract_id, office_id) VALUES (?, ?, ?, ?, ?, ?); """
            cursor.execute(sqlite_insert_query, record)
            sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

#import for students
def load_students():
    with open("Students.csv", "r", encoding="utf-8", newline="") as csv_file:
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
            if line[9] != "":
                line[9] = "+" + line[9]
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

#import for teachers
def load_teachers():
    with open("Teachers.csv", "r", encoding="utf-8", newline="") as csv_file:
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