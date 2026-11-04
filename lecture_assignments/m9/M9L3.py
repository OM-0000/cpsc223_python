#More strings

#slicing

str = '    hello    '

print(str[:])
print(str[4:9])
print(str.strip()) #removes white space by default

str = "###hello###"
print(str.strip('#')) # removes hashes

#Note strip removes leading/trailing elements only
str = ' \n \t hello\n'
print(str)
print(str.strip('\n')) #won't remove the first newline

#More stripping
str = 'www.example.com'.strip('cmow.') #will remove all c's, m's, o's, w's and dots
print(str)

str = '    hello    '.lstrip()
print(str)
str = '    hello    '.rstrip()


#Remove prefix and removesuffix

str = 'Arthur: three!'.lstrip('Arthur: ')
print(str)

str = 'Arthur: three!'.removeprefix('Arthur: ')
print(str)

str = 'HelloPython'.removesuffix('Python')
print(str)

#Replace
str = 'string methods in python'.replace(' ', '') #will remove all the space (by replacing space with \0)
print(str)

#re.sub

import re
s = "string    methods in python"
s2 = re.sub("\s+", "-", s) #regex
print(s2)

#Split
s = 'string methods in python'.split(' ', maxsplit = 1)
print(s)

#rsplit
s = 'string methods in python'.rsplit(' ', maxsplit = 1)
print(s)

# join()

list_of_strings = ['string', 'methods', 'in', 'python']
s = '-'.join(list_of_strings)
print(s)

# upper(), lower(), capitalize()

s = 'python is awesome!'.upper()
print(s)

s = 'python is awesome!'.lower()
print(s)

s = 'python is awesome!'.capitalize() #only capitalize the first letter of the string
print(s)


# islower(), isupper()

print(s.upper().isupper()) #returns True because ALL characters are uppercase
print(s.isupper()) # returns False because only the first character is capital/uppercase

print(s.lower().islower()) #returns True because ALL characters are lowercase
print(s.islower()) #returns False because the first character is not lowercase

# isalpha(), isnumeric(), isalnum()

s = 'python'
print(s.isalpha(), s.isnumeric(), s.isalnum()) #true, false, true
s = 'python3'
print(s.isalpha(), s.isnumeric(), s.isalnum()) #true, false, true
s = '312'
print(s.isalpha(), s.isnumeric(), s.isalnum()) #true, true, true
s ='...'
print(s.isalpha(), s.isnumeric(), s.isalnum()) #false, false, false
s ='123...python'
print(s.isalpha(), s.isnumeric(), s.isalnum()) #false, false, false


# count()

n = 'hellow world'.count('o')
print(n)
n = 'hello world'.count('oo')
print(n)



# find() starts from the left and scans to the right

s = 'Machine Learning'
idx = s.find('a', 2)

print(idx)
print(s[idx:])

# rfind() starts from the right and scans to the left

s = 'Machine Learning'
idx = s.rfind('a')

print(idx)
print(s[idx:])

# startswith and endswith

print('Patrick'.startswith('P'))
print('Patrick'.endswith('ck'))

# partition()

classtime = '10:00 AM to 12:15 PM'
parsed_time = classtime.partition('to')
print(parsed_time)
#note. you could also do this to get rid of the 'to'
parsed_time = classtime.split('to')
print(parsed_time)


#center(), ljust(), rjust()

s = 'Python is a pretty solid language.'
str = s.center(60, '-')
print(str)
str = s.ljust(60, '-')
print(str)
str = s.rjust(60, '-')
print(str)



#Introducing... wait for it... F-STRINGS
num = 1
language = 'Python'
s = f'{language} is the number {num} in programming!'
print(s)

# swapcase()

s = 'HELLO world'
s = s.swapcase()
print(s)


# zfill()

s = '42'.zfill(5)
print(s)

s = '-42'.zfill(5)
print(s)

s = '+42'.zfill(5)
print(s)