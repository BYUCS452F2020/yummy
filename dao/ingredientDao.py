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

    sql = """CREATE TABLE Ingredient (
                RecipeID int NOT NULL,
                Name varchar(255) NOT NULL,
                Amount varchar(255),
                PRIMARY KEY (RecipeID, Name),
                FOREIGN KEY (RecipeID) REFERENCES Recipe(RecipeID) ON DELETE CASDADE	
            );"""

    c.execute(sql)
    c.commit()
    c.close()


def add_ingredient(ingredient):
    c = create_connection('yummy.db')

    print('add_ingredient')

    sql = ''' INSERT INTO Ingredient(RecipeID,Name,Amount)
              VALUES(?,?,?) '''

    c.execute(sql, ingredient)
    c.commit()
    c.close()