from collections import Counter

def wrap(file_name):
    with open(file_name,"r") as f:
        crabs = [int(x) for x in f.readline().strip().split(",")]
    return crab_sub(crabs)


# Part 1
# Determine the horizontal position that the crabs can align to using the least fuel possible.
# How much fuel must they spend to align to that position?
# 331067

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
        

# Part 2
# Determine the horizontal position that the crabs can align to using the least fuel possible.
# How much fuel must they spend to align to that position?
# Now with updated crab engineering!
# 92881128

def crab_fuel(n):
    values = [0,1]
    for i in range(2,n + 1):
        values.append(values[i-1] - values[i-2] + 1 + values[i-1])
    return values

def calc_f(h_count, target, costs):
    fuel = 0
    for x,v in h_count.items():
        fuel += costs[abs(x - target)] * v
    return fuel

def crab_sub(c_list):
    hor_count = Counter(c_list)
    big = max(hor_count.keys())
    small = min(hor_count.keys())
    fuel_costs = crab_fuel(big - small)
    min_fuel = calc_f(hor_count, small, fuel_costs)
    for i in range(small + 1,big + 1):
        min_fuel = min(min_fuel, calc_f(hor_count, i, fuel_costs))

    return min_fuel
