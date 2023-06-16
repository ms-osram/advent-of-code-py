from sys import stdin

expense_report = list()

for line in stdin:
    expense_report.append(int(line.strip()))

def part1(expense_report):
    input1 = None
    input2 = None
    for entry1 in expense_report:
        for entry2 in expense_report:
                if entry1 + entry2 == 2020:
                    input1 = entry1
                    input2 = entry2
                    answer = entry1 * entry2
                    break
    print("For Part 1: The two entries that sum to 2020 are {} and {}. When multiplied together, the result is {}.".format(input1, input2, answer))

def part2(expense_report):
    input1 = None
    input2 = None
    input3 = None
    for entry1 in expense_report:
        for entry2 in expense_report:
            for entry3 in expense_report:
                if entry1 + entry2 + entry3 == 2020:
                    input1 = entry1
                    input2 = entry2
                    input3 = entry3
                    answer = entry1 * entry2 * entry3
                    break
    print("For Part 2: The three entries that sum to 2020 are {}, {}, and {}. When multiplied together, the result is {}.".format(input1, input2, input3, answer))

part1(expense_report)
part2(expense_report)
