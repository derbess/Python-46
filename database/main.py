from sqlite3 import *
from db import create_connection
from db_tables import *

connection = create_connection("test_database")

students = StudentTable(connection)
students.create_table()
students.insert_student(3,"Azamat",21,4,4)

# students.delete_student(2)
print(students.get_all_students())