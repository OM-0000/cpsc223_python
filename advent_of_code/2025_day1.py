# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Advent of Code 2025 Challenge 1


with open("puzzle_input.txt") as file_object:
    input_list = file_object.readlines();


arrow = 50
zero_count = 0
for item in input_list:
    instr_str = item.strip()
    direction = instr_str[0]
    count = int(instr_str[1:])
    if direction == 'L':
        count *= -1
    elif direction != 'R':
        print("Invalid direction")
        exit()

    flag = arrow == 0

    n = abs(count)//100
    zero_count += n
    if count < 0:
        count += n*100
    elif count > 0:
        count -= n*100
    arrow += count

    arrow %= 100

    if arrow == 0 and not flag:
        zero_count += 1
        

print(f"Zero count: {zero_count}")

