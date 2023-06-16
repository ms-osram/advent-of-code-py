from sys import stdin

actions = list()
values = list()

for line in stdin:
    actions.append(line[0])
    values.append(int(line[1:]))

for action, value in zip(actions, values):
    x = 0
    y = 0
    degree_shift = 0
    

    coordinates = 
    print(action, value)

    if action == "N":
        y += value
    elif action == "S":
        y -= value
    elif action == "E":
        x += value
    elif action == "W":
        x += value
    elif action == "L":
    elif action == "R":
    elif action == "F":


