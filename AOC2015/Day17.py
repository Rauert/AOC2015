import time, itertools

d = [43,3,4,10,21,44,4,6,47,41,34,17,17,44,36,31,46,9,27,38] #Containers
c = 150 #Capacity
#d = [20, 15, 10, 5, 5]
#c = 25

def run():
    now = time.time()
    valid = []
    validLength = []
    for s in range(2,len(d)+1):
        p = itertools.combinations(d,s)
        for i in p:
            if sum(i) == c:
                valid.append(i)
                validLength.append(len(i))
    print("Part 1:", len(valid))
    mini = min(validLength)
    print("Part 2:", validLength.count(mini))
    print("Time taken: " + str(time.time() - now))

run()