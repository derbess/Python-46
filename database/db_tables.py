from sqlite3 import *

class StudentTable():
    def __init__(self, connection):
        self.connection = connection

    def get_all_students(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()
        return data

    def insert_student(self, id, name, age, gpa, year):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO students VALUES({id},'{name}', {age}, {gpa}, {year})")
        self.connection.commit()
        print("values inserted")

    def delete_student(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM students WHERE id = {id}")

    def create_table(self):
        CREATE_TABLE = """
        CREATE TABLE students(
            id primary key,
            name varchar(40),
            age int,
            gpa int,
            year_of_study int
        )
        """
        cursor = self.connection.cursor()
        cursor.execute(CREATE_TABLE)