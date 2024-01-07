import sys

sys.setrecursionlimit(10**4)

input = sys.stdin.readline

def init_tree(node, s, e):
    if s == e:
        if lst[s]: # 홀수
            T[node][0] += 1
        else:
            T[node][1] += 1
        return T[node]

    lc = init_tree(node * 2, s, (s + e) // 2)
    rc = init_tree(node * 2 + 1, (s + e) // 2 + 1, e)

    T[node][0] = lc[0] + rc[0]
    T[node][1] = lc[1] + rc[1]
    return T[node]


def sub_sum(node, s, e, s1, e1):

    # 겹치지 않음
    if s > e1 or e < s1: return [0, 0]

    # 포함 됨 -> 이미 존재함
    if s >= s1 and e <= e1: return T[node]

    lc = sub_sum(node * 2, s, (s + e) // 2, s1, e1)
    rc = sub_sum(node * 2 + 1, (s + e) // 2 + 1, e, s1, e1)

    return [lc[0] + rc[0], lc[1] + rc[1]]

def update(node, s, e, idx, diff):
    if idx < s or idx > e: return

    if diff:
        T[node][0] += 1
        T[node][1] -= 1
    else:
        T[node][0] -= 1
        T[node][1] += 1

    if s != e:
        update(node * 2, s, (s + e) // 2, idx, diff)
        update(node * 2 + 1, (s + e) // 2 + 1, e, idx, diff)

n = int(input())
lst = [bool(i % 2) for i in [*map(int, input().split())]]
T = [[0, 0] for _ in range(3000000)]

init_tree(1, 0, n - 1)

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    b -= 1

    if a == 1:
        c = bool(c % 2)
        if lst[b] != c:
            lst[b] = c
            update(1, 0, n - 1, b, c % 2)
    else:
        v = sub_sum(1, 0, n - 1, b, c - 1)
        print(v[not(a%2)])
        
