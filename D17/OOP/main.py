#Learning on creating classes, costructor, initialize, methods

class User:
    # Function to Initialize attributes
    def __init__(self, user_id, username):
    # Self is the object being constructed    
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    #Creating a custom method
    def follow(self, user):
        user.followers += 1
        self.following += 1

    



user1 = User("user1", "izzul")
print(user1.username)
user2 = User("user2", "ain")
print(user2.username)

print(user1.followers)

for follower in range(0,10):
    user1.followers += 1

print(user1.followers)

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.following)
print(user2.followers)