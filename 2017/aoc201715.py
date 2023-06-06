from sys import stdin

gen_a = 0
gen_b = 0
factor_a = 16807
factor_b = 48271
to_mod = 2147483647


for line in stdin:
    split = line.replace(" starts with ", " ").split(" ")
        
    if split[1] == "A":
        gen_a = int(split[2])
    elif split[1] == "B":
        gen_b = int(split[2])


print("Generator A: {}, Generator B: {}".format(gen_a, gen_b))
def part1(gen_a,gen_b,factor_a,factor_b,to_mod):
    n = 0
    counter = 0
    while n < 40000000:
        gen_a = (gen_a * factor_a) % to_mod
        gen_b = (gen_b * factor_b) % to_mod
        checker_a = gen_a % (2**16)
        checker_b = gen_b % (2**16) 
        if checker_a == checker_b:
            counter += 1
        n += 1

    print("For Part 1: The Judge's final count is {}.".format(counter))
    return counter

def part2(gen_a,gen_b,factor_a,factor_b,to_mod):
    to_compare_a = []
    to_compare_b = []

    n = 0
    while n < 40000000:
        gen_a = (gen_a * factor_a) % to_mod
        gen_b = (gen_b * factor_b) % to_mod

        if gen_a % 4 == 0:
            to_compare_a.append(gen_a)

        if gen_b % 8 == 0:
            to_compare_b.append(gen_b)

        n += 1

    counter = 0 
    for A, B in zip(to_compare_a, to_compare_b):
        if A % (2**16) == B % (2**16):
            counter += 1


    print("For Part 2: The Judge's final count is {}.".format(counter))
    return counter

part1(gen_a,gen_b,factor_a,factor_b,to_mod)
part2(gen_a,gen_b,factor_a,factor_b,to_mod)