import time

def Part1():
    now = time.time()
    code = 20151125 #x=1, y=1
    x, yl = 1, 2
    while True:
        for y in range(yl,0,-1):
            code = (code * 252533) % 33554393
            #print(x, y, code)
            if y == 3010 and x == 3019:
                print("Part 1:", code)
                print("Time taken: " + str(time.time() - now))
                return
            x +=1
        x = 1
        yl += 1

Part1()