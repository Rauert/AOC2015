import time

def findFactors(num):
    f = []
    for i in range(1,num+1):
        if num % i == 0: f.append(i)
    return f

#https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
from math import sqrt
from functools import reduce

def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

def Part1():
    now = time.time()
    notFound = True
    house = 1
    while notFound:
        #if sum([x*10 for x in factors(house)]) >= 34000000:
        if sum(factors(house)) >= 3400000:
            notFound = False
        else:
            house += 1

    print("Part 1:", house)
    print("Time taken: " + str(time.time() - now))

def Part2():
    now = time.time()
    notFound = True
    house = 1
    while notFound:
        f = factors(house)
        sumP = 0
        for i in f:
            if house / i <= 50.0:
                sumP += i*11
        if sumP >= 34000000:
            notFound = False
        else:
            house += 1

    print("Part 2:", house)
    print("Time taken: " + str(time.time() - now))

Part1()
Part2()
