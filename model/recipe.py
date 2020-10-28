class Recipe:

    def __init__(self, recipeID, authorID, name, duration, picture, difficulty, style, country, course):

        self.recipeID = recipeID
        self.authorID = authorID
        self.name = name
        self.duaration = duration
        self.picture = picture
        self.difficulty = difficulty
        self.style = style
        self.country = country
        self.course = course

        self.ingredient = []
        self.procedure = []

        # Getters and getters are internally generated
        # Use the Pythonic way to access these properties
        # Setter: obj.attribute = value
        # Getter: value = obj.attribute
        # Deleter: del obj.attribute
