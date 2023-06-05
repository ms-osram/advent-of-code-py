from sys import stdin

directions = []

for line in stdin:
    coordinates = line.strip().split(", ")
    for c in coordinates:
        directions.append((c[0], int(c[1:])))


def part1(directions):
    orientation = 0
    coords_init = [0,0]
    coordinates = [(0,1),(1,0),(0,-1),(-1,0)]
    locations = list()

    x_coords = 0
    y_coords = 0

    for (direction, length) in directions:
        if direction == "R":
            orientation += 1
        else:
            orientation -= 1

        orientation_shift = orientation %  4

        x_coords += length * coordinates[orientation_shift][0]
        y_coords += length * coordinates[orientation_shift][1]

        location = [x_coords, y_coords]

        locations.append(location)
        destination_coords = locations[-1]

    manhattan_distance1 = abs(coords_init[0]-destination_coords[0])+abs(coords_init[1]-destination_coords[1])
    print("For Part 1: Easter Bunny HQ is {} blocks away.".format(manhattan_distance1))


def part2(directions):
    orientation = 0
    coords_init = [0, 0]
    coordinates = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited_coords = set()
    first_loc_visited_twice = None

    x_coords = 0
    y_coords = 0

    for (direction, length) in directions:
        if direction == "R":
            orientation += 1
        else:
            orientation -= 1

        orientation_shift = orientation % 4

        for r in range(length):
            x_coords += coordinates[orientation_shift][0]
            y_coords += coordinates[orientation_shift][1]
            loc = (x_coords, y_coords)
            if loc in visited_coords:
                first_loc_visited_twice = loc
                break
            visited_coords.add(loc)

        if first_loc_visited_twice is not None:
            break

    manhattan_distance = abs(coords_init[0] - first_loc_visited_twice[0]) + abs(coords_init[1] - first_loc_visited_twice[1])
    print("For Part 2: The first location visited twice is {} blocks away.".format(manhattan_distance))

part1(directions)
part2(directions)