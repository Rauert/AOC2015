import os, re, time, itertools
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC09_1.txt", "r").read().splitlines()
#input = open(fileDir+"\Test\AOC09_1.txt", "r").read().splitlines()

d = {}
for i in input:
    j = i.split()
    if j[0] not in d: d[j[0]] = {}
    if j[2] not in d: d[j[2]] = {}
    d[j[0]][j[2]] = int(j[4])
    d[j[2]][j[0]] = int(j[4])

#for k,v in d.items():
#    print(k,v)

def Part12():
    now = time.time()
    p = itertools.permutations(d.keys(),len(d))
    best = -1
    worst = 0
    bestPath = ""
    worstPath = ""
    for i in p:
        dist = 0
        for j in range(len(i)-1):
            dist += d[i[j]][i[j+1]]
        if dist < best or best == -1:
            best = dist
            bestPath = i
        if dist > worst:
            worst = dist
            worstPath = i

    print("Part 1:", bestPath, best)
    print("Part 2:", worstPath, worst)
    print("Time taken: " + str(time.time() - now))

Part12()
