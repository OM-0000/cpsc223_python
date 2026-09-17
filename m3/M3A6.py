# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 3 Assignment 6

name_str = input("What is the student name? ")
score_int = int(input("What is their score? "))
if score_int <= 59:
    print(f"{name_str} earned an F")
elif score_int <= 69:
    print(f"{name_str} earned a D")
elif score_int <= 79:
    print(f"{name_str} earned a C")
elif score_int <= 89:
    print(f"{name_str} earned a B")
elif score_int <= 100:
    print(f"{name_str} earned an A")
