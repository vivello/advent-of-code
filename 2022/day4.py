def make_pretty(ep):
    return [[int(y) for  y in x.split('-')] for x in ep.strip().split(',')]

# Part 1
# Count wholly overlapping range pairs
# 571

def count_total_overlap(elf_pairs):
    count = 0
    for pair in elf_pairs:
        if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
            count += 1
        elif pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]:
            count += 1
    return count

# Part 2
# Count any overlapping range pairs
# 917

def count_overlap(elf_pairs):
    count = 0
    for pair in elf_pairs:
        if pair[0][0] <= pair[1][1] and pair[0][0] >= pair[1][0]:
            count += 1
        elif pair[1][0] <= pair[0][1] and pair[1][0] >= pair[0][0]:
            count += 1
    return count
        

def main(file_name):
    with open(file_name) as f:
        e_pairs = f.readlines()

        return count_overlap([make_pretty(x) for x in e_pairs])
        
