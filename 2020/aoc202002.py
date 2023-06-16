from sys import stdin

policy1 = list()
policy2 = list()
password = list()

for line in stdin:
    entry = line.strip().split(' ')
    policy1.append(entry[0].split('-'))
    policy2.append(list(entry[1]))
    password.append(list(entry[2]))

for p in policy2:
    p.remove(':')

def part1(policy1, policy2, password):
    valid_passwords = 0
    for limits, criteria, password in zip(policy1, policy2, password):
        lower_limit = int(limits[0])
        upper_limit = int(limits[1])

        cnt_criteria = password.count(criteria[0])
        if lower_limit <= cnt_criteria <= upper_limit:
            valid_passwords += 1

    print("For Part 1: There are {} valid passwords.".format(valid_passwords))
    return valid_passwords

def part2(policy1, policy2, password):
    valid_passwords = 0
    for limits, criteria, password in zip(policy1, policy2, password):
        first_position = int(limits[0])-1
        second_position = int(limits[1])-1

        if (password[first_position] == criteria[0] or password[second_position] == criteria[0]) and not(password[first_position] == criteria[0] and password[second_position] == criteria[0]):
            valid_passwords += 1

    print("For Part 2: There are {} valid passwords.".format(valid_passwords))
    return valid_passwords

part1(policy1, policy2, password)
part2(policy1, policy2, password)