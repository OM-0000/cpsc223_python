# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 4 Assignment 1

g_list = []
for itr in range(1,4):
    g_list.append(input(f"What is your number {itr} favorite PlayStation game? "))
for idx,game in enumerate(g_list, start=1):
    print(f"Your number {idx} favorite game was {game}")