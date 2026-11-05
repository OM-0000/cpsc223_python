# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 9 Assignment 1

population_dict = {}

city_str = input("What is next city? (enter q to quit) ")
while city_str != 'q':
    population_str = input(f"What is the population of {city_str}? ")
    population_dict[city_str] = int(population_str)
    city_str = input(f"What is next city? (enter q to quit) ")

threshold_pop_int = int(input("What is the largest population for a small town? "))

big_cities_list=[]
small_cities_list=[]
for city, pop in population_dict.items():
    if pop > threshold_pop_int:
        big_cities_list.append(f"{city},{pop}")
    if pop < threshold_pop_int:
        small_cities_list.append(f"{city},{pop}")

with open("populationdata.txt", "w") as file_object:
    print("Big Cities:", file=file_object)
    for city in big_cities_list:
        print(city, file=file_object)
    print("Small Towns:", file=file_object)
    for city in small_cities_list:
        print(city, file=file_object)