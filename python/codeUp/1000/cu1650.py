arr = [
" ****  ***  ***   ***** *   * ****",
"*     *   * *  *  *     *   * *   *",
"*     *   * *   * *     *   * *   *",
"*     *   * *   * ****  *   * ****",
"*     *   * *   * *     *   * *",
"*     *   * *  *  *     *   * *",
" ****  ***  ***   *****  ***  *"
]

w, h = map(int, input().split())
arr1 = []

for i in range(len(arr) * h):
    wl = len(arr[i // h]) * w
    hArr = [False] * wl
    for j in range(wl):
        hArr[j] = arr[i // h][j // w]
    arr1.append(hArr)
for i in arr1:
    print("".join(i))