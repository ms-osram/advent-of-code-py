from sys import stdin
import math

mass = list()

for line in stdin:
    mass.append(int(line.rstrip()))

def part1(mass):
    total_fuel = 0

    for m in mass:
        fuel_required = math.floor(m/3) - 2
        total_fuel += fuel_required

    print("For Part 1: The sum of the fuel requirements for all the modules is {}.".format(total_fuel))
    return total_fuel

def part2(mass):
    total_fuel_required = 0

    for m in mass:
        fuel_required = list()
        while True:
            fuel = math.floor(m/3) - 2     
            fuel_required.append(fuel)
            if fuel < 6:
                break
            else:
                m = fuel
        total_fuel_required += sum(fuel_required)

    print("For Part 2: The sum of the fuel requirements for all the modules is {}.".format(total_fuel_required))
    return total_fuel_required

part1(mass)
part2(mass)