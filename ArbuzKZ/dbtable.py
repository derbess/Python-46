class User():
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        CREATE_TABLE = """
        CREATE TABLE user(
            id PRIMARY KEY,
            username varchar(40) unique,
            firstname varchar(40),
            lastname varchar(40),
            email varchar(40) unique,
            mobile varchar(12) unique,
            password varchar(20),
            balance int,
            address varchar(40),
            isAdmin boolean
        )
        """
        cursor = self.connection.cursor()
        cursor.execute(CREATE_TABLE)
        print("Table user created")

    def insert_user(self, id, username, firstname, lastname, email, mobile, password, balance, address, isAdmin):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO user VALUES({id}, '{username}', '{firstname}', '{lastname}', '{email}', '{mobile}', '{password}', {balance}, '{address}', {isAdmin})")
        self.connection.commit()
        print("data inserted")

    def get_all_user(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM user")
        data = cursor.fetchall()
        return data

    def delete_user(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM user WHERE id == {id}")
        print(f"User with id {id} deleted!")

    def login(self, email, password):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM user WHERE email = '{email}' and password = '{password}'")
        data = cursor.fetchall()
        return data


class Category():
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        CREATE_TABLE  ="""
        create table category(
          id PRIMARY KEY,
          name varchar(40)
          )
        """
        cursor = self.connection.cursor()
        cursor.execute(CREATE_TABLE)
        print("Category table created")

    def add_category(self, id, name):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO category VALUES({id}, '{name}')")
        self.connection.commit()
        print("Values inserted")

    def get_all_categories(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM category")
        data = cursor.fetchall()
        return data

    def delete_category(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM product WHERE id == {id}")
        print("Deleted")


class Product():
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        CREATE_TABLE = """
        Create table product(
            id PRIMARY KEY,
            name varchar(40),
            price int,
            cnt int,
            category_id int,
            FOREIGN KEY (category_id) REFERENCES category(id)
          )   
        """
        cursor = self.connection.cursor()
        cursor.execute(CREATE_TABLE)
        print("TABLE product created!")

    def add_product(self, id, name, price, cnt, cid):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO product VALUES({id}, '{name}', {price}, {cnt}, {cid})")
        self.connection.commit()
        print("values inserted!")

    def get_all_products(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM product")
        data = cursor.fetchall()
        return data
