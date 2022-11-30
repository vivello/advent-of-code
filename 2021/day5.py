# Part 1
# Determine the number of points where at least two lines overlap
# for only horizontal and vertical lines
# 6841

def vent_cross(file_name):
    points = {}
    with open(file_name,"r") as f:
        for row in f.readlines():
            coords = row.strip().split(" -> ")
            c1 = [int(a) for a in coords[0].split(",")]
            c2 = [int(a) for a in coords[1].split(",")]
            if c1[0] == c2[0]:
                if c1[1] > c2[1]:
                    to_add = [(c1[0],y) for y in range(c2[1],c1[1] + 1)]
                else:
                    to_add = [(c1[0],y) for y in range(c1[1],c2[1] + 1)]
                for pos in to_add:
                    if pos in points:
                        points[pos] += 1
                    else:
                        points[pos] = 1
            elif c1[1] == c2[1]:
                if c1[0] > c2[0]:
                    to_add = [(x,c1[1]) for x in range(c2[0],c1[0] + 1)]
                else:
                    to_add = [(x,c1[1]) for x in range(c1[0],c2[0] + 1)]
                for pos in to_add:
                    if pos in points:
                        points[pos] += 1
                    else:
                        points[pos] = 1
                        
    return len(list(filter(lambda k: points[k] > 1, points.keys())))
                    
# Part 2
# Determine the number of points where at least two lines overlap
# for horizontal, vertical, and diagonal lines
# 19258

def crisscross(file_name):
    points = {}
    with open(file_name,"r") as f:
        for row in f.readlines():
            coords = row.strip().split(" -> ")
            c1 = [int(a) for a in coords[0].split(",")]
            c2 = [int(a) for a in coords[1].split(",")]
            if c1[0] == c2[0]:
                to_add = [(c1[0],y) for y in range(min(c1[1],c2[1]),max(c1[1],c2[1]) + 1)]
            elif c1[1] == c2[1]:
                to_add = [(x,c1[1]) for x in range(min(c1[0],c2[0]),max(c1[0],c2[0]) + 1)]
            else:
                inc_a = (c2[0] - c1[0]) // abs(c2[0] - c1[0])
                inc_b = (c2[1] - c1[1]) // abs(c2[1] - c1[1])
                to_add = [(c1[0],c1[1])]
                cur_coord = c1
                while cur_coord != c2:
                    cur_coord[0] += inc_a
                    cur_coord[1] += inc_b
                    to_add.append((cur_coord[0],cur_coord[1]))
            for pos in to_add:
                if pos in points:
                    points[pos] += 1
                else:
                    points[pos] = 1
            #print(to_add)
    return len(list(filter(lambda k: points[k] > 1, points.keys())))
                    
