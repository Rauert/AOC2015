input = open(r"C:\Users\Shell\source\repos\Rauert\AOC2015\AOC2015\Inputs\AOC05_1.txt", "r").read().splitlines()
v = ["a","e","i","o","u"]
db = ["aa","bb","cc","dd","ee","ff","gg","hh","ii","jj","kk","ll","mm","nn","oo","pp","qq","rr","ss","tt","uu","vv","ww","xx","yy","zz"]
nt = ["ab","cd","pq","xy"]
test = ["aaa","ugknbfddgicrmopn","jchzalrnumimnmhp","haegwjzuvuyypxyu","dvszwmarrgswjxmb","qjhvhtzxzqqjkmpb","xxyxx","uurcxstgmygtbstg","ieodomkazucvgmuy"]

def Part1():
    count = 0
    for i in input:
        if sum(i.count(x) for x in v) >= 3 and any(x in i for x in db) and not any(x in i for x in nt):
            count += 1
    print("Part 1:",count)

def Part2():
    count = 0
    for i in input:
        #print(i)
        pairRepeat = False
        singleRepeat = False
        if len(i) > 3:
            for c in range(len(i)-1):
                #print(i[c:c+2])
                if c <= 1:
                    s = i[c+2:]
                elif c >= len(i)-3:
                    s = i[0:c]
                else:
                    s = i[0:c] + " " + i[c+2:]
                #print(s)
                if i[c:c+2] in s: pairRepeat = True
                if c <= len(i)-3:
                    if i[c] == i[c+2]:
                        singleRepeat = True
                        #print(i)
                        #print(i[c:c+3])
            if pairRepeat == True and singleRepeat == True:
                count += 1
                #print(i)
    print("Part 2:", count)

Part1()
Part2()