# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 8 Assignment 2

with open("input.txt") as file_object:
    data_list = file_object.readlines();

with open("output.txt", 'w') as file_object:
    for line in data_list:
        print(line, end="", file=file_object)