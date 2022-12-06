# Part 1
# Where is start of packet?
# 1109 (set len(packet_start) == 3)

# Part 2
# Where is start of message?
# 3965 (set len(packet_start) == 13)


def find_start(signal):
    packet_start = []

    for i,c in enumerate(signal):
        if c in packet_start:
            if c == packet_start[-1]:
                packet_start = [c]
            else:
                new_start = packet_start.index(c) + 1
                packet_start = packet_start[new_start:]
                packet_start.append(c)
        else:
            if len(packet_start) == 13:
                return i + 1
            else:
                packet_start.append(c)        

def main(file_name):
    with open(file_name) as f:
        stream = f.readlines()

        return find_start(stream[0].strip())
