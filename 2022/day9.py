# Part 1
# How many positions does the Tail visit?
# 6271

def touching(h,t):
    if h[0] == t[0]:
        return abs(h[1] - t[1]) <= 1
    elif h[1] == t[1]:
        return abs(h[0] - t[0]) <= 1
    else:
        return (abs(h[0] - t[0]) == 1) and (abs(h[1] - t[1]) == 1)
    

def close_tail(motions):
    coords = {(0,0)}
    head = [0,0]
    tail = [0,0]

    for m in motions:
        direction, steps = m.strip().split()
        if direction == 'U':
            for i in range(int(steps)):
                head[1] += 1
                if touching(head,tail):
                    continue
                elif head[0] == tail[0]:
                    tail[1] += 1
                elif head[0] > tail[0]:
                    tail[0] += 1
                    tail[1] += 1
                else:
                    tail[0] -= 1
                    tail[1] += 1
                coords.add((tail[0],tail[1]))
        elif direction == "D":
            for i in range(int(steps)):
                head[1] -= 1
                if touching(head,tail):
                    continue
                elif head[0] == tail[0]:
                    tail[1] -= 1
                elif head[0] > tail[0]:
                    tail[0] += 1
                    tail[1] -= 1
                else:
                    tail[0] -= 1
                    tail[1] -= 1
                coords.add((tail[0],tail[1]))
        elif direction == "R":
            for i in range(int(steps)):
                head[0] += 1
                if touching(head,tail):
                    continue
                elif head[1] == tail[1]:
                    tail[0] += 1
                elif head[1] > tail[1]:
                    tail[0] += 1
                    tail[1] += 1
                else:
                    tail[0] += 1
                    tail[1] -= 1
                coords.add((tail[0],tail[1]))
        elif direction == "L":
            for i in range(int(steps)):
                head[0] -= 1
                if touching(head,tail):
                    continue
                elif head[1] == tail[1]:
                    tail[0] -= 1
                elif head[1] > tail[1]:
                    tail[0] -= 1
                    tail[1] += 1
                else:
                    tail[0] -= 1
                    tail[1] -= 1
                coords.add((tail[0],tail[1]))
    return len(coords)

def main(file_name):
    with open(file_name) as f:
        return close_tail(f.readlines())
                    
