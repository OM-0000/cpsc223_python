mylist = ['jim', 'joe', 'tom', 'sally']

while mylist:
    print(f"The last person on the list is {mylist.pop()} and now there are {len(mylist)} on it")

fav_foods = []
user_input = input("What is your favorite food? ('q' for quit) ")
while user_input != 'q':
    fav_foods.append(user_input)
    user_input = input("What is your favorite food? ('q' for quit) ")
print(fav_foods)
while 'pizza' in fav_foods:
    fav_foods.remove('pizza')
print(fav_foods)