from sys import stdin
import heapq

temp_list2 = []
temp_list1 = []

for line in stdin:
    inp = line.strip()
    if inp != '':
        temp_list1.append(int(inp))
    else:
        temp_list2.append(temp_list1)
        temp_list1 = []

calories = []

for n in temp_list2:
    calories.append(sum(n))

greatest_calories = heapq.nlargest(3, calories)   

print("Part 1: The elf carrying the most Calories carries {} calories.".format(greatest_calories[0]))
print("Part 2: The top three elves are carrying {} calories in total.".format(sum(greatest_calories)))
