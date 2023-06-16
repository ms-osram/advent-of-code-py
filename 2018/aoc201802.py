from sys import stdin
from itertools import combinations

box_id = list()

for line in stdin:
    box_id.append(line.strip())

def part1(box_id):
    count_two = 0
    count_three = 0

    for id in box_id:
        
        sample_set = set()
        list_id = list(id)
        for item in list_id:
            sample_set.add(item)
        
        appears_twice = list()
        appears_thrice = list()
        
        for letter in sample_set:
            letter_count = list_id.count(letter)
            if letter_count == 2:
                appears_twice.append(True)
            else:
                appears_twice.append(False)

            if letter_count == 3:
                appears_thrice.append(True)
            else:
                appears_thrice.append(False)

        if any(appears_twice):
            count_two += 1
        if any(appears_thrice):
            count_three += 1

    checksum = count_two * count_three
    print("For Part 1: The checksum for the list of box IDs is {}.".format(checksum))
    return checksum


def part2(box_id):
    combi = combinations(box_id, 2)
    combinations_list = list(combi)

    character_differences = list() 
    for c1, c2 in combinations_list:
        char_diff = 0
        for a, b in zip(c1, c2):
            if a != b:
                char_diff += 1
            
        character_differences.append(char_diff)

    correct_box = min(character_differences)
    locate_correct_box = character_differences.index(correct_box)
    answer = combinations_list[locate_correct_box]

    common_characters = list()
    for a1, a2 in zip(answer[0], answer[1]):
        if a1 == a2:
            common_characters.append(a1)
    
    final_answer = ''.join(common_characters)
    print("For Part 2: The common letters between the two correct box IDs are {}.".format(final_answer))

part1(box_id)
part2(box_id)