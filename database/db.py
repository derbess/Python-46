from sqlite3 import *

def create_connection(path):
    connection = None
    try:
        connection = connect(path)
        print("success")
    except Error as e:
        print(e)
    return connection


CREATE_TABLE = """
CREATE TABLE students(
    id primary key,
    name varchar(40),
    age int,
    gpa int,
    year_of_study int
)
"""

INSERT_VALUES = """
INSERT INTO students VALUES(1,"Derbes", 21, 3, 4)
"""
SELECT_ALL = "SELECT * from students"

