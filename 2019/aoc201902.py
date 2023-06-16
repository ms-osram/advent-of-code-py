from sys import stdin

intcode = list()

for line in stdin:
    integers = line.split(",")
    for i in integers:
        intcode.append(int(i))

intcode[1] = 12
intcode[2] = 2

class Interpreter:
    def __init__(code):
        self.code = code
    
    def execute(self):
        #do something here
        pass
    def on_read_1(self):
        pass 

def part1(intcode):
    for i in range(0, len(intcode), 4):
        values = intcode[i:i+4]
        
        opcode = intcode[i]
        input1 = intcode[intcode[i+1]]
        input2 = intcode[intcode[i+2]]
        address = intcode[i+3]

        print(values)
        if intcode[i] != 99:
            if intcode[i] == 1:
                operation = input1 + input2 
                print("{} + {} = {}".format(input1,input2, operation))
            elif intcode[i] == 2:
                operation = input1 * input2 
                print("{} * {} = {}".format(input1,input2, operation))
            
            intcode[address] = operation
        else:
            break
        
    print("For Part 1: The value left at position [0] after the program halts is {}.".format(intcode[0]))
    return intcode[0]

part1(intcode)