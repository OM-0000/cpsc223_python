
message = 'Hello World'

print('Hello World')
print(message)

#Single quotes v.s. doublequotes

#Two ways to handle nested quotes/apostrophes
msg = 'Bobby\'s World'
print(msg)
msg = "Bobby's World"
print(msg)

#Printing length
print(len(msg))

#Printing from strings by indices
print(message[0])
print(message[5])

#print(message[15]) IndexError: string index out of range (b/c the length is 13 (indexed [0-12]))

#Printing slices
print(message[0:4]) #Prints index 0 to 3 ("Hell") (remember python tends to treat ranges like [indexA, indexB) <-- not including indexB)
print(message[6:]) #Prints index 6 to end ("World")

#Useful functions
print(message.lower())
print(message.upper())
print(message.count("Hello")) #counts number of times "Hello" appears in the string
print(message.count('l')) #counts number of times 'l' appears in the string

print(message.find('World'))  #returns the index where the given substring appears in the string
print(message.find('z')) # returns -1 because 'z' doesn't appear in the string
print(message.find('l')) # returns the index of the first occurance

new_message = message.replace('World', 'Universe')
print(new_message)

#Concatenation

greeting = 'Hello'
name = 'Ossama'

message = greeting + ', ' + name + '. Welcome!'
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

# Introducing... f-strings
message = f'{greeting}, {name}. Welcome!'
print(message)


# other stuff

print(dir(name)) #shows attributes and methods available on the variable
print(help(str)) #shows you a manual page for the data type