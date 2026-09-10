# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 2 Assignment 3

uber_list = list(range(100, 201, 2))
total_int = 0
avg = 0
idx_a = 0
idx_b = 0
slice_sz = 0

idx_a = int(input("What is the start of your slice? "))
idx_b = int(input("What is the end of your slice? "))
data_list = uber_list[idx_a:idx_b]
slize_sz = len(data_list)
for idx in range(0, slize_sz):
    total_int += data_list[idx]
avg = total_int / slize_sz

print(f"Your slice contains {slize_sz} values and has an average value of {avg}")