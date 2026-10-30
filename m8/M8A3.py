# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 8 Assignment 3

first_num=input("What is the first number? (or type q to quit) ")
while first_num != 'q':
    second_num=input("What is the second number? ")
    try:
        answer = float(first_num) / float(second_num)
    except ZeroDivisionError:
        print("You cannot divide by zero")
    else:
        print(f"{first_num} / {second_num} is {answer}")
    first_num=input("What is the first number? (or type q to quit) ")
print("The program is over")
