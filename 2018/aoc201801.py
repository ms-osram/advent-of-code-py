from sys import stdin
from itertools import cycle

frequency_changes = list()

for line in stdin:
    frequency_changes.append(int(line.rstrip()))

def part1(frequency_changes):
    resulting_frequency = 0
 
    for number in frequency_changes:
        resulting_frequency += number
        
    print("For Part 1: The resulting frequency is {}.".format(resulting_frequency))
    return resulting_frequency

def part2(frequency_changes):
    resulting_frequency = 0

    results =  set() 
    for number in cycle(frequency_changes):
        resulting_frequency += number
        
        if resulting_frequency in results:
            print("For Part 2: The first frequency that the device reaches twice is {}.".format(resulting_frequency))
            break
        results.add(resulting_frequency)

    return resulting_frequency

part1(frequency_changes)
part2(frequency_changes)