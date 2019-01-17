import os, re, time, itertools
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC13_1.txt", "r").read().splitlines()
#input = open(fileDir+"\Test\AOC13_1.txt", "r").read().splitlines()

d = {}
for i in input:
    j = i.split()
    if j[0] not in d: d[j[0]] = {}
    amount = int(j[3])
    if j[2] == "lose":
        amount = amount - amount - amount
    d[j[0]][j[10][0:-1]] = amount

for k,v in d.items():
    print(k,v)

def run():
    p = itertools.permutations(d.keys(),len(d))
    best = -1
    #worst = 0
    bestPath = ""
    #worstPath = ""
    
    for i in p:
        happiness = 0
        length = len(i)
        for j in range(length):
            happiness += d[i[j]][i[(j+1)%length]]
            happiness += d[i[j]][i[(j-1)%length]]
        if happiness > best or best == -1:
            best = happiness
            bestPath = i
        #if dist > worst:
            #worst = happiness
            #worstPath = i

    return (bestPath, best)
    #print("Part 2:", worstPath, worst)

print("Part 1:", run())
