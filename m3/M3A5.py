# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 3 Assignment 5

start_int = int(input("What is the first number? "))
end_int = int(input("What is the second number? "))
num_list = list(range(start_int, end_int+1, 5))
sum_int = 0
for item in num_list:
    if item%5 == 0:
        sum_int += item
print(f"The total value of multiples from {start_int} to {end_int} is {sum_int}")
