# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 8 Assignment 4

def dictionary_maker(filepath):
    ret_dict = {}
    try:
        with open(filepath) as file_object:
            for line in file_object:
                line = line.strip()
                pair=line.split(':')
                ret_dict[pair[0]]=pair[1]
    except FileNotFoundError:
        print(f"The file {filepath} does not exist on this system")
    
    return ret_dict

print(dictionary_maker(input("What is the file with the data? ")))
