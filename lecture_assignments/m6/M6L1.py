#Intro to functions

def greet_user(username):
    print(f"Hello there, {username}.")

greet_user("Jimmy")
greet_user("Jumbo")
greet_user("Whatever")

#Parameters v.s. functions
#Parameter is local to the function, it's more like the definition and use of the variable for the function
#Argument is passed into the function. So something external passes an argument into a function.

def greet_user(firstname, lastname):
    print(f"Hello {firstname} {lastname}")

#Since python is a softly typed language, you can pass any data type as arguments to the function
greet_user("Jimmy", "Diresta")
greet_user(1, "Diresta")

#So even though positional parameters are used like with every language, python has an interesting concept called "keyword passing"
greet_user(lastname = "Diresta", firstname="Jimmy") #still prints "Jimmy Diresta"

#So I overloaded the greet_user function. Thus it can run with either one or two arguments.
#However if you try to run it with 0 or more than 2 arguments, it won't run.
#greet_user() would through an error

#We can however define defaults to allow functions to not require arguments to run
def double_it(num=21):
    print(f"{2*num}")

double_it(27) #will double your argument
double_it()   #will double its default parameter of 21

#Note: default parameters must be defined at the end
#So this wouldn't work:
#def function(paramA='', paramB)
#But this would:
def function(paramA, paramB=''):
    print(f"{paramA} needs an argument to be passed, but {paramB} has a default value.")

function("turtle")