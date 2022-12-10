import itertools

rucksacks = []

values = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
value = list(values)
print(value)
while True:
    
    inp = ""
    try: inp = input()
    except EOFError:
        break

    rucksacks.append(inp)

#print(rucksacks)

def day1(rucksacks):
    letters = []
    letter_values = []
    for rucks in rucksacks:
        div = len(rucks)//2

        a = set(rucks[:div])
        b = list(rucks[div:])

        for item in b:
            if item in a:
                print("The common letter is: ", item)
                letters.append(item)
                letter_values.append(values.index(item))
                break
        
    print("The answer for day 1 is: ", sum(letter_values))

day1(rucksacks)
print("\n")



new_rucksacks = []
intersectionValues = []
def day2(rucksacks):
    for r in rucksacks:
        new_item = list(r)
        new_rucksacks.append(new_item)

    new_list = list(zip(*(iter(new_rucksacks),)*3))


    for lists in new_list:
        
        x = set(lists[0])
        y = set(lists[1])
        z = set(lists[2])  
        print(x,y,z)        
        
    
        listIntersection = x.intersection(y,z)
        mostCommonLetter = list(listIntersection)


        print("The intersection is:", (mostCommonLetter))
        print("The corresponding value is:", value.index(mostCommonLetter[0]))
        intersectionValues.append(value.index(mostCommonLetter[0]))

    print("The answer for day 2 is: ", sum(intersectionValues))

day2(rucksacks)

