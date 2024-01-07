import sys

sys.setrecursionlimit(10**4)

input = sys.stdin.readline

def init_tree(node, s, e):
    if s == e:
        T[node] = lst[s]
        return T[node]

    lc = init_tree(node * 2, s, (s + e) // 2)
    rc = init_tree(node * 2 + 1, (s + e) // 2 + 1, e)

    T[node] = min([lc, rc])
    return T[node]


def sub_sum(node, s, e, s1, e1):
    # 겹치지 않음
    if s > e1 or e < s1: return 1_000_000_001

    # 포함 됨 -> 이미 존재함
    if s >= s1 and e <= e1: return T[node]

    lc = sub_sum(node * 2, s, (s + e) // 2, s1, e1)
    rc = sub_sum(node * 2 + 1, (s + e) // 2 + 1, e, s1, e1)

    return min([lc, rc])

def update(node, s, e, idx, c):
    if idx < s or idx > e: return


    if s == e:
        T[node] = c
        return

    update(node * 2, s, (s + e) // 2, idx, c)
    update(node * 2 + 1, (s + e) // 2 + 1, e, idx, c)
    T[node] = min([T[node * 2], T[node * 2 + 1]])

n = int(input())
lst = [*map(int, input().split())]
T = [1_000_000_001 for _ in range(3000000)]

init_tree(1, 0, n - 1)

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    if a == 1:
        b -= 1
        lst[b] = c
        update(1, 0, n - 1, b, c)
    else:
        print(sub_sum(1, 0, n - 1, b - 1, c - 1))
