from sys import stdin

instructions = list()

for line in stdin:
    instructions.append(line.strip())

def part1(instructions):
    code = []

    x = 0
    y = 0

    keypad = {
        (-1,1): 1,
        (0,1): 2,
        (1,1): 3,
        (-1,0): 4,
        (0,0): 5,
        (1,0): 6,
        (-1,-1): 7,
        (0,-1): 8,
        (1,-1): 9
    }

    for instruction in instructions:
        for letter in instruction:
                
            if letter == "U":
                y += 1
            elif letter == "D":
                y -= 1
            elif letter == "L":
                x -= 1
            elif letter == "R":
                x += 1
                
            if x > 1:
                x = 1
            elif x < 0:
                x = -1
            
            if y > 1:
                y = 1
            elif y < 0:
                y = -1
            
            coordinates = (x, y)
        number = keypad[coordinates]
        code.append(number)

    string = [str(i) for i in code]
    answer = int("".join(string))
    print("For Part 1: The bathroom code is {}.".format(answer))

def part2(instructions):
    code = []

    x = 0
    y = 0

    keypad = {
        (2,2): '1',
        (1,1): '2',
        (2,1): '3',
        (3,1): '4',
        (0,0): '5',
        (1,0): '6',
        (2,0): '7',
        (3,0): '8',
        (4,0): '9',
        (1,-1): "A",
        (2,-1): "B",
        (3,-1): "C",
        (2,-2): "D"
    }

    for instruction in instructions:
        for letter in instruction:
            if x == 0:
                if letter == "R":
                    x += 1
                
                if y != 0:
                    y = 0
                    
            elif x == 1:
                
                if y == 1:
                    if letter == "D":
                        y -= 1
                    elif letter == "R":
                        x += 1
                        
                elif y == 0:
                    if letter == "U":
                        y += 1
                    elif letter == "D":
                        y -= 1
                    elif letter == "L":
                        x -= 1
                    elif letter == "R":
                        x += 1
                        
                elif y == -1:
                    if letter == "U":
                        y += 1
                    elif letter == "R":
                        x += 1
                
                # checks limit of y at x=1
                if y > 1:
                    y = 1
                elif y < -1:
                    y = -1
                    
            elif x == 2:
                
                if y == 2 or y == -2:
                    if letter == "U":
                        y += 1
                    elif letter == "D":
                        y -= 1
                elif -2 < y < 2:
                    if letter == "U":
                        y += 1
                    elif letter == "D":
                        y -= 1
                    elif letter == "L":
                        x -= 1
                    elif letter == "R":
                        x += 1
                # checks limit of y at x=2
                if y > 2:
                    y = 2
                elif y < -2:
                    y = -2
                
            elif x == 3:
            
                if y == 1:
                    if letter == "D":
                        y -= 1
                    elif letter == "L":
                        x -= 1
                        
                elif y == 0:
                    if letter == "U":
                        y += 1
                    elif letter == "D":
                        y -= 1
                    elif letter == "L":
                        x -= 1
                    elif letter == "R":
                        x += 1
                        
                elif y == -1:
                    if letter == "U":
                        y += 1
                    elif letter == "L":
                        x -= 1
                
                # checks limit of y at x=1
                if y > 1:
                    y = 1
                elif y < -1:
                    y = -1
                # checks limit of y at x=1
                if y > 1:
                    y = 1
                elif y < -1:
                    y = -1
                
            elif x == 4:
                if letter == "L":
                    x -= 1
                
                if y != 0:
                    y = 0
            
            coordinates = (x, y)
        
        key = keypad[coordinates]
        code.append(key)
    answer = "".join(code)
    print("For Part 2: The correct bathroom code is {}.".format(answer))

part1(instructions)
part2(instructions)