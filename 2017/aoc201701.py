from sys import stdin

sequence = list()

for line in stdin:
    for number in line:
        sequence.append(int(number))

def part1(sequence):
    sequence_size = len(sequence)
    captcha_numbers = list()
    captcha_solution = 0
    for x in range(sequence_size-1):
        if sequence[x] == sequence[x+1]:
            captcha_numbers.append(sequence[x])
            
    if sequence[0] == sequence[-1]:
        captcha_numbers.append(sequence[0])


    for n in captcha_numbers:
        captcha_solution += n
    
    print("For Part 1: The captcha solution is {}.".format(captcha_solution))
    return captcha_solution

def part2(sequence):
    sequence1 = sequence[:len(sequence)//2]
    sequence2 = sequence[len(sequence)//2:]
    captcha_solution = 0
    for a,b in zip(sequence1, sequence2):
        if a == b:
            captcha_solution += (2*a)
        else:
            continue
    print("For Part 2: The new captcha solution is {}.".format(captcha_solution))
    return captcha_solution

part1(sequence)
part2(sequence)

