# Part 1
# 7824

def comps(rucks):
    priors = 0

    for r in rucks:
        c_size = len(r) // 2
        front = r[:c_size]
        back = r[c_size:]

        for c in front:
            if c in back:
                if ord(c) >= 97:
                    priors += ord(c) - 96
                else:
                    priors += ord(c) - 38
                break

    return priors

# Part 2
# 2798

def badges(rucks):
    priors = 0

    for i in range(len(rucks) // 3):
        index = i * 3
        e1 = set(rucks[index])
        e2 = set(rucks[index + 1])
        e3 = set(rucks[index + 2])

        badge = e1.intersection(e2).intersection(e3).pop()

        if ord(badge) >= 97:
            priors += ord(badge) - 96
        else:
            priors += ord(badge) - 38

    return priors



def main(file_name):
    with open(file_name) as f:
        r = [x.strip() for x in f.readlines()]

    return badges(r)
