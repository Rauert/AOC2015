import os, time
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC16_1.txt", "r").read().splitlines()

d = {} #Sue data
for i in input:
    j = i.split()
    sue = int(j[1][0:-1])
    d[sue] = {}
    d[sue][j[2][0:-1]] = int(j[3][0:-1])
    d[sue][j[4][0:-1]] = int(j[5][0:-1])
    d[sue][j[6][0:-1]] = int(j[7])

#Ticker Tape
tt = [["children", 3],
    ["cats", 7],
    ["samoyeds", 2],
    ["pomeranians", 3],
    ["akitas", 0],
    ["vizslas", 0],
    ["goldfish", 5],
    ["trees", 3],
    ["cars", 2],
    ["perfumes", 1]]

#for k,v in d.items():
    #print(k,v)

def Part1():
    now = time.time()
    for k,v in d.items():
        num = 0
        for kk in tt:
            if kk[0] in v:
                if v[kk[0]] == kk[1]:
                    num += 1
        if num == 3:
            print("part 1: Sue", k)
            break
    print("Time taken: " + str(time.time() - now))

def Part2():
    now = time.time()
    for k,v in d.items():
        num = 0
        for kk in tt:
            if kk[0] in v:
                if kk[0] in ["cat", "tree"]:
                    if v[kk[0]] > kk[1]:
                        num += 1
                elif kk[0] in ["pomeranians", "goldfish"]:
                    if v[kk[0]] < kk[1]:
                        num += 1
                elif kk[0] in ["children","samoyeds","akitas","vizslas","cars","perfumes"]:
                    if v[kk[0]] == kk[1]:
                        num += 1
        if num == 3:
            print("part 2: Sue", k, v)
            break
    print("Time taken: " + str(time.time() - now))

Part1()
Part2()
