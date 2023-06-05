from sys import stdin
from collections import deque

signal = []

for line in stdin:
    signal = list(line)

def part1(signal):
# Initializing a queue
    q = deque()
      
    # Adding elements to a queue
    q.extend(signal[0:3])

    index = 3
    while index < len(signal): 
        q.append(signal[index])
        if len(q) == len(set(q)):
            print("The first start-of-packet marker is detected after {} characters.".format(index+1))
            break
        else:
            q.popleft()
            index += 1


def part2(signal):
    # Initializing a queue
    q = deque()
      
    # Adding elements to a queue
    q.extend(signal[0:13])

    index = 13
    while index < len(signal): 
        q.append(signal[index])
        if len(q) == len(set(q)):
            print("The first start-of-message marker is detected after {} characters.".format(index+1))
            break
        else:
            q.popleft()
            index += 1

part1(signal)
part2(signal)

