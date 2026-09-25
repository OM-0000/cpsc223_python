# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 4 Extra Credit 1

#Perhaps I missed a memo about default values for the city lists because of absence.
#I will use placeholder values.

#Define the empty list
cities_list = []
#Init the dictionaries and append to the list
#Toronto:
cities_list.append({
    'name': 'Toronto',
    'pop': 3350000,
    'state': 'Ontario',
    'teams': ['Maple Leafs', 'Raptors', 'Bluejays', 'FC', 'Argonauts'],
})
#Los Angeles:
cities_list.append({
    'name': 'Los Angeles',
    'pop': 3860000,
    'state': 'California',
    'teams': ['Lakers', 'Dodgers', 'Rams', 'Kings', 'Galaxy'],
})
#And I'll choose for the third: Cairo:
cities_list.append({
    'name': 'Cairo',
    'pop': 9600000,
    'state': 'Cairo Governorate',
    'teams': ['Al Ahly', 'Zamalek', 'Pyramids', 'Al Gezira', 'Heliopolis'],
})

choice_str = input("What is your favorite team? ")
city_str = ''
for idx1, dict in enumerate(cities_list):
    for idx2, team in enumerate(dict['teams']):
        if team.lower() == choice_str.lower():
            city_str = dict['name']
            break
#Print result
print(f"If you like {choice_str.title()} you should move to {city_str}")