import sqlite3
from sqlite3 import Error
from dao import flavoriteDao
from dao import ingredientDao
from dao import procedureDao
from dao import recipeDao
from dao import userDao


def create_all_tables():
    """ Create all tables of the Yummy database. It does not create any default model
    """

    flavoriteDao.create_table()
    procedureDao.create_table()
    recipeDao.create_table()
    ingredientDao.create_table()
    userDao.create_table()


def insert_mock_data():
    """ Insert the default mock model into the Yummy database """

    # add users
    user_1 = (0, 'test1', 'password', 'email@gmail.com')
    user_2 = (1, 'test2', 'password', 'email@gmail.com')
    user_3 = (2, 'test3', 'password', 'email@gmail.com')

    userDao.add_user(user_1)
    userDao.add_user(user_2)
    userDao.add_user(user_3)

    # add recipe
    recipe_1 = (0, 0, 'recipe1', '160', 'blob', 1, 'party', 'Korea', 'step1, step2')

    recipeDao.add_recipe(recipe_1)


def main():

    create_all_tables()

    insert_mock_data()

    ### edit model ###
    # edit user
    user_1_edit = ('newtest1', 'newemail@gmail.com', 0)

    userDao.update_user(user_1_edit)

    ### delete model ###
    # delete user
    userDao.delete_user(2)


if __name__ == '__main__':
    main()