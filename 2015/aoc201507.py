from sys import stdin 

instructions = []
wires = {}

class SixteenBit:
    def __init__(self, num):
        array = '{0:016b}'.format(num)
        binary = list()
        for a in array:
            b = bool(int(a))
            binary.append(b)
        self.array = binary
        
        # above is the bitwise implementation for "0"
        # complete implementation so you can represent numbers from 0 to 65535
    
    def to_num(self):
        x = 0
        for (i, b) in enumerate(self.array[::-1]):
            if b:
                x += 2 **i
        return x

    def b_and(self, other):
        retval = SixteenBit(0)
        retval.array = []
        for a, b in zip(self.array, other.array):
            c = a & b
            retval.array.append(c)
        return retval
    
    def b_or(self, other):
        retval = SixteenBit(0)
        retval.array = []
        for a, b in zip(self.array, other.array):
            c = a | b
            retval.array.append(c)
        return retval
    
    def lshift(self, other): # `other` is also a SixteenBit, but treat it as a number using to_num()
        value = self.to_num() * (2 ** other.to_num())
        retval = SixteenBit(value)
        return retval
    
    def rshift(self, other): # `other` is also a SixteenBit, but treat it as a number using to_num()
        value = self.to_num() // (2 ** other.to_num())
        retval = SixteenBit(value)
        return retval
    
    def b_not(self):
        retval = SixteenBit(0)
        retval.array = []
        for a in self.array:
            c = not a
            retval.array.append(c)
        return retval

class Value:
    def __init__(self, string): # could be either num or variable
        try: 
            self.value = SixteenBit(int(string))
            self.discriminant = 0
        
        except ValueError:
            self.discriminant = 1
            self.value = string

    def get(self, wires):
        if self.discriminant == 0:
            return self.value
        else:
            return wires[self.value]

    def required_variable(self):
        if self.discriminant == 0:
            reqvar = None
        elif self.discriminant == 1:
            reqvar = self.value
        return reqvar

class Operation:
    def __init__(self, rope):
        if rope[0] == "NOT":
            self.discriminant = 0
            self.left = Value(rope[1])

        elif rope[1] == "AND":
            self.discriminant = 1
            self.left = Value(rope[0])
            self.right = Value(rope[2])

        elif rope[1] == "OR":
            self.discriminant = 2
            self.left = Value(rope[0])
            self.right = Value(rope[2])

        elif rope[1] == "LSHIFT":
            self.discriminant = 3
            self.left = Value(rope[0])
            self.right = Value(rope[2])

        elif rope[1] == "RSHIFT":
            self.discriminant = 4
            self.left = Value(rope[0])
            self.right = Value(rope[2])

        else:
            self.discriminant = 5
            self.left = Value(rope[0])

    def evaluate(self, wires):
        if self.discriminant == 0:
            return self.left.get(wires).b_not()
            
        elif self.discriminant == 1:
            return self.left.get(wires).b_and(self.right.get(wires))

        elif self.discriminant == 2:
            return self.left.get(wires).b_or(self.right.get(wires))

        elif self.discriminant == 3:
            return self.left.get(wires).lshift(self.right.get(wires))

        elif self.discriminant == 4:
            return self.left.get(wires).rshift(self.right.get(wires))

        elif self.discriminant == 5:
            return self.left.get(wires)

    def return_variables(self):
        req_vars = []
        if self.discriminant == 0 or self.discriminant == 5:
            if self.left.required_variable() != None:
                req_vars.append(self.left.required_variable())
            
        else:
            if self.left.required_variable() != None:
                req_vars.append(self.left.required_variable())
            if self.right.required_variable() != None:
                req_vars.append(self.right.required_variable())

        return req_vars

class Assignment:
    def __init__(self, rope):
        self.assigned_value = Operation(rope)
        self.destination = rope[-1]

    def evaluate_and_assign(self, wires):
        evaluated = self.assigned_value.evaluate(wires) # returns evaluated value based on operation
        wires[self.destination] = evaluated  #add evaluated value in wires dictionary

    def extract_required_variables(self):
        return self.assigned_value.return_variables()

    def extract_target_variable(self):
        return self.destination


ordered_list = []
dec_values = set()


def list_sorting(instructions):

    a = len(instructions)
    b = len(ordered_list)
    while a > b:
        for ins in instructions:
            if ins not in ordered_list:
                i = ins.split(" ")
                req_vars = Assignment(i).extract_required_variables()
                req_targ = Assignment(i).extract_target_variable()
                if req_targ == "b" and req_vars == False:
                    ordered_list.append("956 -> b")

                if req_vars:
                    if all(v in dec_values for v in req_vars):
                        ordered_list.append(ins)
                        dec_values.add(req_targ)
                    else:
                        continue
                else: 
                    ordered_list.append(ins)
                    dec_values.add(req_targ)
        a = len(instructions)
        b = len(ordered_list)

    return ordered_list

for line in stdin:
    instructions.append(line)


sorted_instructions = list_sorting(instructions)
print(sorted_instructions)

for instruction in sorted_instructions:
    Assignment(instruction.split(" ")).evaluate_and_assign(wires)

for (key, val) in wires.items():
    print(key, val.to_num())