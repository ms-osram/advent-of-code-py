directions = []
stepsNumber = []
while True:
    inp = ""
    try:
        inp = input()

    except EOFError:
        break
        
    xSplit = inp.split(" ")
    temp_list = []
    for splits in xSplit:
        if splits.isdigit(): 
            temp_list.append(int(splits))
        else: temp_list.append(splits)
    directions.append(temp_list)


# x and y coordinates of Head 
hx = 0 
hy = 0 

# x and y coordinates of Tail
tx = 0
ty = 0

# difference of H and T x and y coordinates

s = 0 #origin


coveredPositions = set()

hCoords = (hx, hy)
tCoords = (tx, ty)
dRange = ((0,0), (1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,-1),(-1,1))


print("Initial Head Coordinates: ", hCoords)
print("Initial Tail Coordinates: ", tCoords)

for d in directions:
    print(d[0])
    for i in range(d[1]):
        
        if d[0] == "U":
            hy += 1

        elif d[0] == "D":
            hy -= 1

        elif d[0] == "L":
            hx -= 1

        elif d[0] == "R":
            hx += 1

        dx = hx - tx
        dy = hy - ty
        dCoords = (dx, dy)
        print("DX: ", dx, "| DY: ", dy)
    
        if dCoords not in dRange:
            if dx >= 1 and dy >= 1:
                tx += 1
                ty += 1
            elif dx <= -1 and dy <= -1:
                tx -= 1
                ty -= 1
            elif dx >= 1 and dy <= -1:
                tx += 1
                ty -= 1
            elif dx <= -1 and dy >= 1:
                tx -= 1
                ty += 1 
            elif dx > 1 and dy == 0:
                tx += 1
            elif dx < -1 and dy == 0:
                tx -= 1
            elif dy > 1 and dx == 0:
                ty += 1
            elif dy < -1 and dx == 0:
                ty -= 1 

        hCoords = (hx, hy)
        tCoords = (tx, ty)
        print("Head Coordinates: ", hCoords)
        print("Tail Coordinates: ", tCoords)
        if tCoords not in coveredPositions:
            coveredPositions.add(tCoords)
            print("Covered Positions: ", coveredPositions)
            
                
print("Directions: ",directions)
#print("Number of Steps: ", stepsNumber)

print(coveredPositions)
print(len(coveredPositions))



