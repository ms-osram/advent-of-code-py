from sys import stdin
from itertools import permutations

spreadsheet = list()
for line in stdin:
    row = line.split()
    spreadsheet_row = []
    for item in row:
        spreadsheet_row.append(int(item))
    spreadsheet.append(spreadsheet_row)
    spreadsheet_row = []

def part1(spreadsheet):
    differences = []
    for values in spreadsheet:
        minimum_value = min(values)
        maximum_value = max(values)
        difference = maximum_value - minimum_value
        differences.append(difference)
             
    sum_value = sum(differences)
    print("For Part 1: The checksum for the spreadsheet is {}.".format(sum_value))

def part2(spreadsheet):
    quotients = []
    for i in spreadsheet:

        permu = permutations(i, 2)
        permu_list = list(permu)
        
        for value in permu_list:
        
            x = 0
            
            if value[0] % value[1] == 0:
                quotient = value[0] // value[1]
                quotients.append(quotient)
                break
        
    sum_value = sum(quotients)
    print("For Part 2: The sum of each row's result is {}.".format(sum_value))

part1(spreadsheet)
part2(spreadsheet)