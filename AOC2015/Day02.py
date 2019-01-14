data = []

def Day2_1(d):
    total = 0
    for i in d:
        j = list(map(int,i.rstrip().split("x")))
        data.append(j)
        k = [j[0]*j[1],j[1]*j[2],j[0]*j[2]]
        total += k[0]*2 + k[1]*2+k[2]*2 + min(k)

    print("AOC 2015 Day 2_1 answer:",total)

def Day2_2():
    total = 0
    for i in data:
        print(i)
        j = i.sort()
        print(j)

    print("AOC 2015 Day 2_2 answer:",total)

d = open(r"C:\Users\michelle\python\AOC2015\Inputs\AOC02_1.txt", "r").readlines()
Day2_1(d)
Day2_2()
