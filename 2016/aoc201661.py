from sys import stdin
import itertools

strings = []  

for line in stdin:
    x = list(line.strip())
    strings.append(x)

def part1(strings):
    most_common_letter = list()
    for s in zip(*strings):
        most_frequent = (max(s, key=s.count))
        most_common_letter.append(most_frequent)

    answer = "".join(most_common_letter)
    print("For Part 1: The error-corrected version of the message is '{}'.".format(answer))

def part2(strings):
    least_common_letter = list()
    for s in zip(*strings):
        least_frequent = (min(s, key=s.count))
        least_common_letter.append(least_frequent)

    answer = "".join(least_common_letter)
    print("For Part 2: The original message is '{}'".format(answer))
            

part1(strings)
part2(strings)