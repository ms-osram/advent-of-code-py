"""
lists = [["D", "T", "W", "N", "L"], ["H", "P", "C"], ["J", "M", "G", "D", "N", "H", "P", "W"], ["L", "Q", "T", "N", "S", "W", "C"], ["N", "C", "H", "P"], ["B", "Q", "W", "M", "D", "N", "H", "T"], ["L", "S", "G", "J", "R", "B", "M"], ["T", "R", "B", "V", "G", "W", "N", "Z"], ["L", "P", "N", "D", "G", "W"]]

"""
lists = [['N', 'Z'], ['D', 'C', 'M'], ['P']]


for lst in lists:
    lst.reverse()

print("Original List:", lists)


instructions = []
message = []

while True:
    inp = ""
    try: inp = input()

    except EOFError:
        break

    x = inp.replace("move ","").replace(" from ", " ").replace(" to ", " ")
    xSplit = x.split(" ")
    instructions.append(xSplit)

steps = []
for num in instructions:
    step = []
    for n in num:
        step.append(int(n))
        
    steps.append(step)
    step = []



def day1(steps):
    for stp in steps:
        n = stp[0]
        x1 = stp[1]-1
        x2 = stp[2]-1

        for i in range(n):
            lists[x2].append(lists[x1].pop())

        print(lists)

def day2(steps):
    temp_list = []
    for stp in steps:
        n = -stp[0]
        x1 = stp[1]-1
        x2 = stp[2]-1
        
        print("n:", n, "x1: ", x1, "x2: ", x2)
        
        temp_list = [lists[x1][0:n]]
        temp_list.reverse()
        
        lists[x2].extend(temp_list)
        del lists[x1][n]
        

        
        
        print(lists)


day2(steps)


for m in range(len(lists)):
    message.append(lists[m][-1])

joinMessage = "".join(message)
print("The message is: ", joinMessage)
