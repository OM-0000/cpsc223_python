with open("The United States' Constitution _ Project Gutenberg.txt") as file_object:
    text = file_object.read()

#print(text)

with open("The United States' Constitution _ Project Gutenberg.txt") as file_object:
    text = file_object.readlines()

#New option for print. You can specify what it prints at the end. By default, that's a newline. You can make it print nothing at the end of its argument.
for line in text:
    if line != '\n':
        #print(line, end="")
        continue #comment this out if you want to uncomment the above

#Using a for loop directly on the file object works only within the with statement
with open("The United States' Constitution _ Project Gutenberg.txt") as file_object:
    for line in file_object:
        if line != '\n':
            #print(line.strip())
            continue #comment this out if you want to uncomment the above

#Turn string into list
with open("The United States' Constitution _ Project Gutenberg.txt") as file_object:
    text = file_object.read()

text_list = text.split('\n')
for line in text_list:
    print(line)