from sys import stdin

ip_addresses = []
hypernet_sequences = []

for line in stdin:
    splitted = line.replace("[", "]").split("]")

    temp_A = []
    temp_B = []
    cnt = 0
    while cnt < len(splitted):
        if cnt % 2 == 0:
            temp_B.append(splitted[cnt])
        else:
            temp_A.append(splitted[cnt])
        cnt += 1

    hypernet_sequences.append(temp_A)
    ip_addresses.append(temp_B)

def checker(string):
    return any(((c1 == c4) and (c2 == c3) and (c1 != c2)) for c1, c2, c3, c4 in zip(string, string[1:], string[2:], string[3:]))

def aba_bab(string):
    patterns = []
    for c1, c2, c3 in zip(string, string[1:], string[2:]):
        
        if c1 == c3 and c1 != c2:
            patterns.append(c2+c1+c2)
        
    if patterns:    
        return patterns
    else: 
        return None

def part1(ip_addresses, hypernet_sequences):
    counter = 0
    iterator = 0
    while iterator < len(ip_addresses):

        ip_boolean = []
        for i in ip_addresses[iterator]:
            c_ip = checker(i)
            ip_boolean.append(c_ip)
        
        hs_boolean = []
        for h in hypernet_sequences[iterator]:
            c_hs = checker(h)
            hs_boolean.append(c_hs)

        if any(ip_boolean) and not any(hs_boolean):
            counter += 1

        iterator += 1

    print("For Part 1: {} IPs in the puzzle input support TLS (Transport-Layer Snooping).".format(counter))
    return counter

def part2(ip_addresses, hypernet_sequences):
    counter = 0
    iterator = 0
    while iterator < len(ip_addresses):
        ip_patterns = []
        for i in ip_addresses[iterator]:
            c_ip = aba_bab(i)
            ip_patterns.append(c_ip)
        
        filtered = list(filter(lambda item: item is not None, ip_patterns))
        ip = sum(filtered, [])

        if ip:
            for h in hypernet_sequences[iterator]:
                h_checker = []
                for pattern in ip:
                    if pattern in h:
                        h_checker.append(True)
                        
                if any(h_checker):
                    counter += 1

        iterator += 1

    print("For Part 2: {} IPs in the puzzle input support SSL (Super-Secret Listening).".format(counter))
    return counter

part1(ip_addresses, hypernet_sequences)
part2(ip_addresses, hypernet_sequences)