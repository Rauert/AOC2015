dir = {"^":[0,1],"v":[0,-1],"<":[-1,0],">":[1,0]}
input = open(r"C:\Users\Shell\source\repos\Rauert\AOC2015\AOC2015\Inputs\AOC03_1.txt", "r").readlines()[0].rstrip()

def Day1_1():
    x,y = 0, 0
    d = {}
    d[(0,0)] = 1
    
    for i in input:
        dx,dy = dir[i]
        x += dx
        y += dy
        if (x,y) in d:
            d[(x,y)] += 1
        else:
            d[(x,y)] = 1

    print("AOC 2015 Day 3_1 answer:", len(d))

def Day1_2():
    x,y = 0,0
    xx,yy = 0,0
    d = {}
    d[(0,0)] = 2
    for i in range(0,len(input),2):
        dx,dy = dir[input[i]]
        x += dx
        y += dy
        if (x,y) in d:
            d[(x,y)] += 1
        else:
            d[(x,y)] = 1

        dx,dy = dir[input[i+1]]
        xx += dx
        yy += dy
        if (xx,yy) in d:
            d[(xx,yy)] += 1
        else:
            d[(xx,yy)] = 1
    print("AOC 2015 Day 3_2 answer:", len(d))

Day1_1()
Day1_2()
