import time
bHP = 51
bD = 9
hHP = 50
hM = 500
hA = 0
spells = ["MM","Drain","Shield","Poison","Recharge"]
outcomes = []

def recurseRound(r):
    return r

def Part1():
    now = time.time()
    for i in spells:
        recurseRound()
    print("Time taken: " + str(time.time() - now))

Part1()