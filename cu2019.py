a, b, c = map(int, input().split())
z = -b / 2 / a
w = b ** 2 - 4 * a * c
if w == 0:
    print("%.2f" % (z + ((abs(b**2 - 4 * a * c)) ** 0.5) / 2 / a))
elif w > 0:
    print("%.2f" %(((abs(b ** 2 - 4 * a * c)) ** 0.5) / 2 / a + z))
else:
    print("%.2f" % z, end="")
    aaa = (((abs(b ** 2 - 4 * a * c)) ** 0.5) / 2 / a)
    if aaa >= 0:
        print("+%.2fi" %aaa)
    else:
        print("+%.2fi" % abs(aaa))
if w == 0:
    if (w ** 0.5) % 1 != 0.0:
        print("%.2f" % (z - ((abs(b**2 - 4 * a * c)) ** 0.5) / 2 / a))
elif w > 0:
    print("%.2f"%(-((abs(b ** 2 - 4 * a * c)) ** 0.5) / 2 / a + z))
else:
    print("%.2f" % z, end="")
    aaa = (((abs(b ** 2 - 4 * a * c)) ** 0.5) / 2 / a)
    if aaa >= 0:
        print("-%.2fi" %aaa)
    else:
        print("%.2fi" % aaa)
