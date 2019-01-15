import os, re
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC06_1.txt", "r").read().splitlines()
#input = open(fileDir+"\Test\AOC06_1.txt", "r").read().splitlines()
ls = []
d = []
#create d data object. 0 = off, 1 = on, 2 = toggle
for ii in input:
    jj = re.split("\s|,",ii)
    if len(jj) == 7:
        o = 0
        if jj[1] == "on": o = 1
        d.append([o,int(jj[2]),int(jj[3]),int(jj[5]),int(jj[6])])
    else:
        d.append([2,int(jj[1]),int(jj[2]),int(jj[4]),int(jj[5])])

def Part1():
    ls = [[0] * 1000 for i in range(1000)]
    count = 0
    for i in d:
        for y in range(i[2], i[4]+1):
            for x in range(i[1], i[3]+1):
                if i[0] == 2:
                    ls[y][x] = ls[y][x] ^ 1
                else:
                    ls[y][x] = i[0]
    for j in ls:
        count += sum(j)
    print("Part 1:",count)

def Part2():
    count = 0
    ls = [[0] * 1000 for i in range(1000)]
    for i in d:
        for y in range(i[2], i[4]+1):
            for x in range(i[1], i[3]+1):
                if i[0] == 0:
                    if ls[y][x] >= 1:
                        ls[y][x] -= 1
                else:
                    ls[y][x] += i[0]
    for j in ls:
        count += sum(j)
    print("Part 2:", count)

Part1()
Part2()
