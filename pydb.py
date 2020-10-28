import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"C:\Users\tmdtm\Desktop\pythonsqlite.db"

    sql_create_Recipe_table = """CREATE TABLE IF NOT EXISTS Recipe (
                                    RecipeID int NOT NULL,
                                    AuthorID int NOT NULL,
                                    Name varchar(255) NOT NULL,
                                    Duration varchar(255),
                                    Picture BLOB,
                                    Difficulty int,
                                    Style varchar(255),
                                    Country varchar(255),
                                    Course varchar(255),
                                    PRIMARY KEY (RecipeID),
                                    FOREIGN KEY (AuthorID) REFERENCES User(UserID),
                                    CHECK (Difficulty BETWEEN 1 AND 5)
                                );"""

    sql_create_Ingredient_table = """CREATE TABLE IF NOT EXISTS Ingredient (
                                        RecipeID int NOT NULL,
                                        Name varchar(255) NOT NULL,
                                        Amount varchar(255),
                                        PRIMARY KEY (RecipeID, Name),
                                        FOREIGN KEY (RecipeID) REFERENCES Recipe(RecipeID)	
                                    );"""

    sql_create_User_table = """CREATE TABLE IF NOT EXISTS User (
                                UserID int NOT NULL,
                                Username varchar(255) NOT NULL,
                                Password varchar(255) NOT NULL,
                                Email varchar(255),
                                PRIMARY KEY (UserID)
                            );"""

    user_1 = (0, 'test1', 'password', 'email@gmail.com')


    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create Recipe table
        create_table(conn, sql_create_Recipe_table)

        # create Ingredient table
        create_table(conn, sql_create_Ingredient_table)

        # create User table
        create_table(conn, sql_create_User_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()