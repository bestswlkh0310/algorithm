print(max([i * (idx + 1) for (idx, i) in enumerate([*sorted([int(input())for _ in range(int(input()))])][::-1])]))