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

def add_user(user):
    c = create_connection('yummy.db')

    print('add_user')

    sql = ''' INSERT INTO User(UserID,Username,Password,Email)
              VALUES(?,?,?,?) '''

    c.execute(sql, user)
    c.commit()
    c.close()

def update_user(user):
    c = create_connection('yummy.db')

    print('update_user')

    sql = ''' UPDATE User
                SET Username = ?,
                    Email = ?
                WHERE UserID = ?'''

    c.execute(sql, user)
    c.commit()
    c.close()

def delete_user(UserID):
    c = create_connection('yummy.db')

    print('delete_user')

    sql = ''' DELETE FROM User WHERE UserID = ? '''

    c.execute(sql, (UserID,))
    c.commit()
    c.close()