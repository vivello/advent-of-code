# Part 1
# Find crate at top of each stack
# MQSHJMWNH

def top_crate(crate_stuff):
    stacks = {}
    for i in range(1,10):
        stacks[i] = []

    for i, row in enumerate(crate_stuff):
        if "[" in row:
            for i in range(9):
                stack_place = i * 4 + 1
                if row[stack_place] != ' ':
                    stacks[i + 1].insert(0,row[stack_place])
        elif row[0] == 'm':
            step1 = row.strip().strip('move ').split()
            move = [int(step1[0]),int(step1[2]),int(step1[4])]
            for i in range(move[0]):
                to_move = stacks[move[1]].pop()
                stacks[move[2]].append(to_move)

    crate_list = []
    for i in range(1,10):
        crate_list.append(stacks[i][-1])
    return ''.join(crate_list)

# Part 2
# Can now move multiple crates at once
# LLWJRBHVZ

def moar_crate(crate_stuff):
    stacks = {}
    for i in range(1,10):
        stacks[i] = []

    for i, row in enumerate(crate_stuff):
        if "[" in row:
            for i in range(9):
                stack_place = i * 4 + 1
                if row[stack_place] != ' ':
                    stacks[i + 1].insert(0,row[stack_place])
        elif row[0] == 'm':
            step1 = row.strip().strip('move ').split()
            move = [int(step1[0]),int(step1[2]),int(step1[4])]
            to_move = stacks[move[1]][-move[0]:]
            for crate in to_move:
                stacks[move[2]].append(crate)
            stacks[move[1]] = stacks[move[1]][:-move[0]]

    crate_list = []
    for i in range(1,10):
        crate_list.append(stacks[i][-1])
    return ''.join(crate_list)


def main(file_name):
    with open(file_name) as f:
        return moar_crate(f.readlines())
    
            
