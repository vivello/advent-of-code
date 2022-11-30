from collections import Counter

# Part 1
# How many lanterfish will there be after 80 days?
# 360761

def sim_fish(file_name, days):
    with open(file_name,"r") as f:
        start = [int(x) for x in f.readline().strip().split(",")]
        fish = Counter(start)

    for i in range(days):
        new = fish[0]
        for i in range(8):
            fish[i] = fish[i + 1]
        fish[8] = new
        fish[6] += new

    return sum(fish.values())
            
# Part 2
# How many lanterfish will there be after 256 days?
# 1632779838045
