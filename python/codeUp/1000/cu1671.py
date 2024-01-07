a, b = map(int, input().split())
if (a == 1 and b == 2) or (a == 0 and b == 1) or (a == 2 and b == 0):
    print("win")
elif (a == b):
    print("tie")
else:
    print("lose")