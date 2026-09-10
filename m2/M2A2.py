# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 2 Assignment 2

g_list = ['Mortal Kombat', 'Contra', 'Streets Of Rage', 'Shinobi', 'Sonic', 'Phantasy Star']
print("Here are the top Sega games:")
for idx in range(0, len(g_list)):
    print(g_list[idx])
rmv_str = input("Which one do you think should be removed? ")
for idx in range(0, len(g_list)):
     if g_list[idx] == rmv_str:
          del(g_list[idx])
          break
print("Here are the new top Sega games:")
for idx in range(0, len(g_list)):
    print(g_list[idx])