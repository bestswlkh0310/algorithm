import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr1 = sorted(list(set(arr)))
dic = dict()
for i in range(len(arr1)):
    dic[arr1[i]] = i

for i in arr:
    sys.stdout.write(f"{dic[i]} ")