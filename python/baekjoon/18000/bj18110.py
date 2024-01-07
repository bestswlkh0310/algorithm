import sys

def round(n):
    k = str(float(n)).split('.')
    i = int(k[0])
    if int(k[1][0]) >= 5:
        i += 1

    return i

arr = sorted([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))])
if len(arr) == 0: print(0); exit(0)
n = round(len(arr) * 0.15)

arr = arr[n:len(arr)-n]
print(round(sum(arr) / float(len(arr))))
