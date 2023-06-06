from sys import stdin
import hashlib


# reads the standard input and sets it as the value for `secret_key`
for line in stdin:
    secret_key = line

print("Secret Key: {}".format(secret_key))


# Both functions `part1` and `part2` iterates through increasing values of i, combines them with the secret key, 
# calculates the MD5 hash, and stops when a hash with the desired condition is found.
# For part 1, the desired condition is that the hash must start with at least five zeroes
# For part 2, the desired condition is that the hash must start with at least six zeroes


def part1(secret_key):
    i = 0

    while True:
        test_input = secret_key + str(i)
        
        resulting_hash = hashlib.md5(test_input.encode()).hexdigest()
        
        if resulting_hash[:5] == "00000":
            break

        i += 1

    print("Day 4 Part 1")
    print("Resulting hash: {}".format(resulting_hash))
    print("i: {}".format(i))
    return i 


def part2(secret_key):
    i = 0

    while True:
        test_input = secret_key + str(i)
        
        resulting_hash = hashlib.md5(test_input.encode()).hexdigest()
        
        if resulting_hash[:6] == "000000":
            break

        i += 1

    print("Day 4 Part 2")
    print("Resulting hash: {}".format(resulting_hash))
    print("i: {}".format(i))
    return i 

part1(secret_key)
part2(secret_key)