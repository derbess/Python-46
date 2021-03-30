from database_init import create_connection
from dbtable import *
from SignUpTk import signUp, logIn

connection = create_connection("arbuz")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

users = User(connection)
category = Category(connection)
product = Product(connection)

# signUp(users)
print(users.get_all_user())
logIn(users)
