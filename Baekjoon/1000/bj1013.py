for _ in range(int(input())):
    lst = list(map(int, list(input())))
    state = lst[0]
    t = 0
    k = True
    l = len(lst)

    for (idx, i) in enumerate(lst):
        if state == 0 and t == 2:
            state = i
            t = 0
        
        if state == 0:
            if i == 0 and t == 0:
                t = 1
            elif i == 1 and t == 1:
                t = 2
            else:
                k = False
                break
        elif state == 1:
            if i == 1 and t == 0:
                t = 1
            elif i == 0 and t == 1:
                t = 2
            elif i == 0 and 2 <= t <= 3:
                t = 3
            elif i == 1 and 3 <= t <= 4:
                t = 4
            elif i == 0 and t == 4:
                if idx - 2 < 0 or idx + 1 >= l:
                    k = False
                    break
                if lst[idx + 1] == 1:
                    state = 0
                    t = 1
                elif lst[idx - 2] == 0:
                    k = False
                    break
                else:
                    state = 1
                    t = 2
            else:
                k = False
                break
    if k and ((state == 0 and t == 2) or (state == 1 and t == 4)):
        print('YES')
    else:
        print('NO')