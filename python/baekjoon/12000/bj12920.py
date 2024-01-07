n = int(input())
l = list(map(int, input().split()))
g = list(map(int, input().split()))
lst = zip(l, g)

C = [None for _ in range(101)]

for j in lst:
    tempArr = []
    for i in range(100):
        if C[i] != None and i + j[0] < 100:
            newIdx = i + j[0]
            newG = C[i] + j[1]
            tempArr.append((newIdx, newG))
    
    if C[j[0]] == None and j[0] < 100:
        C[j[0]] = j[1]

    for (newIdx, newG) in tempArr:
        if C[newIdx] == None:
            C[newIdx] = newG
        else:
            C[newIdx] = max(C[newIdx], newG)

print(max([i for i in C if i != None] + [0]))
