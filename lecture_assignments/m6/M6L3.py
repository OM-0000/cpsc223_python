#Lecture 3: Functions with Lists as Parameters

def dummy(names_list):
    names_list.append('Jill')
    for name in names_list:
        print(f"Welcome {name}")

n_list = ['Jim', 'John', 'Pretzel']

print(f"The list is {n_list}")
dummy(n_list)
print(f"The list is {n_list}")

#lists are passed by reference in functions, so changes to that list that happen inside the function apply to the argument itself even outside the function.
#But single variables are not the passed by reference, but by value. The function will make a copy of them. So changes to them wouldn't affect the argument.

#However, if you don't want to pass the list in by reference, use "slice" (colon operator)
print(f"The list is {n_list}")
dummy(n_list[:])
print(f"The list is {n_list}")

#Arbitrary number of variables denoted with *
def dummy2(*names):
    for name in names:
        print(f"Welcome {name}")
#Pass in a tuple, which is an immutable list (can't be changed). Is another way to prevent the function from changing anything.
dummy2('Jim', 'Joe', 'Billybob')

#You could also have a variable before *names. a tuple passed to this function, d3, would take the first argument as int_var, and then the remaining arguments as *names
def d3(int_var, *names):
    for name in names:
        print(f"Welcome {name}")

#**kwargs is equivalent to a dictionary
def d4(int_var, **kwargs):
    for name in names:
        print(f"Welcome {name}")

#Finally, how to unpack a list into an arbitrary set of variables

def unpack_list(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

#items_list = ['item1', 'item2', 'item3', 'item4'] won't work; too many arguments
items_list = ['item1', 'item2', 'item3']
unpack_list(*items_list)

#For dictionaries:

def func1(a1, a2, a3):
    print('a1 =', a1)
    print('a2 =', a2)
    print('a3 =', a3)

def func2(arg1, arg2, arg3):
    print('a1 =', arg1)
    print('a2 =', arg2)
    print('a3 =', arg3)

d = {'arg1': 'one', 'arg2': 'two', 'arg3': 'three'}
#func1(**d) won't work because the key values don't match the parameter names
func2(**d) #works
