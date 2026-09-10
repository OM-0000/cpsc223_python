# CPSC223P Lecture
# September 8, 2026
# Topic: Lists

#Initialize/create a list in python
my_list = ["I", 2, "ready"]

#Modify the last item in my_list
my_list[-1] = "late"
#print the last item and the size
print(my_list[len(my_list)-1])
print(f"My list is {len(my_list)} items")

#modify the list by appending two additional items to the end of the list.
my_list.append("for")
my_list.append("work")
#insert an item into the 1st index
my_list.insert(1, "will")
print(my_list)
#Using pop to remove the last item from the list (and also print that item before losing it)
print(f"The last item in my list was {my_list.pop()}")
print(my_list)
#Using del to remove the last item from the list
del(my_list[-1])
print(my_list)

#Creating a new list
new_list = ["I", "am", "the", "very", "model", "of", "a", "modern", "general"]
print(new_list)
#sorted(new_list) returns a sorted list but doesn't modify the original list
print(sorted(new_list))
print(new_list)
#new_list.sort() returns none, but it modifies the original list
new_list.sort()
print(new_list)
#reverse
new_list.reverse()
print(new_list)