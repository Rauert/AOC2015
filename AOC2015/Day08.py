import os, re
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC08_1.txt", "r").read().splitlines()

def Part1():
    count = 0
    for i in input:
        print(i)
        print(i.count("\\\\"))
        print(i.count("\\\""))
        print(i.count("\\x"))
        #consider overlapping
    print("Part 1:",count)

def Part2():

    print("Part 2:")

Part1()
Part2()
