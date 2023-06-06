from sys import stdin
rangePairs = []

for line in stdin:    
    x = line.replace("-", ",")
    splitx = x.split(",")
    rangePairs.append(splitx)
    

intPairs = []
for ranges in rangePairs:
    sublist = []   
    for r in ranges:
        x = int(r)
        sublist.append(x)

    intPairs.append(sublist)

pairCounter = 0
intersectionCounter = 0

for pairs in intPairs:
    x1 = pairs[0]
    x2 = pairs[1] + 1

    y1 = pairs[2]
    y2 = pairs[3] + 1

    firstPair = set([*range(x1, x2)])
    secondPair = set([*range(y1,y2)])

    if (firstPair.issubset(secondPair)) or (secondPair.issubset(firstPair)) == True:
        pairCounter += 1

    intsect = firstPair.intersection(secondPair) 
    if len(intsect) != 0:
        intersectionCounter += 1


print("Total Count of subsets is {}.".format(pairCounter))
print("The total number of intersectioning pairs is {}.".format(intersectionCounter))


