import os, time, itertools
from functools import reduce
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC24_1.txt", "r").read().splitlines()

input = list(map(int,input))

#Find every combination until one equals the group size.
#NOTE: Does not consider if the remaining presents split evenly into 2 groups of equal size. Works for input, but an incomplete solution.
def run(groupSize):
    now = time.time()
    for i in range(3, len(input)-6):
        comb = itertools.combinations(input,i)
        for c in comb:
            if sum(c) == groupSize:
                return(c, reduce(lambda x, y: x*y, c))
    
    print("Time taken: " + str(time.time() - now))

print("Part 1:",run(int(sum(input)/3)))
print("Part 2:",run(int(sum(input)/4)))