'''
The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category.

Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted.
Each line within a map contains three numbers: the destination range start, the source range start, and the range length.
'''

# Part 1 = 403695602

def convert(source,destinations):
    to_append = [source - d[1] + d[0] for d in destinations if (source >= d[1]) and (source < (d[1] + d[2]))]

    if len(to_append) == 0:
        return source
    else:
        return to_append[0]


def main(file_name):

    with open(file_name,"r") as f:
        line = f.readline()

        seeds = [int(n) for n in line.split(": ")[1].split()]
        #print(seeds)

        line = f.readline()

        while line:
            if line == "\n":
                line = f.readline() # go to title line
                line = f.readline() # skip title line
                collection = []
                while line and line != "\n":
                    collection.append([int(a) for a in line.split()])
                    line = f.readline()
                seeds = [convert(seed,collection) for seed in seeds]
                #print(collection)
                #print(seeds)

        return min(seeds)

# Part 2 -- ran out of memory

def make_seeds(initial):
    new_seeds = []

    for i in range(0,len(initial),2):
        for j in range(initial[i],initial[i]+initial[i+1]):
            new_seeds.append(j)

    return new_seeds

def new_main(file_name):

    with open(file_name,"r") as f:
        line = f.readline()

        seeds = [int(n) for n in line.split(": ")[1].split()]
        seeds = make_seeds(seeds)
        #print(seeds)

        line = f.readline()

        while line:
            if line == "\n":
                line = f.readline() # go to title line
                line = f.readline() # skip title line
                collection = []
                while line and line != "\n":
                    collection.append([int(a) for a in line.split()])
                    line = f.readline()
                seeds = [convert(seed,collection) for seed in seeds]
                #print(collection)
                #print(seeds)

        return min(seeds)
