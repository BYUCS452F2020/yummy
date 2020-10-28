class Ingredient:

    def __init__(self, recipeID, name, amount):

        self.recipeID = recipeID
        self.name = name
        self.amount = amount

        # Getters and getters are internally generated
        # Use the Pythonic way to access these properties
        # Setter: obj.attribute = value
        # Getter: value = obj.attribute
        # Deleter: del obj.attribute
