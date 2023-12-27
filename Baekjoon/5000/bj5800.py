for i in range(int(input())):
    mx = 0
    lst = list(map(int, input().split()))
    del lst[0]
    lst.sort()
    for idx in range(1, len(lst)):
        a = abs(lst[idx] - lst[idx - 1])
        if mx < a:
            mx = a
    print(f"Class {i + 1}")
    print(f"Max {max(lst)}, Min {min(lst)}, Largest gap {mx}")