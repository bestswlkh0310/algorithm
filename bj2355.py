a, b = map(int, input().split())
mx = max(a, b)
mn = min(a, b)
print((mn + mx) * (mx - mn + 1) // 2)