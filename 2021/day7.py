from collections import Counter

# Part 1
# Determine the horizontal position that the crabs can align to using the least fuel possible.
# How much fuel must they spend to align to that position?


def wrap(file_name):
    with open(file_name,"r") as f:
        crabs = [int(x) for x in f.readline().strip().split(",")]
    return opt_fuel(crabs)

def calc_fuel(h_count, target):
    fuel = 0
    for x,v in h_count.items():
        fuel += abs(x - target) * v
    return fuel

def opt_fuel(c_list):
    hor_count = Counter(c_list)

    min_fuel = calc_fuel(hor_count, min(hor_count.keys()))
    for i in range(min(hor_count.keys()) + 1,max(hor_count.keys()) + 1):
        min_fuel = min(min_fuel, calc_fuel(hor_count, i))

    return min_fuel
        
