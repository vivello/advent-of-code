'''
For example:

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53).
Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers!
That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).

    Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
    Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
    Card 4 has one winning number (84), so it is worth 1 point.
    Card 5 has no winning numbers, so it is worth no points.
    Card 6 has no winning numbers, so it is worth no points.

So, in this example, the Elf's pile of scratchcards is worth 13 points.

Take a seat in the large pile of colorful cards. How many points are they worth in total?
'''

# Part 1 = 22897

def card_value(winning,card):
    win_count = 0
    for num in card:
        if num in winning:
            win_count += 1
    if win_count == 0:
        return 0
    else:
        return 2 ** (win_count - 1)

def calc_cards(file_name):
    score = 0

    with open(file_name,"r") as f:
        line = f.readline()

        while line:
            sep = line.split("|")
            cv = card_value(sep[0].split(),sep[1].split())
            score += cv
            line = f.readline()

    return score

# Part 2 = 5095824

def card_wins(winning,card):
    win_count = 0

    for num in card:
        if num in winning:
            win_count += 1
            
    return win_count


def copy_cards(file_name):
    wins = {}
    c_index = 1
    
    with open(file_name,"r") as f:
        line = f.readline()

        while line:
            sep = line.split("|")
            w = card_wins(sep[0].split(),sep[1].split())
            wins[c_index] = w
            c_index += 1
            line = f.readline()

        copies = {k:1 for k in wins}

        for k,v in wins.items():
            if v == 0:
                continue
            else:
                for i in range(k+1,k+v+1):
                    copies[i] += copies[k]

        return sum(copies.values())
            
            
