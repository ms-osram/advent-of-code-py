directions = []

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



def main_head_movement(length): 
    elements = [(0,0) for x in range(length)]

    hx = elements[0][0]
    hy = elements[0][1]
    
    coveredPositions = set()

    for d in directions:
        
        for i in range(d[1]):
            # only for the main head
            
            if d[0] == "U":
                hy += 1

            elif d[0] == "D":
                hy -= 1

            elif d[0] == "L":
                hx -= 1

            elif d[0] == "R":
                hx += 1

            elements[0] = (hx, hy)         
               
            for h in range(len(elements)-1):
                hCoords = elements[h]
                tCoords = elements[h+1]
                elements[h+1] = tail_movement(hCoords, tCoords)
            coveredPositions.add(elements[-1])
            
    return print("The number of Covered Positions by the tail is: {}".format(len(coveredPositions)))

def tail_movement(hCoords, tCoords):
    dRange = ((0,0), (1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,-1),(-1,1))    
    hx = hCoords[0]
    hy = hCoords[1]    

    tx = tCoords[0]
    ty = tCoords[1]

    dx = hx - tx
    dy = hy - ty
    dCoords = (dx, dy)

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
    return (tx, ty)


main_head_movement(2)
main_head_movement(10)
    
