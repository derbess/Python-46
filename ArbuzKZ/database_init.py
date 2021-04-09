from sqlite3 import *
from dbtable import User, Category, Product
def create_connection(path):
    connection = None
    try:
        connection = connect(path)
        print("success")
    except Error as e:
        print(e)
    return connection

connection = create_connection("arbuz")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

users = User(connection)
category = Category(connection)
product = Product(connection)