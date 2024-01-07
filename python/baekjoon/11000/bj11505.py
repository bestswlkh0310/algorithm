import sys

sys.setrecursionlimit(10**4)
D = 1_000_000_007

input = sys.stdin.readline

def init_tree(node, s, e):
    if s == e:
        T[node] = lst[s]
        return T[node]

    lc = init_tree(node * 2, s, (s + e) // 2)
    rc = init_tree(node * 2 + 1, (s + e) // 2 + 1, e)

    T[node] = (lc * rc)
    return T[node]

def sub_sum(node, s, e, s1, e1):
    # 겹치지 않음
    if s > e1 or e < s1: return 1

    # 포함 됨 -> 이미 존재함
    if s >= s1 and e <= e1: return T[node] % D

    lc = sub_sum(node * 2, s, (s + e) // 2, s1, e1)
    rc = sub_sum(node * 2 + 1, (s + e) // 2 + 1, e, s1, e1)

    return (lc * rc) % D

def update(node, s, e, idx, diff, x):
    if idx < s or idx > e: return

    if T[node] == 0:
        T[node] = diff
    else:
        T[node] = T[node] * diff // x

    if s != e:
        update(node * 2, s, (s + e) // 2, idx, diff, x)
        update(node * 2 + 1, (s + e) // 2 + 1, e, idx, diff, x)

n, m, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]
T = [1 for _ in range(3000000)]

init_tree(1, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())

    # print([i for i in T if i != 1])

    if a == 1:
        b -= 1
        x1 = lst[b]
        lst[b] = c
        update(1, 0, n - 1, b, c, x1)
    elif a == 2:
        print(int(sub_sum(1, 0, n - 1, b - 1, c - 1)) % 1_000_000_007)
