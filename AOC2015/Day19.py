import os, time, re
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC19_1.txt", "r").read().splitlines()

d = {} #Transformations
rd = {} #Reverse Transformations
od = {} #Ordered Transformations
odl = []
m = "" #Molecule

for i in input:
    j = i.split()
    if len(j) == 3:
        if j[0] not in d:
            d[j[0]] = [j[2]]
        else:
            d[j[0]].append(j[2])
        rd[j[2]] = [j[0]]
        odl.append([j[2],j[0],len(j[2])])
    elif len(j) == 1:
        m = i

odl = sorted(odl, key=lambda k: k[2], reverse=True)
for i in odl:
    od[i[0]] = i[1]

#for k,v in od.items():
#    print(k,v)
#print(m)

def findParents(inM):
    distM = [] #Distinct Molecules
    for k,v in rd.items():
        indices = ([(i.start(), i.end()) for i in re.finditer(k, inM)])
        for i in indices:
            mol = inM[0:i[0]] + v[0] + inM[i[1]:]
            if mol not in distM: distM.append(mol)
    return sorted(distM) #Speeds up DFS

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

#Mem overload
def Part2BottomUp():
    now = time.time()
    count = 0
    mols = ["e"]
    while m not in mols:
        count +=1
        newMols = []
        for i in mols:
            newMols.extend(findChildren(i))
        mols = newMols
        print(len(m), len(mols[0]))
    print("Part 2: ", count)
    print("Time taken: " + str(time.time() - now))

#Mem overload
def Part2TopDown():
    now = time.time()
    count = 0
    mols = [m]
    while "e" not in mols:
        count +=1
        newMols = []
        for i in mols:
            newMols.extend(findParents(i))
        mols = newMols
        print(len(m), len(mols[0]), len(mols))
    print("Part 2: ", count)
    print("Time taken: " + str(time.time() - now))

#Stalls
#Greedy reduction method. Reduce by longest first
def Part2A():
    now = time.time()
    count = 0
    global m
    print(m)
    while len(m) != 1:
        for k,v in od.items():
            indices = ([(i.start(), i.end()) for i in re.finditer(k, m)])
            if len(indices) != 0:
                for i in reversed(indices):
                    m = m[0:i[0]] + v[0] + m[i[1]:]
                count += len(indices)
                break
        print(m)
    print("Part 2: ", count)
    print("Time taken: " + str(time.time() - now))

#Inspied by:
#https://www.reddit.com/r/adventofcode/comments/3z6cyy/day_19_python_day_19_solution_in_python/
#Greedy DFS
def Part2():
    now = time.time()
    count = 0
    frontier = [(m, 0)]
    while frontier and not count:  # Terminate as soon as we find a path.
        curr, dist = frontier.pop()
        for neighbour in findParents(curr):
            frontier.append((neighbour, dist + 1))
            if neighbour == "e":
                count = dist + 1
    print("Part 2: ", count)
    print("Time taken: " + str(time.time() - now))

Part1()
Part2()
