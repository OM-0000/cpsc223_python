# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 6 Assignment 4

def show_messages(messages_list):
    while len(messages_list) > 0:
        print(messages_list.pop())

msg_str = input("What is the next message? (type 'q' to quit) ")
my_messages = []
while msg_str != 'q':
    my_messages.append(msg_str)
    msg_str = input("What is the next message? (type 'q' to quit) ")
print("First time calling function")
show_messages(my_messages[:])
print("Second time calling function")
show_messages(my_messages[:])