from sys import stdin
import numpy as np 

triangles = []  
new_triangles = list()

for line in stdin:
    sides = [int(num) for num in line.rstrip().split()]
    triangles.append(sides)

def triangle_counter(triangles):
    counter = 0 
    for items in triangles:
        items.sort()
        if items[0]+items[1] > items[2]:
            counter += 1
    return counter
    
def group(triangles):
    
    for i in range(0, len(triangles), 3):
        array = np.array(triangles[i:i+3])
        transposed_array = array.T.tolist()
        #print(transposed_array)
        for arrays in transposed_array:
            new_triangles.append(arrays)
    
group(triangles)
        
print("For Part 1: There are {} possible triangles.".format(triangle_counter(triangles)))
print("For Part 2: There are {} possible triangles.".format(triangle_counter(new_triangles)))