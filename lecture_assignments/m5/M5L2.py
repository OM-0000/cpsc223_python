#Counting loops

#Preferred: use for-loops
for x in range(5):
    print(x)

#Also works: use while-loops
count_int = 0
while count_int < 5:
    print(count_int)
    count_int += 1

print()
print()

#Two ways to ensure the 'quit' value doesn't show up in the list. (you could also use if, but if adds an extra check every loop.)
mylist = []
user_input = ''
while user_input != 'quit':
    user_input = input("What is the next food choice? (or 'quit' to end) ")
    mylist.append(user_input)
mylist.pop()
print(mylist)


mylist = []
user_input = input("What is the next food choice? (or 'quit' to end) ")
while user_input != 'quit':
    mylist.append(user_input)
    user_input = input("What is the next food choice? (or 'quit' to end) ")
print(mylist)

#Random note: you can use r-strings to not interpret special characters. Useful for file paths.
#             you can also do rf strings to get the previous characteristic, but also allow for {} to be interpretted and use variagles


#Here you can use break or keep_going = false to break out of the loop.
keep_going = True
while keep_going:
    user_input = input(rf"C:\Program Files Enter a program name? ")
    print(user_input.upper())
    if len(user_input) < 5:
        break
print(f"Done with the loop")

