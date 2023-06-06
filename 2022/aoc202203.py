from sys import stdin
import itertools

rucksacks = []

values = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
value = list(values)

for line in stdin:
    rucksacks.append(line.strip())

def part1(rucksacks):
    letters = []
    letter_values = []
    for rucks in rucksacks:
        div = len(rucks)//2

        a = set(rucks[:div])
        b = list(rucks[div:])

        for item in b:
            if item in a:
                letters.append(item)
                letter_values.append(values.index(item))
                break
        
    print("The answer for day 1 is {}.".format(sum(letter_values)))
    return sum(letter_values)


new_rucksacks = []
intersectionValues = []
def part2(rucksacks):
    for r in rucksacks:
        new_item = list(r)
        new_rucksacks.append(new_item)

    new_list = list(zip(*(iter(new_rucksacks),)*3))


    for lists in new_list:
        
        x = set(lists[0])
        y = set(lists[1])
        z = set(lists[2])       
        
        listIntersection = x.intersection(y,z)
        mostCommonLetter = list(listIntersection)

        intersectionValues.append(value.index(mostCommonLetter[0]))

    print("The answer for day 2 is {}.".format(sum(intersectionValues)))
    return sum(intersectionValues)

part1(rucksacks)
part2(rucksacks)

