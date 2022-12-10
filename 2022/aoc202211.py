import heapq

temp_list2 = []
temp_list1 = []

while True:
    inp = ""

    try:
        inp = input()
        temp_list1.append(int(inp))    
    
    except ValueError:
        temp_list2.append(temp_list1)
        temp_list1 = []
        
    except EOFError:
        break

calories = []

for n in temp_list2:
    calories.append(sum(n))

greatest_calories = heapq.nlargest(3, calories)    

print(sum(greatest_calories))
