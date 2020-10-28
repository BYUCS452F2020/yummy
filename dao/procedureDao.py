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

    sql = """CREATE TABLE Procedure (
                RecipeID int NOT NULL,
                Procedure int NOT NULL,
                Description varchar(255),
                PRIMARY KEY (RecipeID, Procecure),
                FOREIGN KEY (RecipeID) REFERENCES Recipe(RecipeID) ON DELETE CASDADE
            );"""

    c.execute(sql)
    c.commit()
    c.close()