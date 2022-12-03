# Part 1
# Calculate the total score according to strategy guide
# 12156

def rpc(rpc_sets):
    win = {"A": "Y",
           "B": "Z",
           "C": "X",
           "X": "B",
           "Y": "C",
           "Z": "A"}

    choice_points = {"X": 1,
                     "Y": 2,
                     "Z": 3}
    score = 0
    for game in rpc_sets:
        if game[1] == win[game[0]]:
            score += 6
        elif win[game[1]] == game[0]:
            score += 0
        else:
            score += 3
        score += choice_points[game[1]]

    return score

# Part 2
# Calculate total score according to strategy guide with updated meaning
# 10835

def rpc_strat(rpc_sets):
    win = {"A": ("Y","X","Z"),
           "B": ("Z","Y","X"),
           "C": ("X","Z","Y"),
           "Z": (0,6),
           "Y": (1,3),
           "X": (2,0)}

    choice_points = {"X": 1,
                     "Y": 2,
                     "Z": 3}
    score = 0

    for game in rpc_sets:
        score += win[game[1]][1]
        score += choice_points[win[game[0]][win[game[1]][0]]]

    return score

def main(file_name):
    with open(file_name,"r") as f:
        tourney = [x.strip().split() for x in f.readlines()]

        return rpc_strat(tourney)
