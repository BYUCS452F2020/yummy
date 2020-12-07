import redis


class FlavoriteDao:

    def __init__(self, host='localhost', port=6379, db=0):

        self.host = host
        self.port = port
        self.db = 0

    def add_flavorite(self, userId, recipeId):
        try:
            r = redis.Redis(host=self.host, port=self.port, db=self.db)
            r.rpush(f"flavorite:{userId}", recipeId)
        except Exception as e:
            print(e)
            raise e

    def find_flavorite_by_userId(self, userId):
        try:
            r = redis.Redis(host=self.host, port=self.port, db=self.db)
            flavorite = r.get(f"flavorite:{userId}")
            return flavorite
        except Exception as e:
            print(e)
            raise e

    def delete_flavorite(self, userId, recipeId):
        try:
            r = redis.Redis(host=self.host, port=self.port, db=self.db)
            r.lrem(f"flavorite:{userId}", 1, recipeId)
        except Exception as e:
            print(e)
            raise e


# Unit Test
flavoriteDao = FlavoriteDao()
flavoriteDao.add_flavorite('135', '135')

found_flavorite = flavoriteDao.find_flavorite_by_userId('135')
print(found_flavorite)

flavoriteDao.delete_flavorite('135', '135')

found_flavorite = flavoriteDao.find_flavorite_by_userId('135')
print(found_flavorite)

