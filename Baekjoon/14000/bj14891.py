class Gear():
    def __init__(self, arr, head=0):
        self.head = head
        self.arr = arr

l = 4
g = 8

gearLst = [Gear(list(map(int, list(input())))) for _ in range(l)]


# print('======', 0, '======')
# for i in gearLst:
#     print(i.head, i.arr)

for j in range(int(input())):
    n, r = map(int, input().split())

    beforeHead = gearLst[n - 1].head
    beforeHead1 = beforeHead
    
    gearLst[n - 1].head = ((gearLst[n - 1].head) - r) % g
    for i in range(n - 2, -1, -1):
        pGear = gearLst[i + 1]
        nGear = gearLst[i]
        if pGear.arr[(beforeHead - 2) % g] != nGear.arr[(nGear.head + 2) % g]:
            beforeHead = nGear.head
            if ((n - 1) - i) % 2:
                nGear.head = (nGear.head + r) % g
            else:
                nGear.head = (nGear.head - r) % g
            continue
        break
    
    beforeHead = beforeHead1

    for i in range(n, l):
        pGear = gearLst[i - 1]
        nGear = gearLst[i]
        # print('log -', i, beforeHead, nGear.head)
        if pGear.arr[(beforeHead + 2) % g] != nGear.arr[(nGear.head - 2) % g]:
            beforeHead = nGear.head
            # print(nGear.head, r, -r)
            if (i - (n - 1)) % 2:
                nGear.head = (nGear.head + r) % g
            else:
                nGear.head = (nGear.head - r) % g
            continue

        break

    # print('======', j + 1, '======')
    # for i in gearLst:
        # print(i.head, i.arr)

cnt = 0

for (idx, i) in enumerate(gearLst):
    # print('head', i.head, i.arr[i.head])
    if i.arr[i.head] == 1:
        cnt += 2 ** idx


print(cnt)