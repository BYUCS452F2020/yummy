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

    sql = """CREATE TABLE Recipe (
                RecipeID int NOT NULL UNIQUE AUTO_INCREMENT,
                AuthorID int,
                Name varchar(255) NOT NULL,
                Duration varchar(255),
                Picture BLOB,
                Difficulty int,
                Style varchar(255),
                Country varchar(255),
                Course varchar(255),
                PRIMARY KEY (RecipeID),
                FOREIGN KEY (AuthorID) REFERENCES User(UserID) ON DELETE SET NULL,
                CHECK (Difficulty BETWEEN 1 AND 5)
            );"""

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