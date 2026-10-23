# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 7 Assignment 1

class User:
    def __init__(self, first_name, last_name, user_id, last_login, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.last_login = last_login
        self.password = password

    def describe_user(self):
        print(f"Accessing user {self.user_id}:")
        print(f"{self.first_name} {self.last_name} last logged in on {self.last_login}")

    def greet_user(self):
        print(f"Welcome to the jungle {self.first_name} {self.last_name}, you gonna die")

# hard-coded calls
jim = User(first_name='Jim', 
           last_name='Bob', 
           user_id=1000, 
           last_login='June 12, 1998', 
           password='password123')
jim.describe_user()
jim.greet_user()
joe = User('Joe', 
           'Bob',
           1001,
           'July 4, 2001',
           'babygirl')
joe.greet_user()
joe.describe_user()