mylist = ["hot dogs", "hamburgers", "pizza"]

for food in mylist:
    print(f"The food is {food}")

#This C-style way of doing it works but is a faux paus in python for some reason (since, perhaps, lists aren't arrays and doing this suggests they might be)
for num in range(0, len(mylist)):
    print(f"Food number {num+1} is {mylist[num]}")
print("Python style enumeration")
#This is the Python way. It allows the python interpretter to run the code more efficiently. So there's your answer. Next question is obviously why.
for num, food in enumerate(mylist):
    print(f"Food number {num+1} is {food}")
print("Python-style enumeration specifying start to 1")
#You can optionally specify the start of the enumeration. (difference is subtle, look closely)
for num, food in enumerate(mylist, start=1):
    print(f"Food number {num} is {food}")