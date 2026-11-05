# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 9 Assignment 3

def print_board(list_arg):
    for i in range(1, 2*len(list_arg)+2):
        print("-", end="")
    print("")
    for iitem in list_arg:
        for jitem in iitem:
            print("|", end="")
            print(jitem, end="")
        print("|")
        for i in range(1, 2*len(list_arg)+2):
            print("-", end="")
        print("")
    


board1_list = [['*','*','*'],
               ['*','+','*'],
               ['*','*','*']]
print_board(board1_list)
print() #just for a spacer line
board2_list = [['*',' ',' ','*'],
               ['*',' ',' ','*'],
               ['*',' ',' ','*'],
               ['*',' ',' ','*']]
print_board(board2_list)
print() #just for a spacer line
board3_list = [['*',' ','*',' ','*'],
               [' ','*',' ','*',' '],
               [' ',' ',' ',' ',' '],
               [' ','+',' ','+',' '],
               ['+',' ','+',' ','+']]
print_board(board3_list)