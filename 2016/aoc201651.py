from sys import stdin
import hashlib

puzzle_input = None

for line in stdin:
    puzzle_input = line
  
def part1(puzzle_input):
    i = 0
    password_values = list()

    while True:

        test_input = puzzle_input + str(i)
        resulting_hash = hashlib.md5(test_input.encode()).hexdigest()
        
        if resulting_hash[0:5] == "00000":

            password_input = resulting_hash[5]
            password_values.append(password_input)

            if len(password_values) == 8:
                break
            
        i += 1

    password = "".join(password_values)
    print("For Part 1: The password is {}.".format(password))
    return password

def part2(puzzle_input):
    i = 0
    password = dict()

    while True:

        test_input = puzzle_input + str(i)
        
        resulting_hash = hashlib.md5(test_input.encode()).hexdigest()
        
        if resulting_hash[0:5] == "00000":
            
            position = resulting_hash[5]
            password_input = resulting_hash[6]

            if position.isdigit() and position <= "7" and position not in password:
                password.update({position:password_input})

            if len(password) == 8:
                break
            
        i += 1

    sorted_keys = sorted(password.keys())
    sorted_password = dict()

    for key in sorted_keys:
        sorted_password[key] = password [key]


    pw_values = sorted_password.values()
    answer = "".join(pw_values)

    print("For Part 2: The password is: {}".format(answer))
    return answer

part1(puzzle_input)
part2(puzzle_input)