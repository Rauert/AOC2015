import time, itertools

#Data
#Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
#Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
#Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
#Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8
d = {"Sprinkles":[2,0,-2,0,3],
     "Butterscotch":[0,5,-3,0,3],
     "Chocolate":[0,0,5,-1,8],
     "Candy":[0,-1,0,5,8]} #Ingredients

#Test data
#Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
#Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
#d = {"Butterscotch":[-1,-2,6,3,8],
#     "Cinnamon":[2,3,-2,-1,3]} #Ingredients

#Find all permutations and test each one.
def run():
    p = itertools.combinations_with_replacement(d.keys(),100)
    best = 0
    bestPath = ""
    bestCal = 0
    bestPathCal = ""

    for i in p:
        ca,du,fl,te,cal = 0,0,0,0,0
        path = []
        for k in d.keys():
            num = i.count(k)
            path.append([k, num])
            ca += num * d[k][0]
            du += num * d[k][1]
            fl += num * d[k][2]
            te += num * d[k][3]
            cal += num * d[k][4]
        if ca < 0: ca = 0
        if du < 0: du = 0
        if fl < 0: fl = 0
        if te < 0: te = 0
        total = ca*du*fl*te
        if total > best:
            best = total
            bestPath = path
        if cal == 500:
            if total > bestCal:
                bestCal = total
                bestPathCal = path
    print("Part 1:", bestPath, best)
    print("Part 2:", bestPathCal, bestCal)

run()