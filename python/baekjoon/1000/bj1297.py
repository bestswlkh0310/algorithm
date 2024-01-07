d, h, w = map(int, input().split())
s = d / ((h**2+w**2) ** 0.5)
print(int(h * s), int(w * s))