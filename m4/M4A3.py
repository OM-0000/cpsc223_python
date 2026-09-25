# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 4 Assignment 3

games_dict = {}
for itr in range(1,4):
    game_str = input("What is a great game? ")
    system_str = input("What system can I play that on? ")
    games_dict[game_str] = system_str
print("That's too many, let's get rid of one")
remove_str = input("What game should we remove? ")
del games_dict[remove_str]
print("The new dictionary is:")
for game, system in games_dict.items():
    print(f"You can play {game} on {system}")
