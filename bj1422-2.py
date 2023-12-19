k, n = map(int, input().split())

lst = []

for _ in range(k):
    n1 = int(input())
    lst.append(n1)

# 정렬: 왼쪽 내림차순 정렬
# 베스트:  높은 자리수 중 가장 큰 수

lst = list(reversed(sorted(lst, key=lambda x: x * 10 ** (k - len(str(x))) - len(str(x)) * 0.01)))

newLst = sorted(lst, key=lambda x: 12 - len(str(x)))

bst = newLst[0]

# print('lst', lst)
# print('bst', bst)

t = False

for i in lst:
    if i == bst and not t:
        print(str(i) * (n - k), end='')
        t = True
    print(i, end='')
