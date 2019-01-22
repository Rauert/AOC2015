import time

weapons = [[8,4,0],
          [10,5,0],
          [25,6,0],
          [40,7,0],
          [74,8,0]]

armour = [[13,0,1],
         [31,0,2],
         [53,0,3],
         [75,0,4],
         [102,0,5]]

rings = [[25,1,0],
        [50,2,0],
        [100,3,0],
        [20,0,1],
        [40,0,2],
        [80,0,3]]

def Part12():
    now = time.time()
    #Find all combinations
    cb = []
    cb.extend(weapons) #Just a weapon
    for w in weapons:
        for a in armour:
            cb.append([w[0]+a[0],w[1],a[2]])  #Every combination of a weapon and armour
    cbwa = cb.copy()
    cbr = [] #1-2 ring combinations
    for r1 in rings:
        cbr.append(r1)
        for r2 in rings:
            if r1!= r2:
                newComb = [r1[0]+r2[0],r1[1]+r2[1],r1[2]+r2[2]]
                if newComb not in cbr: cbr.append(newComb)
    for wa in cbwa:
        for rs in cbr:
            newComb = [wa[0]+rs[0],wa[1]+rs[1],wa[2]+rs[2]]
            if newComb not in cb: cb.append(newComb)

    cb = sorted(cb, key=lambda k: k[0])
    #for c in cb:
    #    print(c)
    #print(len(cb))

    #Fight
    for c in cb:
        bD = 8 - c[2] #Boss Damage
        if bD < 1: bD = 1
        hD = c[1] - 2 #Hero Damage
        if hD < 1: hD = 1
        if hD >= bD:
            print("Part 1:",c[0])
            break

    for c in reversed(cb):
        bD = 8 - c[2] #Boss Damage
        if bD < 1: bD = 1
        hD = c[1] - 2 #Hero Damage
        if hD < 1: hD = 1
        if hD < bD:
            print("Part 2:",c[0])
            break
    print("Time taken: " + str(time.time() - now))

Part12()