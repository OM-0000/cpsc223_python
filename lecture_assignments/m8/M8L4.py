#flow control examples: if-else, while, functions
#so executing based on conditions, or branching to blocks of code on command is flow control
#errors are also a type of flow control

import os.path #allows os.path.exists(filename)

#Introducing Try-Except blocks
try:
    var1 = 5 / 0
except ZeroDivisionError:
    #print(f"var1 is {var1}") #gives you a NameError because var1 wasn't defined because of the DivideByZero error
    print("WTF BOOOOOOOOOOOOOM! AHAHHHAAH! AHHAHAHAHAHAHA!")
    var1 = 0
    print(f"var1 is {var1}") #now it works fine because we just defined var1
else:
    print(f"var1 worked fine")

filename = "junk.txt"
try:
    if os.path.exists(filename): #makes this try except structure superfluous here, but it's used often so you need to know it.
        with open(filename) as file_object:
            text = file_object.read()
except FileNotFoundError:
    #print(f"Sorry, but {filename} does not exist.")
    pass #pass keyword will just move on without doing anything
else:
    #print(text, end="")
    pass