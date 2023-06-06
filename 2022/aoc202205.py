from copy import deepcopy
from sys import stdin
from collections import deque

instructions = []
steps = []
stacks = [[],[],[],[],[],[],[],[],[]]

for line in stdin:
    if line == "\n":
        break
    for (crate, stack) in zip(line[1::4], stacks):
        if crate == " ":
            continue    
        stack.append(crate)

for line in stdin:
    x = line.replace("move ","").replace(" from ", " ").replace(" to ", " ")
    xSplit = x.split(" ")

    step = []
    for splits in xSplit:
        step.append(int(splits))
    instructions.append(step)
    step = []

for stack in stacks:
    try:
        stack.pop()
    except IndexError:
        break
    stack.reverse()

    for crate in stack:
        print("[" + crate + "]", end=" ")
    print()

def part1(steps, stacks):
    message = []
    for stp in steps:
        n = stp[0]
        x1 = stp[1]-1
        x2 = stp[2]-1

        for i in range(n):
            stacks[x2].append(stacks[x1].pop())

    for m in range(len(stacks)):
        message.append(stacks[m][-1])

    joinMessage = "".join(message)
    print("The message for Part 1 is {}.".format(joinMessage))
    return joinMessage

def part2(steps, stacks):
    message = []
    for stp in steps:
        n = stp[0]
        x1 = stp[1]-1
        x2 = stp[2]-1
        
        rev = []
        for i in range(n):
            rev.append(stacks[x1].pop())

        rev.reverse()
        stacks[x2].extend(rev)
            
    for m in range(len(stacks)):
        message.append(stacks[m][-1])

    joinMessage = "".join(message)
    print("The message for Part 2 is {}.".format(joinMessage))
    return joinMessage
    
part1(instructions, deepcopy(stacks))
part2(instructions, stacks)