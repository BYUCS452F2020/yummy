class User:

    def __init__(self, userID, username, password, email):

        self.userID = userID
        self.username = username
        self.password = password
        self.email = email

        self.flavorite = []

        # Getters and getters are internally generated
        # Use the Pythonic way to access these properties
        # Setter: obj.attribute = value
        # Getter: value = obj.attribute
        # Deleter: del obj.attribute
