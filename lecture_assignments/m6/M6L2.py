#Lecture 2: Function return values

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name

var_name = get_formatted_name("Jim", "Diresta")
print(var_name)

def mult(num1, num2):
    return num1*num2

value = mult(3, 5)
print(value)

def get_fav_food():
    foods_dict = {}
    fav_food = ""
    while fav_food != 'q':
        fav_food = input("Enter your favorite food or 'q' to quit: ")
        if fav_food == 'q':
            break
        country = input("What country is that food from? ")
        foods_dict[fav_food] = country
    return foods_dict

empty_list = get_fav_food()
print(empty_list)