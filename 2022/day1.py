# Part 1
# Find elf with most calories - how many calories are they carrying?
# 70369

def elf_cals(file_name):
    elves = {0:[]}
    index = 0
    most_cals = 0

    with open(file_name,"r") as f:
        line = f.readline()

        while line:
            if line == "\n":
                most_cals = max(most_cals, sum(elves[index]))
                index += 1
                elves[index] = []
            else:
                item = int(line.strip())
                elves[index].append(item)
            line = f.readline()

        return max(most_cals, sum(elves[index]))


# Part 2
# Find top 3 calorie carrying elves and return the sum
# 203002

def top3(file_name):
    elves = {0:0}
    index = 0

    with open(file_name,"r") as f:
        line = f.readline()

        while line:
            if line == "\n":
                index += 1
                elves[index] = 0
            else:
                item = int(line.strip())
                elves[index] += item
            line = f.readline()

    return sum(sorted(elves.values(),reverse=True)[0:3])
