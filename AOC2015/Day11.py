pw = list("abcdefgh")
pw = list("hxbxwxba")
alpha = "abcdefghijklmnopqrstuvwxyz"
legal = []
for i in range(24):
    legal.append(alpha[i:i+3])

def incrLetter(i):
    if i == "z": return "a"
    elif i in ["h","n","k"]: return chr(ord(i) + 2)
    else: return chr(ord(i) + 1)

def increment():
    finished = False
    i = len(pw)-1
    while finished == False:
        pw[i] = incrLetter(pw[i])
        if pw[i] == "a":
            if i == 0: i = len(pw)-1
            else: i -= 1
        else:
            finished = True
    #return pw

def pairCheck():
    pairs = []
    for i in range(len(pw)-1):
        if pw[i] == pw[i+1] and pw[i] not in pairs:
            pairs.append(pw[i])
    if len(pairs)>1: return True
    else: return False

def run():
    invalid = True
    results = []
    while len(results) < 2:
        increment()
        if any(substring in "".join(pw) for substring in legal) and pairCheck():
            results.append("".join(pw))
    print("Day 1:",results[0])
    print("Day 2:",results[1])

run()