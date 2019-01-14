input = open(r"C:\Users\Shell\source\repos\Rauert\AOC2015\AOC2015\Inputs\AOC05_1.txt", "r").read().splitlines()
v = ["a","e","i","o","u"]
db = ["aa","bb","cc","dd","ee","ff","gg","hh","ii","jj","kk","ll","mm","nn","oo","pp","qq","rr","ss","tt","uu","vv","ww","xx","yy","zz"]
nt = ["ab","cd","pq","xy"]
test = ["aaa","ugknbfddgicrmopn","jchzalrnumimnmhp","haegwjzuvuyypxyu","dvszwmarrgswjxmb"]

def Part1():
    count = 0
    for i in input:
        if sum(i.count(x) for x in v) >= 3 and any(x in i for x in db) and not any(x in i for x in nt):
            count += 1
    print("Part 1:",count)

def Part2():
    
    print("Part 2:")

Part1()
