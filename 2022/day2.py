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

def main(file_name):
    with open(file_name,"r") as f:
        tourney = [x.strip().split() for x in f.readlines()]

        return rpc(tourney)
