from sys import stdin

input = []


# reads input from standard input per line, then separates one character from another
# then append to a list of which becomes the set of directions for movement

for line in stdin:
    for l in line:
        input.append(l)


# for part 1, Santa moves based on the directions given by the input 
def part1(input):
    # initializes the position of Santa at (0, 0)
    santa_x = 0
    santa_y = 0

    # initializes the set of coordinates that has received at least one present
    house_coords = {(0,0)}

    for direction in input: 
        if direction == "^":
            santa_y += 1

        elif direction == ">":
            santa_x += 1
            
        elif direction == "<":
            santa_x -= 1
            
        elif direction == "v":
            santa_y -= 1
            
        else:
            pass
        
        coords = (santa_x, santa_y)
        
        house_coords.add(coords)

    print("Part 1: There are {} houses that receive at least one present.".format(len(house_coords)))
    return len(house_coords)    


# for part 2, Santa and Robo-Santa take turns on moving based on the input.
# the coordinates that are added on the set depend on whose turn it is to move 
def part2(input):

    # initializes Santa's position at (0,0)
    santa_x = 0
    santa_y = 0

    # initializes Robo-Santa's position at (0,0)
    robo_x = 0
    robo_y = 0

    # initializes the set of coordinates that has received at least one present
    # from Santa and Robo-Santa
    house_coords = {(0,0)}

    for i, input in enumerate(input):
        if i % 2 == 0:
            if input == "^":
                santa_y += 1
            elif input == "v":
                santa_y -= 1
            elif input == "<":
                santa_x -= 1
            elif input == ">":
                santa_x += 1

            coords = (santa_x,santa_y)

        else:
            if input == "^":
                robo_y += 1
            elif input == "v":
                robo_y -= 1
            elif input == "<":
                robo_x -= 1
            elif input == ">":
                robo_x += 1

            coords = (robo_x, robo_y)
        
        house_coords.add(coords)

    print("Part 2: There are {} houses that receive at least one present.".format(len(house_coords)))
    return len(house_coords) 

day1(input)
day2(input)