from database_init import create_connection
from dbtable import *
from SignUpTk import signUp, logIn
from OtherTk import productsTk,profileTk

connection = create_connection("arbuz")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

users = User(connection)
category = Category(connection)
product = Product(connection)


# signUp(users)
# print(product.get_all_products())
user = (1, 'decode', 'Derbes', 'Utebaliyev', 'decode@gmail.com', '87777777778', 'adminadmin', 10000, 'Abai 52', 0)
profileTk(user)
# productsTk(product)
