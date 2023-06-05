from sys import stdin
from collections import Counter

strings = []
temp = []
values = []
checksum = []
encrypted = []
decrypted = []
alphabet = " abcdefghijklmnopqrstuvwxyz"

for line in stdin:
    split = line.split("-")
    temp.append(split[-1])
    split.pop()
    encrypted.append(split)
    strings.append("".join(split))

for t in temp:
    c = t.replace("]", "").split("[")
    checksum.append(c[1].strip())
    values.append(int(c[0]))

sum_ID = 0
for s, v, c in zip(strings, values, checksum):
    validity = True

    counter = Counter(s)
    commons = (counter.most_common(len(s)))
    sorted_commons = sorted(commons, key=lambda e: (-e[1], e[0]))

    for a, b in zip(sorted_commons, c):

        if a[0] != b:
            validity = False
            continue
    if validity == False:
        continue 

    sum_ID += v
    
    decrypt = []
    for letters in s:
        modulo = (alphabet.index(letters) + v) % 26
        letter = alphabet[modulo]
        decrypt.append(letter)

    decrypted.append(("".join(decrypt), v))

print("For Part 1: The sum of the Sector IDs of the real rooms is {}.".format(sum_ID))

for room in decrypted:
    
    if "northpoleobjectstorage" not in room:
        continue
    else:    
        print("For Part 2: North Pole objects are stored in sector ID {}.".format(room[1]))