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
