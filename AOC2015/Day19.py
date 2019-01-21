import os, time, re
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

def findChildren(inM):
    distM = [] #Distinct Molecules
    for k,v in d.items():
        indices = ([(i.start(), i.end()) for i in re.finditer(k, inM)])
        for i in indices:
            for j in v:
                mol = inM[0:i[0]] + j + inM[i[1]:]
                if mol not in distM: distM.append(mol)
    return distM

def Part1():
    now = time.time()
    print("Part 1: ", len(findChildren(m)))
    print("Time taken: " + str(time.time() - now))

def Part2():
    now = time.time()

    print("Part 2: ")
    print("Time taken: " + str(time.time() - now))

Part1()
Part2()
