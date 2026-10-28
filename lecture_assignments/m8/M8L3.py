#Open in append mode and write to file
with open('tmp.txt', 'a') as file_object:
    file_object.write('Hidy ho\n')
    file_object.write('What is up\n')

#Another way to write using the print statement and passing in the file_object into print
with open('tmp.txt', 'a') as file_object:
    print('This came from my first print statement', file=file_object)
    print('This came from my second print statement', file=file_object)

with open('tmp.txt', 'a') as file_object:
    user_input = input("what do you want to save forever? (q to quit) ")
    while user_input != 'q':
        print(user_input, file=file_object)
        # you could use file_object.flush() here to force writes to go through before the file is closed by the with statement
        # another option is to specify flush=True in the print statement itself
        # but it might not work here. it's a mystery when, where, or why it will sometimes work and sometimes not.
        user_input = input("what do you want to save forever? (q to quit) ")

print("Check your file")