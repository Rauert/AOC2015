import os, time
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC19_1.txt", "r").read().splitlines()

d = {} #Transformations
m = "" #Molecule

for i in input:
    j = i.split()
    if len(j) == 3:
        if j[0] not in d:
            d[j[0]] = [j[2]]
        else:
            d[j[0]].append(j[2])
    elif len(j) == 1:
        m = i

#for k,v in d.items():
#    print(k,v)
#print(m)

def Part1():
    now = time.time()
    distM = [] #Distinct Molecules
    count = 0
    for k in d.keys():
        count += m.count(k) * len(d[k])
    print("Time taken: ", count)

def Part2():
    now = time.time()
    
    print("Time taken: ")

Part1()
Part2()
