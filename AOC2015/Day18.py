import os
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC18_1.txt", "r").read().splitlines()
#input = open(fileDir+"\Test\AOC06_1.txt", "r").read().splitlines()
ls = []
stuck = []

def setup():
    global ls, stuck
    ls = [[0] * 102 for i in range(102)]
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "#":
                ls[y+1][x+1] = 1
    stuck = [[1,1],[1,len(ls)-2],[len(ls)-2,1],[len(ls)-2,len(ls)-2]]

#ls = [[0,0,0,0,0,0,0,0],
      #[0,0,1,0,1,0,1,0],
      #[0,0,0,0,1,1,0,0],
      #[0,1,0,0,0,0,1,0],
      #[0,0,0,1,0,0,0,0],
      #[0,1,0,1,0,0,1,0],
      #[0,1,1,1,1,0,0,0],
      #[0,0,0,0,0,0,0,0]]

def printLS():
    for y in range(len(ls)):
            print(''.join(map(str, ls[y])))
    print()


def Part1():
    setup()
    for _ in range(100):
        global ls
        newLS = [[0] * 102 for i in range(102)]
        for y in range(1,len(ls)-1):
            for x in range(1,len(ls[y])-1):
                sumL = ls[y-1][x-1] + ls[y-1][x] + ls[y-1][x+1] + ls[y][x-1] + ls[y][x+1] + ls[y+1][x-1] + ls[y+1][x] + ls[y+1][x+1]
                if ls[y][x] == 1:
                    if sumL == 2 or sumL == 3: newLS[y][x] = 1
                else:
                    if sumL == 3: newLS[y][x] = 1
        ls = newLS
        #printLS()
    count = 0
    for j in ls:
        count += sum(j)
    print("Part 1:",count)

def Part2():
    global ls, stuck
    setup()
    for c in stuck: ls[c[1]][c[0]] = 1
    for _ in range(100):
        newLS = [[0] * 102 for i in range(102)]
        for c in stuck: newLS[c[1]][c[0]] = 1
        for y in range(1,len(ls)-1):
            for x in range(1,len(ls[y])-1):
                if [x,y] not in stuck:
                    sumL = ls[y-1][x-1] + ls[y-1][x] + ls[y-1][x+1] + ls[y][x-1] + ls[y][x+1] + ls[y+1][x-1] + ls[y+1][x] + ls[y+1][x+1]
                    if ls[y][x] == 1:
                        if sumL == 2 or sumL == 3: newLS[y][x] = 1
                    else:
                        if sumL == 3: newLS[y][x] = 1
        ls = newLS
        #printLS()
    count = 0
    for j in ls:
        count += sum(j)
    print("Part 2:",count)

#printLS()
Part1()
Part2()
