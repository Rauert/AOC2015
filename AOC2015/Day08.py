import os, re
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC08_1.txt", "r").read().splitlines()
#input = open(fileDir+"\Test\AOC08_1.txt", "r").read().splitlines()

#Decode
def Part1():
    totCount = 0
    for i in input:
        count = len(i)-2
        #print(i)
        j = 1
        while j < len(i)-2:
            #print(i[j:j+2],"\\\\","\\\"","\\x")
            if i[j:j+2] in ["\\\\","\\\""]:
                count -= 1
                j += 1
            elif i[j:j+2] == "\\x":
                count -= 3
                j += 3
            j+=1
        #print(len(i), count)
        totCount += len(i) - count
    #1892, too high
    print("Part 1:",totCount)

#Encode
def Part2():
    totCount = 0
    for i in input:
        count = len(i)+4
        #print(i)
        j = 1
        while j < len(i)-2:
            #print(i[j:j+2],"\\\\","\\\"","\\x")
            if i[j:j+2] in ["\\\\","\\\""]:
                count += 2
                j += 1
            elif i[j:j+2] == "\\x":
                count += 1
                j += 3
            j+=1
        #print(len(i), count)
        totCount += count - len(i)
    #1892, too high
    print("Part 2:",totCount)

Part1()
Part2()
