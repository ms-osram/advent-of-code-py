tree_height = []

while True:
    inp = ""
    try:
        inp = input()

    except EOFError:
        break
        
    print(inp)
    tree_row = [int(x) for x in str(inp)]
    tree_height.append(tree_row)

for tree_rows in tree_height:
    print(tree_rows) # displays the trees

visible_trees = 0

for i in range(len(tree_height)):
    for j in range(len(tree_height[0])):
        t = tree_height
        tree = t[i][j]
        
        print("Tree Height: {}".format(tree))
        
        if i == 0 or i == len(tree_height)-1 or j == 0 or j == len(tree_height[0])-1:
            continue
        # write a boolean here, probably a false value
        value_checker = [False, False, False, False]
         
        for up in range(0, i, 1):
            print("Up: ", tree_height[up][j])
            if tree <= tree_height[up][j]:
                # if a tree blocks the way, update the boolean and break out of this for loop
                value_checker[0] = True  
                break

        #if value_checker == True:
            #continue
        # if the boolean is different, use continue
        # do the same for the other for loops        
        for down in range(i+1, len(tree_height)):
            print("Down: ", tree_height[down][j])
            if tree <= tree_height[down][j]:
                value_checker[1] = True  
                break

        for left in range(0, j, 1):
            print("Left: ", tree_height[i][left])
            if tree <= tree_height[i][left]:
                value_checker[2] = True  
                break

        #if value_checker == True:
            #continue

        for right in range(j+1, len(tree_height[0])):
            print("Right: ", tree_height[i][right])
            if tree <= tree_height[i][right]:
                value_checker[3] = True  
                break

        if all(value_checker) == True:
            continue

        visible_trees += 1
        print("Tree with height of {} is visible".format(tree))
        

total_visible_trees = 2*len(tree_height)+ 2*(len(tree_height[0])-2) + visible_trees
print("The total number of visible trees is: {}".format(total_visible_trees))
print("The tree's scenic score is: {}".format())
