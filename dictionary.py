#"cluji solution" i.e. solution works but comes with difficulties, like can't be sorted easily, etc.
cities_list = ['los angeles', 'long beach', 'sacremento']
pop_list = [7000000, 500000, 600000]

for index, city in enumerate(cities_list):
    print(f"The city of {city} has a population of {pop_list[index]}")

#Using dictionaries
cities_dict = {
    'los angeles': 7000000,
    'long beach': 500000,
    'sacramento': 600000,
}
#looping through dictionary by key
for city in cities_dict:
    print(f"The city of {city} has a population of {cities_dict[city]}")
#note that ... .keys() is the same
for city in cities_dict.keys():
    print(f"The city of {city} has a population of {cities_dict[city]}")
#looping through just the values
for values in cities_dict.values():
    print(f"{values}")
#looping through key-value pairs (returns tuples, i.e. "immutable lists"):
for pair in cities_dict.items():
    print(f"{pair}")
#Directly extracting the key, value pair
for city, pop in cities_dict.items():
    print(f"The city of {city} has a population of {pop}")

#Adding dictionary values (changes and adds)
cities_dict['los angeles'] = 7500000
cities_dict['san francisco'] = 6250000
for city, pop in cities_dict.items():
    print(f"The city of {city} has a population of {pop}")

#Attempting to access a non-existant key will throw a key-error
print(f"The population of {'fullerton'} is {cities_dict['fullerton']}")
#Using .get() will prevent error by checking if the key is in the dictinoary and returning none if it isn't.
#Well it should. Not sure what's going on.
print(f"The population of {'fullerton'} is {cities_dict.get('fullerton')}")

#Another way to deal with this sort of problem (namely uncertaintly about the present keys in the dictionary)

if 'fullerton' in cities_dict:
    print(f"The population of {'fullerton'} is {cities_dict.get('fullerton')}")
else:
    print(f"Fullerton not found")