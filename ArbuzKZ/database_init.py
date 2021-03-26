from sqlite3 import *

def create_connection(path):
    connection = None
    try:
        connection = connect(path)
        print("success")
    except Error as e:
        print(e)
    return connection