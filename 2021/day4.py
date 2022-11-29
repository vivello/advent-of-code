# Part 1
# Find the winning bingo board and return the score
# 38913

def bingo(file_name):    

    def update(board_num, draw):
        for i,row in enumerate(boards[board_num]):
            if draw in row:
                (boards[board_num])[i][row.index(draw)] = "x"

    def check_board(board, draw_count, n):
        if draw_count >= 4:
            for row in board:
                if row.count("x") == 5:
                    return [n]
            flipped = [[row[x] for row in board] for x in range(5)]
            for row in flipped:
                if row.count("x") == 5:
                    return [n]
        return False

    with open(file_name, "r") as f:
        draws = f.readline().strip().split(",")
        boards = {0: []}

        f.readline()

        line = f.readline()

        board_num = 0

        while line:
            if line == "\n":
                board_num += 1
                boards[board_num] = []
            else:
                to_add = line.strip().split()
                boards[board_num].append(to_add)
            line = f.readline()
            
        for i,v in enumerate(draws):
            for b in boards:
                update(b, v)
                result = check_board(boards[b], i, b)
                if result:
                    result.append(v)
                    break
            if result:
                break

        winning_board = boards[result[0]]
        flat_board = [n for row in winning_board for n in row]
        unmarked = sum(map(int, filter(lambda x: x != "x", flat_board)))
        #print(result[1])
        #print(winning_board)
        return unmarked * int(result[1])
        
