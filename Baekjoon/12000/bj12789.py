n = int(input())

arr = list(map(int, input().split()))

stack = []

current_n = 1
current_idx = 0

while current_n < n:
    if current_idx < n and arr[current_idx] == current_n:
        current_n += 1
        current_idx += 1
    elif len(stack) != 0 and stack[-1] == current_n:
        current_n += 1
        del stack[-1]
    else:
        if len(stack) != 0 and arr[current_idx] > stack[-1]:
            print('Sad')
            exit(0)
        stack.append(arr[current_idx])
        current_idx += 1

print('Nice')