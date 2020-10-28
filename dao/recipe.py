import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def create_table():

    c = create_connection('yummy.db')

    c.execute()
    c.commit()
    c.close()

def add_recipe():
    pass

def delete_recipe():
    pass