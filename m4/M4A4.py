# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 4 Assignment 4

guy_dict1 = {
    'name': 'Jimmer',
    'age': 23,
    'scout rank': 'Eagle',
    'scout badges': [],
}

print(f"I know {guy_dict1['name']} has three scout badges, what are they?")
guy_dict1['scout badges'].append(input("The first badge is: "))
guy_dict1['scout badges'].append(input("The second badge is: "))
guy_dict1['scout badges'].append(input("The third badge is: "))
print(guy_dict1)