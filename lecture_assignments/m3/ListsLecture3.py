# CPSC223P Lecture
# September 8, 2026
# Topic: More Lists: Tuples and Slicing

#create list by casting a range
num_list = list(range(0, 100))

print(num_list)
#slice lists using the colon operator
print(num_list[2:9]) #everything from/including index 2 to/excluding index 9
print(num_list[2:])  #everything from/including index 2 to the end
print(num_list[:9])  #everything from/including index 0 to/excluding index 9

new_list = num_list[:]
for i in range(0, len(new_list)):
    new_list[i] *= 2

print(f"The original list is:")
print(num_list)
print(f"The new list is:")
print(new_list)

print(num_list[5:-2])