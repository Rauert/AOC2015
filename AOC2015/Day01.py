def Day1_1(data):
    print("AOC 2015 Day 1_1 answer:", data.count("(") - data.count(")"))

def Day1_2(data):
    pos = 0
    ans = 0
    for i in range(len(data)):
        if data[i] == "(":
            pos += 1
        else:
            pos -= 1
        if pos == -1:
            ans = i+1
            break

    print("AOC 2015 Day 1_2 answer:",ans)

d = open(r"C:\Users\michelle\python\AOC2015\Inputs\AOC01_1.txt", "r").readlines()[0].rstrip()
Day1_1(d)
Day1_2(d)
