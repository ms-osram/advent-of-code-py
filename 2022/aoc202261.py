from collections import deque

signal = []

while True:
    inp = ""
    try: inp = list(input())
    except EOFError:
        break
    
    signal.extend(inp)

print(signal)



def day1(signal):
# Initializing a queue
    q = deque()
      
    # Adding elements to a queue
    q.extend(signal[0:3])

    index = 3
    while index < len(signal): 
        q.append(signal[index])
        print(q)
        if len(q) == len(set(q)):
            print("First marker after character ", index+1)
            break
        else:
            q.popleft()
            index += 1

  
day1(signal)


def day2(signal):
# Initializing a queue
    q = deque()
      
    # Adding elements to a queue
    q.extend(signal[0:13])

    index = 13
    while index < len(signal): 
        q.append(signal[index])
        print(q)
        if len(q) == len(set(q)):
            print("First marker after character ", index+1)
            break
        else:
            q.popleft()
            index += 1

day2(signal)

