from sys import stdin
import itertools as it

# initializes a list named `strings`
strings = list()

# reads the standard input and appends it on the list named `strings`
for line in stdin:
    strings.append(line)


# `criteria1` function returns true if the string contains at least 3 vowels
def criteria1(string): 
    vowels = "aeiou"
    vowel_counter = 0
    for v in vowels:
        vowel_counter += string.count(v)
    return vowel_counter >= 3


# `criteria2` function returns true if the string contains at least 1 letter
# that appears twice in a row
def criteria2(string):
    return any(c1 == c2 for c1, c2 in zip(string, string[1:]))


# `criteria3` function returns true if the string contains any of the substrings
def criteria3(string):
    substring = ["ab", "cd", "pq", "xy"]
    for sub in substring:
        if sub in string:
            return True


# `criteria4` function returns true if the string contains a pair of two letters that 
# appears at least twice in the string without overlapping
def criteria4(string):
    for i in range(len(string) - 1):
        for j in range(i+2, len(string) - 1):
            if string[i:i+2] == string[j:j+2]:
                return True
    return False

# `criteria5` function returns true if the string contains at least one letter that
# repeats with exactly one letter between them
def criteria5(string):
    return any(c1 == c2 for c1, c2 in zip(string, string[2:]))


# returns the number of nice strings based on strings who pass `criteria1`, 
# `criteria2`, and `criteria3`
def part1(strings):
    nice_strings = 0

    for x in strings:
        if criteria1(x) == False:
            continue

        if criteria2(x) == False:
            continue

        if criteria3(x) == True:
            continue

        nice_strings += 1

     
    print("The number of nice strings for Day 1 is: {}". format(nice_strings))
    return nice_strings


# returns the number of nice strings based on strings who pass `criteria4` 
# and `criteria5`
def part2(strings):
    nice_strings = 0

    for x in strings:
        if criteria4(x) == False:
            continue
        
        if criteria5(x) == False:
            continue

        nice_strings += 1

     
    print("The number of nice strings for Day 2 is: {}". format(nice_strings))
    return nice_strings

part1(strings)
part2(strings)