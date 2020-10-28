import sqlite3
from sqlite3 import Error
from dao import user
from dao import recipe
from dao import ingredient

def main():
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

    ### create tables ###
    # create Recipe table
    recipe.create_table(sql_create_Recipe_table)

    # create Ingredient table
    ingredient.create_table(sql_create_Ingredient_table)

    # create User table
    user.create_table(sql_create_User_table)

    ### add data ###
    # add users
    user_1 = (0, 'test1', 'password', 'email@gmail.com')
    user_2 = (1, 'test2', 'password', 'email@gmail.com')
    user_3 = (2, 'test3', 'password', 'email@gmail.com')

    user.add_user(user_1)
    user.add_user(user_2)
    user.add_user(user_3)

    # add recipe
    recipe_1 = (0, 0, 'recipe1', '160', 'blob', 1, 'party', 'Korea', 'step1, step2')

    recipe.add_recipe(recipe_1)

    ### edit data ###
    # edit user
    user_1_edit = ('newtest1', 'newemail@gmail.com', 0)

    user.update_user(user_1_edit)

    ### delete data ###
    # delete user
    user.delete_user(2)


if __name__ == '__main__':
    main()