import os, time, re
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
input = open(fileDir+"\Inputs\AOC23_1.txt", "r").read()

program = []

input = input.replace("+","")
input = input.replace(",","")
input = input.splitlines()

for i in input:
    ins = i.split()
    if ins[0] in ["jio","jie"]:
        program.append([ins[0], ins[1], int(ins[2])])
    elif ins[0] == "jmp":
        program.append([ins[0], int(ins[1])])
    else:
        program.append(ins)

#for i in program:
#    print(i)

def run(aVal):
    r = {"a": aVal,"b": 0}
    ip = 0
    while ip < len(program):
        ins = program[ip]
        if ins[0] == "hlf":
            r[ins[1]] = int(r[ins[1]] / 2)
            ip+=1
        elif ins[0] == "tpl":
            r[ins[1]] = r[ins[1]] * 3
            ip+=1
        elif ins[0] == "inc":
            r[ins[1]] += 1
            ip+=1
        elif ins[0] == "jmp":
            ip += ins[1]
        elif ins[0] == "jie":
            if r[ins[1]] % 2 == 0:
                ip += ins[2]
            else:
                ip+=1
        elif ins[0] == "jio":
            if r[ins[1]] == 1:
                ip += ins[2]
            else:
                ip+=1

    return r["b"]

now = time.time()
print("Part 1:", run(0))
print("Part 2:", run(1))
print("Time taken: " + str(time.time() - now))