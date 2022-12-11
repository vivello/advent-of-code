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

# Part 2
# Draw screen output based on positioning of sprite relative to which pixels are being drawn
# RLEZFLGE

def screen(instructions):
    result = []
    cycle = 1
    x = [0,1,2]
    position = 0

    for command in instructions:
        if cycle >= 240:
            break
        to_add = '#' if position in x else '.'
        result.append(to_add)
        if position == 39:
            result.append('\n')
        cycle += 1
        position = (position + 1) % 40
        if command[0] == 'noop':
            continue
        else:
            to_add = '#' if position in x else '.'
            result.append(to_add)
            if position == 39:
                result.append('\n')
            cycle += 1
            position = (position + 1) % 40
            x[1] += int(command[1])
            x[0] = x[1] - 1
            x[2] = x[1] + 1
    if cycle == 240:
        if position in x:
            result.append('#')
        else:
            result.append('.')
    return ''.join(result)
                

def main(file_name):
    with open(file_name) as f:
        print(screen([x.strip().split() for x in f.readlines()]))


# check position relative to sprite, draw # if position in sprite else .
# if end of a line, insert newline
# advance 1 clock cycle
# cycle and position advances without sprite changing
# if noop, proceed to next command
# if addx, check if at end of line and insert newline if necessary
#     advance 1 clock cycle & posiition and update x value / sprite 
