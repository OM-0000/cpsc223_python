# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 6 Assignment 5

def comp_avg(*nums):
    sum = 0
    for n in nums:
        sum += n
    return (sum/len(nums))

def comp_max(*nums):
    max = nums[0]
    for n in nums:
        if n > max:
            max = n
    return max

def comp_min(*nums):
    min = nums[0]
    for n in nums:
        if n < min:
            min = n
    return min