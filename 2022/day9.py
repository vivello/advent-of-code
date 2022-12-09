short_test = ['R 4','U 4','L 3','D 1','R 4','D 1','L 5','R 2']
long_test = ['R 5','U 8','L 8','D 3','R 17','D 10','L 25','U 20']

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

# Part 2
# Model rope now with 10 knots, how many positions does the new tail (9) visit?
# 2458

def shift_knot(head,tail):
    if touching(head,tail):
        return False
    elif head[0] == tail[0]:
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
    elif head[1] == tail[1]:
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1
    elif head[0] > tail[0]:
        if head[1] > tail[1]:
            tail[0] += 1
            tail[1] += 1
        else:
            tail[0] += 1
            tail[1] -= 1
    else:
        if head[1] > tail[1]:
            tail[0] -= 1
            tail[1] += 1
        else:
            tail[0] -= 1
            tail[1] -= 1
    return True
    
def long_rope(motions):
    coords = {(0,0)}
    knots = []
    for i in range(10):
        knots.append([0,0])
    for m in motions:
        direction, steps = m.strip().split()
        for i in range(int(steps)):
            for n,knot in enumerate(knots):
                if n == 0:
                    if direction == 'U':
                        knots[0][1] += 1
                    elif direction == 'D':
                        knots[0][1] -= 1
                    elif direction == 'R':
                        knots[0][0] += 1
                    else:
                        knots[0][0] -= 1
                    shift_knot(knots[0],knots[1])
                elif n <= 7:
                    shift_knot(knots[n],knots[n+1])
                elif n == 8:
                    if shift_knot(knots[8],knots[9]):
                        coords.add((knots[9][0],knots[9][1]))
            #print(knots)
    return len(coords)
    

def main(file_name):
    with open(file_name) as f:
        return long_rope(f.readlines())
                    
