from sys import stdin
passphrase = list()

for line in stdin:
    series_words = line.split()
    passphrase.append(series_words)

def part1(passphrase):
    valid_counter = 0
    for p in passphrase:
        checker = set()
        for word in p:
            checker.add(word)

        if len(checker) == len(p):
            valid_counter += 1

    print("For Part 1: There are {} valid passphrases.".format(valid_counter))

def part2(passphrase):
    valid_counter = 0
    for p in passphrase:
        checker = set()
        for word in p:
            sorted_letters = sorted(word)
            new_word = "".join(sorted_letters)
            checker.add(new_word)

        if len(checker) == len(p):
            valid_counter += 1

    print("For Part 2: There are {} valid passphrases.".format(valid_counter))

part1(passphrase)
part2(passphrase)