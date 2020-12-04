import redis
from model.user import User


class UserDao:

    def __init__(self, host='localhost', port=6379, db=0):

        self.host = host
        self.port = port
        self.db = 0

    def add_user(self, user):

        if self.find_user_by_id(user.userID):
            # User already exists
            return -1

        try:
            r = redis.Redis(host=self.host, port=self.port, db=self.db)
            r.hset(f'user:{user.userID}', mapping = {
                'userID': user.userID,
                'username': user.username,
                'password': user.password,
                'email': user.email
            })
        except Exception as e:
            print(e)
            raise e

    def find_user_by_id(self, id):

        try:
            r = redis.Redis(host=self.host, port=self.port, db=self.db)
            user = r.hgetall(f'user:{id}')
            return user
        except Exception as e:
            print(e)
            raise e

    def update_user(self, user):

        if not self.find_user_by_id(user.userID):
            # User does not create
            return -1

        try:
            r = redis.Redis(host=self.host, port=self.port, db=self.db)
            r.hset(f'user:{user.userID}', mapping = {
                'userID': user.userID,
                'username': user.username,
                'password': user.password,
                'email': user.email
            })
        except Exception as e:
            print(e)
            raise e

    def delete_user_by_id(self, id):

        if not self.find_user_by_id(id):
            # User does not create
            return -1

        try:
            r = redis.Redis(host=self.host, port=self.port, db=self.db)
            r.delete(f'user:{id}')
        except Exception as e:
            print(e)
            raise e


# Unit Test
user1 = User('135', 'sarah', 'pw', 'email')
user2 = User('134', 'gordon', 'pw', 'gordon@gmail.com')
user3 = User('136', 'heeseung', 'pw', 'hee@gmail.com')
userDao = UserDao()
userDao.add_user(user1)
userDao.add_user(user2)
userDao.add_user(user3)

user3.password = 'nopw'
user3.email = 'heeseung@gmail.com'
userDao.update_user(user3)

found_user = userDao.find_user_by_id('134')
print(found_user)

userDao.delete_user_by_id('134')
