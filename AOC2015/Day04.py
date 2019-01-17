from hashlib import md5
import time, math

s = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22, 5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20, 4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]
k = []
for i in range(64):
    k.append(hex(math.floor(4294967296 * abs(math.sin(i + 1)))))

key = "iwrupvqb"
#key = "abcdef"

#Unfinished MD5 function
def myMD5(input):
    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476
    length = str(format(len(input), "b"))
    while len(length) < 64: length = "0" + length
    bin = ''.join(format(ord(x), 'b') for x in input)
    bin += "1"
    while len(bin) % 512 != 448: bin += "0"
    bin += length
    print(len(bin))
    print(len(length))

def Part1():
    now = time.time()
    i = 0
    while True:
        if md5((key+str(i)).encode()).hexdigest()[0:5] == "00000":
            print("Part 1:",i)
            break
        else:
            i+=1

    print("Time taken: " + str(time.time() - now))

def Part2():
    now = time.time()
    i = 0
    while True:
        if md5((key+str(i)).encode()).hexdigest()[0:6] == "000000":
            print("Part 2:",i)
            break
        else:
            i+=1

    print("Time taken: " + str(time.time() - now))

Part1()
Part2()
