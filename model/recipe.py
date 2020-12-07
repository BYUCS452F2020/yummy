class Recipe:

    def __init__(self, recipeID, authorID, name, duration, picture, difficulty, style, country, course, ingredient, procedure):

        self.recipeID = recipeID
        self.authorID = authorID
        self.name = name
        self.duration = duration
        self.picture = picture
        self.difficulty = difficulty
        self.style = style
        self.country = country
        self.course = course

        # For noSQL, the ingredient is stored as JSON in Redis
        # Ingredient = {
        #   "ingredient": [{
        #       "name": str,
        #       "amount": str
        #       },
        #       ...
        #   ]
        # }
        self.ingredient = ingredient

        # For noSQL, the procedure is stored as JSON in Redis
        # Procedure = {
        #   "procedure": [{
        #       "procedure": int,
        #       "description": str
        #       },
        #       ...
        #   ]
        # }
        self.procedure = procedure

        # Getters and getters are internally generated
        # Use the Pythonic way to access these properties
        # Setter: obj.attribute = value
        # Getter: value = obj.attribute
        # Deleter: del obj.attribute
