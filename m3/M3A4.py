# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 3 Assignment 4

age_int = int(input("What year is it now? ")) - int(input("What year were you born? "))
if age_int < 50:
    if age_int%2 == 0:
        print("This will be a great year")
    else:
        print("This year will be tough")
elif age_int == 50:
    print("The future is unclear")
else:
    print("Death will come for you soon")