n, c = map(int, input().split())
lst = list(map(int, input().split()))

from collections import Counter

mc = Counter(lst).most_common()

for i in mc:
    for j in range(i[1]):
        print(f'{i[0]} ', end='')