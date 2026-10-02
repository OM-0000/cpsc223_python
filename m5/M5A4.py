# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 5 Assignment 4

orders_list = ['pastrami', 'turkey', 'pastrami', 'ham', 'turkey']
finished_list = []

while len(orders_list) > 0:
    temp_str = orders_list.pop()
    print(f"I made your {temp_str}")
    finished_list.append(temp_str)
print("Here are all the sandwiches I made:")
for item in finished_list:
    print(item)