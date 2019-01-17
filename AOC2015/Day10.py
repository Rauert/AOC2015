def run(input, length):
    for _ in range(length):
        newInput = ""
        times = 1
        next = input[0]
        for i in range(len(input)):
            if i == len(input)-1:
                newInput += str(times)+next
            elif next == input[i+1]:
                times += 1
            else:
                newInput += str(times)+next
                times = 1
                next = input[i+1]
        input = newInput
        #print(input)
    return len(input)

print("Part 1:", run("1113122113", 40))
print("Part 2:", run("1113122113", 50))
