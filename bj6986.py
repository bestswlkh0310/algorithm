import sys
n, k = map(int, sys.stdin.readline().split())
arr = []
for i in range(n): arr.append(float(sys.stdin.readline()))
arr.sort()
g = arr[k:n-k]
print("%.2f" %(sum(g) / len(g) + 0.00000001))
print("%.2f" %((sum(g) + (g[0] + g[-1]) * k) / (len(g) + k * 2) + 0.00000001))