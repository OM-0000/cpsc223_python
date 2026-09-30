print("Meal time.")
time = "Evening"
age = 21
if time == "Morning":
    print("Breakfast.")
elif time == "Midday":
    print("Lunch")
elif time == "Evening":
    print("Supper/dinner")
if age < 21:
    print("No beer for you.")
else:
    print("You may have beer, if you choose.")

engine_on = True
gas_tank_empty = False
car_starts = engine_on and not gas_tank_empty
if car_starts:
    print("vroom vroom")
    gas_tank_empty = True
if not engine_on or gas_tank_empty:
    car_starts = False
    print("You're having car troubles")

toppings = ['mushrooms', 'onions', 'pineapple', 'pepperoni', 'sausage']
#if "onions" in toppings:
#    print("Yum, onions")

customer = "Jim Carrey"
inp = input("Is Jim Carrey going to order pizza? (y/n)")
if (inp[0].lower() == "n"):
    customer = "Not Jim Carrey"
elif (inp[0].lower() == "y"):
    print("rip")
else:
    print("Your input wasn't recognized. You're Jim Carrey.")

request = input("What do you want on youra pizza? ")
if request.lower() in toppings:
    print(f"Yum, {request}.")
elif customer == "Jim Carrey":
    print("T h a z z a  s p i c y  u h  m e a t. b a l l.")
else:
    print(f"Sorry sir or madam, we don't have {request}")
    