# Part 1
# Calculate gamma and epsilon rate of submarine, then multiply for power consumption rate
# 4174964

from collections import defaultdict

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
    
                
                
