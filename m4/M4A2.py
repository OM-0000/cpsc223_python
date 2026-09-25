# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 4 Assignment 2

food_dict = {}
for itr in range(1,4):
    food_str = input("What is good to eat? ")
    country_str = input("What country is that from? ")
    food_dict[food_str] = country_str
choice_str = input("What dish do you like? ")
print(f"{choice_str.title()} is from {food_dict[choice_str].title()}")
