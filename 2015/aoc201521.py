from sys import stdin

dimensions = []

# reads dimensions from standard input per line, splits using "x" as separator,
# converts them into int type, then append to a list of dimensions of the present
# appends the dimensions to list of dimensions
for line in stdin:
    string = line.strip().split("x")
    dim = []
    for item in string:
        num = int(item)
        dim.append(num)
    dimensions.append(dim)

total_area = 0
total_ribbon_length = 0

for dimension in dimensions:
    dimension.sort()
    a = dimension[0]
    b = dimension[1]
    c = dimension[2]
    
    # calculates the surface area of the present
    area = 2*a*b + 2*b*c + 2*c*a + a*b

    # calculates the required length of ribbon
    ribbon = 2*(a+b) + a*b*c 

    total_area += area
    total_ribbon_length += ribbon
    
print("The total area is: ", total_area)
print("The total ribbon length is: ", total_ribbon_length)