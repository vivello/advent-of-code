# Part 1
# Find sum of "interesting" signal strengths
# 17020

def sig_sum(instructions):
    result = 0
    cycle = 1
    x = 1

    for command in instructions:
        if cycle >= 220:
            break
        check_value = (cycle - 20) % 40
        if check_value == 0:
            result += (cycle * x)
        if command[0] == 'noop':
            cycle += 1
            continue
        elif check_value == 39 or check_value == -1:
            result += (cycle + 1) * x
        x += int(command[1])
        cycle += 2
    if ((cycle - 20) % 40) == 0:
        result += cycle * x
    return result

def main(file_name):
    with open(file_name) as f:
        return sig_sum([x.strip().split() for x in f.readlines()])
