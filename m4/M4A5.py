# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 4 Assignment 5

food_dict = {'Jim': 'Tacos',
             'Bob': 'Burgers',
             'Janelle': '',
             'Lisa': 'Pizza',
             'Thomas': '',
             'Yolanda': '',
             'Finn': 'Bread',
             }

for name,food in food_dict.items():
    if food == '':
        food_dict[name] = input(f"What is {name}\'s favorite food? ")
print("Here are the favorite foods:")
for name,food in food_dict.items():
    print(f"{name}'s favorite food is {food}")
