import os, re
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC07_1.txt", "r").read().splitlines()
#input = open(fileDir+"\Test\AOC07_1.txt", "r").read().splitlines()
d = {}

def setup():
    for ii in input:
        jj = re.split("\s->\s|\s",ii)
        d[jj[len(jj)-1]]=jj[0:-1]
    #print(d)

def evaluate(i):
    #print(i)
    if len(i) == 1:
        if str.isdigit(i[0]) == True:
            return int(i[0])
        else:
            evaluate(d[i[0]])
    elif len(i) == 2:
        num = str(format(evaluate(d[i[1]]),"b"))
        for p in range(16-len(num)):
            num = "0" + num
        #print(evaluate(d[i[1]]))
        #print(num)
        comp = ""
        for c in num:
            if c == "1":
                comp += "0"
            else:
                comp += "1"
        #print(comp, len(comp))
        return int(comp,2)
    else:
        a,b = 0,0
        if str.isdigit(i[0]) == True:
            a = int(i[0])
        else:
            a = evaluate(d[i[0]])
        if str.isdigit(i[2]) == True:
            b = int(i[2])
        else:
            b = evaluate(d[i[2]])
        if i[1] == "AND": return a & b
        elif i[1] == "OR": return a | b
        elif i[1] == "RSHIFT": return a >> b
        else: return a << b

def canEvaluate(k):
    i = d[k]
    #print(i)
    can = False
    if len(i) == 1:
        if isinstance(i[0],int) == True:
            d[k] = i[0]
            can = True
        elif str.isdigit(i[0]) == True:
            d[k] = int(i[0])
            can = True
    elif len(i) == 2:
        if isinstance(i[1],int) == True:
            num = str(format(i[1],"b"))
            for p in range(16-len(num)):
                num = "0" + num
            comp = ""
            for c in num:
                if c == "1":
                    comp += "0"
                else:
                    comp += "1"
            d[k] = int(comp,2)
            can = True
    else:
        a,b = -1,-1
        if isinstance(i[0],int) == True:
            a = i[0]
        elif str.isdigit(i[0]) == True:
            a = int(i[0])
        if isinstance(i[2],int) == True:
            b = i[2]
        elif str.isdigit(i[2]) == True:
            b = int(i[2])
        if a != -1 and b != -1:
            if i[1] == "AND": d[k] = a & b
            elif i[1] == "OR": d[k] = a | b
            elif i[1] == "RSHIFT": d[k] = a >> b
            else: d[k] = a << b
            can = True
    return can

def run():
    seen = []
    while len(seen) != len(d):
        #print(len(seen), len(d))
        #print(d)
        #print(seen)
        for k,v in d.items():
            if k not in seen and canEvaluate(k) == True:
                seen.append(k)
                for kk,vv in d.items():
                    if k != kk:
                        if kk not in seen and k in vv:
                            #print(d[kk])
                            d[kk] = [x if x != k else d[k] for x in d[kk]]
                            #print(d[kk])

    #print("Part 1:", d["a"])
    #print("Part 1:", evaluate(d["f"]))
    #for k in d.keys():
        #print(k, d[k])
        #print(k, evaluate(d[k]))

def Part1():
    setup()
    run()
    print("Part 1:", d["a"])

def Part2():
    newB = d["a"]
    setup()
    d["b"] = [newB]
    run()
    print("Part 2:", d["a"])


Part1()
Part2()
