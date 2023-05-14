n = int(input())
rx = input().split('*')
for i in range(n):
    inp = input()
    if rx[0] == inp[0:len(rx[0])]:
        # inp = "#"*(len(rx[0])) + inp[len(inp) - len(rx[0]):]
        inp = "#"*(len(rx[0])) + inp[len(rx[0]):]
        # print(inp)
        if rx[1] == inp[len(inp) - len(rx[1]):]:
            print("DA")
        else:
            print("NE")
    else:
        print("NE")