import os, re
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC12_1.txt", "r").read()

def count():
    nums = []
    num = ""
    wasDig = False
    for i in input:
        if i.isdigit() or i == "-":
            num += i
            wasDig = True
        elif wasDig == True:
            nums.append(int(num))
            num = ""
            wasDig = False
    #print(nums)
    return sum(nums)

#determine if red lies within an array or object. For objects remove the entire object.
def remove():
    global input
    while input.find("red") != -1:
        inArray = False
        level = 0
        levelArr = 0
        i = input.find("red")
        while True:
            if input[i] == "{":
                if level == 0: break
                else: level -= 1
            elif input[i] == "}": level += 1
            elif input[i] == "[":
                if levelArr == 0:
                    inArray = True
                    break
                else: levelArr -= 1
            elif input[i] == "]": levelArr += 1
            i -= 1
        iStart = i
        i = input.find("red")
        if inArray == True:
            input = input[0:i] + input[i+1:] #Ensure this red doesn't get found again
        else:
            while True:
                if input[i] == "}":
                    if level == 0: break
                    else: level += 1
                elif input[i] == "{": level -= 1
                i += 1
            iEnd = i+1
            #print(input[iStart:iEnd], iStart, iEnd)
            input = input[0:iStart+1] + input[iEnd-1:]
            #print(input[0:iEnd])
            #print(len(input))
    return count()

print("Part 1:", count())
print("Part 2:", remove())
