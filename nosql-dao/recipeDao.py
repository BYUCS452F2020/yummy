import redis
from model.recipe import Recipe
import json


class RecipeDao:

    def __init__(self, host='localhost', port=6379, db=0):

        self.host = host
        self.port = port
        self.db = 0

    def add_recipe(self, recipe):

        if self.find_recipe_by_id(recipe.recipeID):
            # recipe already exists
            return -1

        try:
            r = redis.Redis(host=self.host, port=self.port, db=self.db)
            r.hset(f'recipe:{recipe.recipeID}', mapping = {
                'recipeID': recipe.recipeID,
                'authorID': recipe.recipeID,
                'name': recipe.name,
                'duration': recipe.duration,
                'picture': recipe.picture,
                'difficulty': recipe.difficulty,
                'style': recipe.style,
                'country': recipe.country,
                'course': recipe.course,
                'ingredient': json.dumps(recipe.ingredient),
                'procedure': json.dumps(recipe.procedure)
            })
        except Exception as e:
            print(e)
            raise e

    def find_recipe_by_id(self, id):

        try:
            r = redis.Redis(host=self.host, port=self.port, db=self.db)
            recipe = r.hgetall(f'recipe:{id}')
            return recipe
        except Exception as e:
            print(e)
            raise e

    def update_recipe(self, recipe):

        if not self.find_recipe_by_id(recipe.recipeID):
            # recipe does not create
            return -1

        try:
            r = redis.Redis(host=self.host, port=self.port, db=self.db)
            r.hset(f'recipe:{recipe.recipeID}', mapping={
                'recipeID': recipe.recipeID,
                'authorID': recipe.recipeID,
                'name': recipe.name,
                'duration': recipe.duration,
                'picture': recipe.picture,
                'difficulty': recipe.difficulty,
                'style': recipe.style,
                'country': recipe.country,
                'course': recipe.course,
                'ingredient': json.dumps(recipe.ingredient),
                'procedure': json.dumps(recipe.procedure)
            })
        except Exception as e:
            print(e)
            raise e

    def delete_recipe_by_id(self, id):

        if not self.find_recipe_by_id(id):
            # recipe does not create
            return -1

        try:
            r = redis.Redis(host=self.host, port=self.port, db=self.db)
            r.delete(f'recipe:{id}')
        except Exception as e:
            print(e)
            raise e


# Unit Test
recipe1 = Recipe(recipeID='135',
                 authorID='sarah',
                 name='Sweet Potato Soup',
                 duration='45 minutes',
                 picture='picture',
                 difficulty='easy',
                 style='boiling',
                 country='chinese',
                 course='dessert',
                 ingredient={
                     "ingredient": [{
                         "name": "sweet potato",
                         "amount": "400g"
                     }, {
                         "name": "slab sugar",
                         "amount": "1 block"
                     }, {
                         "name": "ginger",
                         "amount": "2 slices"
                     }]
                 },
                 procedure={
                     "procedure": [{
                         "procedure": 1,
                         "description": "Washed and peel sweet the potato"
                     }, {
                         "procedure": 2,
                         "description": "When you slice the sweet potatoes, cut it halfway then split the piece off (It brings out a better flavor)"
                     }, {
                         "procedure": 3,
                         "description": "Add ginger and sweet potatoes into boiled water. Turn the water to med heat. "
                     }, {
                         "procedure": 4,
                         "description": "Cook for 25 minutes until the sweet potatoes are softened. "
                     }, {
                         "procedure": 5,
                         "description": "Add slab sugar. "
                     }]
                 })
recipeDao = RecipeDao()
recipeDao.add_recipe(recipe1)

found_recipe = recipeDao.find_recipe_by_id('135')
print(found_recipe)
