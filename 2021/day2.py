# Part 1
# Calculate the horizontal position and depth you would have after following the planned course
# 1507611

move_dict = {"forward": (0,1),
             "down": (1,1),
             "up": (1,-1)}

def mult_pos(file_name):
    position = [0,0]
    with open(file_name,"r") as f:
        move = f.readline().split()
        while move:
            index = move_dict[move[0]][0]
            multiplier = move_dict[move[0]][1]
            position[index] += (int(move[1]) * multiplier)
            move = f.readline().split()
    return position[0] * position[1]


# Part 2
# Calculate horizonal position and depth with new interpretation of planned course
# 1880593125

def new_course(file_name):
    position = {"horizontal": 0,
                "depth": 0,
                "aim": 0}
    with open(file_name,"r") as f:
        move = f.readline().split()
        while move:
            nyoom = int(move[1])
            if move[0] == "forward":
                position["horizontal"] += nyoom
                position["depth"] += (nyoom * position["aim"])
            elif move[0] == "down":
                position["aim"] += nyoom
            elif move[0] == "up":
                position["aim"] -= nyoom
            move = f.readline().split()
    return position["horizontal"] * position["depth"]
