from sys import stdin

for line in stdin:
    polymer = list(line)

def part1(polymer):
    pattern_found = True
    while pattern_found:
        pattern = polymer
        
        for index,(p1, p2) in enumerate(zip(pattern, pattern[1:])):
            if (p1.lower() == p2 or p1.upper() == p2) and p1 != p2:
                pattern_found = True
                del pattern[index:index+2]
                break
            else:
                pattern_found = False

        if not pattern_found:
            break

    
    return len(pattern)

print("For Part 1: There are {} units remaining after fully reacting the polymer.".format(part1(polymer)))

def part2(polymer):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    length_list = list()

    for a in alphabet:
        letters_to_remove = [a, a.lower()]
        new_list = [x for x in polymer if x not in letters_to_remove]
        current_length = part1(new_list)
        length_list.append(current_length)

    shortest_polymer = min(length_list)
    print("For Part 2: The length of the shortest polymer that can be produced is {}.".format(shortest_polymer))
    
part2(polymer)