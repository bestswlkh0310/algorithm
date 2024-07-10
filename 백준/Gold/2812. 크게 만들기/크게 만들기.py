N, K = map(int, input().split())
G = [*map(int, [*input()])]

_K = K

result = [G[0]]
del G[0]

for i in G:
    if result[-1] > i:
        result.append(i)
        continue
    while len(result) and result[-1] < i and K > 0:
        K -= 1
        result.pop()
    result.append(i)

result = result[:N - _K]

for idx, i in enumerate(result):
    print(i, end='')
