mylist = ['the', 'name', 'is', 'bond']

if 'bond' in mylist:
    print(f'true')

age_int = int(input(f"How old are you? "))

if age_int < 16:
    print(f"You can't drive") 
print()
print(f"This is the end of the program")

if age_int % 2 == 0:
    print(f"{age_int} is even")

#accumulator variable : total_int
#iterator variable    : num_int
total_int = 0
for num_int in list(range(0, age_int, 2)):
    total_int += num_int
print(f"The total is {total_int} and the average is {total_int}")
