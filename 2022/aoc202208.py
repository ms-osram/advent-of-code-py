from sys import stdin
import numpy

tree_height = []

for line in stdin:
    tree_row = [int(x) for x in str(line.strip())]
    tree_height.append(tree_row)

print(len(tree_height))
print(len(tree_height[0]))

def part1(tree_height):
    visible_trees = 0
    highest_scenic_score = 0
    for i in range(len(tree_height)):
        for j in range(len(tree_height[0])):
            t = tree_height
            tree = t[i][j]
            scenic_directions = []

            #print("Tree Height: {}".format(tree))
            
            if i == 0 or i == len(tree_height)-1 or j == 0 or j == len(tree_height[0])-1:
                continue
            # write a boolean here, probably a false value
            value_checker = [False, False, False, False]
            
            for up in range(0, i, 1):
                #print("Up: ", tree_height[up][j])
                if tree <= tree_height[up][j]:
                    # if a tree blocks the way, update the boolean and break out of this for loop
                    value_checker[0] = True  
                    break
                else:
                    scenic_directions.append(up-1)
                    print(scenic_directions)

            #if value_checker == True:
                #continue
            # if the boolean is different, use continue
            # do the same for the other for loops        
            for down in range(i+1, len(tree_height)):
                #print("Down: ", tree_height[down][j])
                if tree <= tree_height[down][j]:
                    value_checker[1] = True  
                    break
                else:
                    scenic_directions.append(down-1)
                    print(scenic_directions)

            for left in range(0, j, 1):
                #print("Left: ", tree_height[i][left])
                if tree <= tree_height[i][left]:
                    value_checker[2] = True  
                    break
                else:
                    scenic_directions.append(left-1)
                    print(scenic_directions)

            #if value_checker == True:
                #continue

            for right in range(j+1, len(tree_height[0])):
                #print("Right: ", tree_height[i][right])
                if tree <= tree_height[i][right]:
                    value_checker[3] = True  
                    break
                else:
                    scenic_directions.append(right-1)
                    print(scenic_directions)

            if all(value_checker) == True:
                continue
            else:
                scenic_score = numpy.prod(scenic_directions)
                if scenic_score > highest_scenic_score:
                    highest_scenic_score = scenic_score

                scenic_directions = []


            visible_trees += 1
            #print("Tree with height of {} is visible".format(tree))
            

    total_visible_trees = 2*len(tree_height)+ 2*(len(tree_height[0])-2) + visible_trees
    print("{} trees are visible from outside the grid.".format(total_visible_trees))
    print(highest_scenic_score)
    return total_visible_trees

def part2(tree_height):
    pass

part1(tree_height)