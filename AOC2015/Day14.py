import os
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC14_1.txt", "r").read().splitlines()
iterations = 2503
#input = open(fileDir+"\Test\AOC14_1.txt", "r").read().splitlines()
#iterations = 1000

r = [] #Reindeer

#Import
for i in input:
    j = i.split()
    r.append([j[0],int(j[3]),int(j[6]),int(j[13]),0,0])

#for v in r:
#    print(v)

def Part1():
    results = []
    for i in r:
        fullRounds = int(iterations / (i[2] + i[3]))
        total = fullRounds * i[1] * i[2]
        leftOver = iterations % (i[2] + i[3])
        if leftOver > i[2]: #Completed full flight session
            total += i[1] * i[2]
        else:
            total += leftOver * i[1]
        results.append([i[0],total])
        results = sorted(results, key=lambda k: [k[1]], reverse=True)
    print("Part 1:", results[0][0], results[0][1])

def Part2():
    for t in range(iterations):
        #Update distances
        for i in range(len(r)):
            posi = t % (r[i][2] + r[i][3])
            if posi < r[i][2]: r[i][4] += r[i][1]
        #Find leader/s
        sort = sorted(r, key=lambda k: [k[4]], reverse=True)
        maxi = sort[0][4]
        #Award points
        for i in range(len(r)):
            if maxi == r[i][4]: r[i][5] += 1
    sort = sorted(r, key=lambda k: [k[5]], reverse=True)
    print("Part 2:", sort[0][0], sort[0][5])
Part1()
Part2()