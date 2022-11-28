# Part 1
# Calculate gamma and epsilon rate of submarine, then multiply for power consumption rate
# 4174964

from collections import Counter

def power_consumption(file_name):
    with open(file_name, "r") as f:
        line = f.readline().strip()
        digits = [[0 for j in range(2)] for i in range(len(line))]
        while line:
            for i,bit in enumerate(line):
                digits[i][int(bit)] += 1
            line = f.readline().strip()

        gamma = []
        epsilon = []

        for a,b in digits:
            if a > b:
                gamma.append("0")
                epsilon.append("1")
            else:
                gamma.append("1")
                epsilon.append("0")

        gamma = int(''.join(gamma),2)
        epsilon= int(''.join(epsilon),2)

        return gamma * epsilon


# Part 2
# Calculate oxygen generator rating and CO2 scrubber rating to find life support rating
# 4474944

def diag_filter(dlist, default):
    index = 0
    guide = Counter(list(map(lambda x: x[0], dlist)))
    while len(dlist) > 1:
        if default == 1:
            if guide["0"] > guide["1"]:
                target = "0"
            else:
                target = "1"
        else:
            if guide["1"] < guide["0"]:
                target = "1"
            else:
                target = "0"
        dlist = list(filter(lambda x: x[index] == target, dlist))
        index += 1
        guide = Counter(list(map(lambda x: x[index], dlist)))
    return dlist[0]
                
def life_support(file_name):
    with open(file_name, "r") as f:
        diagnostics = f.readlines()
        oxygen = int(diag_filter(diagnostics, 1),2)
        co2 = int(diag_filter(diagnostics, 0),2)
    return oxygen * co2
        

    
