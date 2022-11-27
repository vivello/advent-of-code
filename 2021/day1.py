# part one
# count the number of times a depth measurement increases from the previous measurement
# 1228

def increasing_count(file_name):
    with open(file_name,"r") as f:
        count = 0
        prev_line = f.readline()
        line = f.readline()
        while line:
            if int(line) > int(prev_line):
                count += 1
            prev_line = line
            line = f.readline()
    return count


# part two
# count the number of times the sum of measurements in three-measurement sliding window
# increases from the previous sum, stop when you can't complete new windows
# 1257

#[2,3,4,5,6,3,2,4,1,3]
#[2]
#[5,3]
#[9,7,4]
#[9][12,9,5]

def sliding_count(file_name, window_size):
    count = 0
    windows = []
    w1 = -1
    w2 = -1
    with open(file_name,"r") as f:
        line = f.readline()
        while line:
            if len(windows) == window_size:
                w1 = w2
                w2 = windows.pop(0)
                if (w2 > w1) and (w1 != -1):
                    count += 1
            depth = int(line)
            for i,value in enumerate(windows):
                windows[i] += depth
            windows.append(depth)
            line = f.readline()
    if (len(windows) == 3) and windows[0] > w2:
        return count + 1
    else:
        return count
                
    
