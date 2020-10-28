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

def create_table(sql):

    c = create_connection('yummy.db')

    c.execute(sql)
    c.commit()
    c.close()

def add_recipe(recipe):
    c = create_connection('yummy.db')

    print('add_recipe')

    sql = ''' INSERT INTO Recipe(RecipeID,AuthorID,Name,Duration,Picture,Difficulty,Style,Country,Course)
              VALUES(?,?,?,?,?,?,?,?,?) '''

    c.execute(sql, recipe)
    c.commit()
    c.close()

def delete_recipe():
    pass