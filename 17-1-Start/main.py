class User:

    # the arguments will be required when we initialise an object
    def __init__(self, user_id, username):
        # __init__ function is executed every time we create an object from the class
        print("new user being created...")

        # set the attributes equal to the arguments that will be passed when calling the class
        self.id = user_id
        self.username = username
        # set a default value for an attribute that will not be known during initialisation
        self.followers = 0
        self.following = 0

    # define a method for the users to follow one another
    def follow(self, user):
        print(f"user_{self.id} is now following user_{user.id}")
        user.followers += 1
        self.following += 1


# create instances / objects from the class and pass values for the attributes

user_1 = User("001", "housemaster")
user_2 = User("002", "pumpernickel")

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


# call methods as created in the class definition
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)