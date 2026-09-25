# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 4 Extra Credit 2

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

#Let's do it the hard way, I guess.
#We'll use a tally dictionary whose keys are food items and values are the tally (represented as an integer)
tally_dict = {}
for name, food in food_dict.items():
    if food in tally_dict:
        tally_dict[food] += 1
    else:
        tally_dict[food] = 1

#Now we'll use a simple algorithm to find the max
#Maybe we could use a tuple, but I'll just use two variables
popular_food_str = ''
max_int = 0
for food, tally in tally_dict.items():
    if tally > max_int:
        popular_food_str = food
        max_int = tally
#Now, let's print the result:
print(f"The most popular food is {popular_food_str}")