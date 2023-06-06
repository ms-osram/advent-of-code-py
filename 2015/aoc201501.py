from sys import stdin

directions = []

# reads directions from standard input and converts them to a list 
for line in stdin:
    for l in line:
        directions.append(l.strip())

#calculates the resulting floor number based on the directions list
def part1(directions): 
    floor_number = 0 
    for d in directions:
        if d == "(":
            floor_number += 1
        else:
            floor_number -= 1
    print("The instructions take santa to floor {}.".format(floor_number)) 
    return floor_number

#calculates the position of the character that causes Santa to enter the basement (floor_number = -1) for the first time.
def part2(directions): 
    floor_number = 0
    x = 0
    while x <= (len(directions)-1):
        if directions[x] == "(":
            floor_number += 1
            x += 1
        else:   
            floor_number -= 1
            x += 1
            
        if floor_number == -1:
            break
    print("The position of the character that causes Santa to first enter the basement is at {}.".format(x))  
    return x

day1(directions)
day2(directions)