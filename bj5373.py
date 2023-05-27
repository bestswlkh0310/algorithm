def 오른쪽위회전():
    for y in range(3):
        for x in range(3):
            roArr[x][y] = arr[0][2 - y][x]
    arr[0] = [i[:] for i in roArr]
    tempArr = arr[2][0][:]
    for i in range(2, 5):
        arr[i][0] = arr[i + 1][0][:]
    arr[5][0] = tempArr

def 오른쪽아래회전():
    for y in range(3):
        for x in range(3):
            roArr[x][y] = arr[1][2 - y][x]
    arr[1] = [i[:] for i in roArr]
    tempArr = arr[5][2][:]
    for i in range(5, 2, -1):
        arr[i][2] = arr[i - 1][2][:]
    arr[2][2] = tempArr


def 왼쪽앞회전():
    for y in range(3):
        for x in range(3):
            roArr[x][y] = arr[2][2 - y][x]
    arr[2] = [i[:] for i in roArr]
    Arr1 = arr[0][2][:]
    Arr2 = [arr[3][2 - i][0] for i in range(3)]
    Arr3 = arr[1][0][:]
    Arr4 = [arr[5][2 - i][2] for i in range(3)]
    for i in range(3):
        arr[0][2][i] = Arr4[i]
        arr[3][i][0] = Arr1[i]
        arr[1][0][i] = Arr2[i]
        arr[5][i][2] = Arr3[i]
def 오른쪽으로_돌려버리기():
    for y in range(3):
        for x in range(3):
            roArr[x][y] = arr[0][2 - y][x]
    arr[0] = [i[:] for i in roArr]
    # print([i[:] for i in roArr],"dasd")
    for y in range(3):
        for x in range(3):
            roArr[x][y] = arr[1][2 - y][x]
    arr[1] = [i[:] for i in roArr]
    for y in range(3):
        for x in range(3):
            roArr[x][y] = arr[1][2 - y][x]
    arr[1] = [i[:] for i in roArr]
    for y in range(3):
        for x in range(3):
            roArr[x][y] = arr[1][2 - y][x]
    arr[1] = [i[:] for i in roArr]

    tempArr = [i[:] for i in arr[2]] # 앞
    arr[2] = [i[:] for i in arr[3]] # 앞은 오른쪽꺼
    arr[3] = [i[:] for i in arr[4]] # 오른쪽은 뒤쪽 꺼
    arr[4] = [i[:] for i in arr[5]] # 뒤쪽은 왼쪽 꺼
    arr[5] = tempArr # 왼쪽은 앞
def 왼쪽으로_돌려버리기():
    for i in range(3): 오른쪽으로_돌려버리기()

roArr = [[0] * 3 for _ in range(3)]
C = ["w", "y", "r", "b", "o", "g"]
#     위   아래   앞   오    뒤    왼
for _ in range(int(input())):
    arr = []
    # arr = [[['w1', 'w2', 'w3'], ['w4', 'w5', 'w6'], ['w7', 'w8', 'w9']],
    #        [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']],
    #        [['r1', 'r2', 'r3'], ['r4', 'r5', 'r6'], ['r7', 'r8', 'r9']],
    #        [['b1', 'b2', 'b3'], ['b4', 'b5', 'b6'], ['b7', 'b8', 'b9']], [['o1', 'o2', 'o3'], ['o4', 'o5', 'o6'], ['o7', 'o8', 'o9']],
    #        [['g1', 'g2', 'g3'], ['g4', 'g5', 'g6'], ['g7', 'g8', 'g9']]]
    for c in C:
        arr.append([[c for j in range(3)] for i in range(3)])
    _ = int(input())
    for inp in list(input().split()):
        roArr = [[0] * 3 for _ in range(3)]
        if inp == "U+":
            오른쪽위회전()
        elif inp == "U-":
            오른쪽위회전()
            오른쪽위회전()
            오른쪽위회전()
        elif inp == "D+":
            오른쪽아래회전()
        elif inp == "D-":
            오른쪽아래회전()
            오른쪽아래회전()
            오른쪽아래회전()
        elif inp == "F+":
            왼쪽앞회전()
        elif inp == "F-":
            왼쪽앞회전()
            왼쪽앞회전()
            왼쪽앞회전()
        elif inp == "B+":
            오른쪽으로_돌려버리기()
            오른쪽으로_돌려버리기()
            왼쪽앞회전()
            오른쪽으로_돌려버리기()
            오른쪽으로_돌려버리기()
        elif inp == "B-":
            오른쪽으로_돌려버리기()
            오른쪽으로_돌려버리기()
            왼쪽앞회전()
            왼쪽앞회전()
            왼쪽앞회전()
            오른쪽으로_돌려버리기()
            오른쪽으로_돌려버리기()
        elif inp == "L+":
            왼쪽으로_돌려버리기()
            왼쪽앞회전()
            오른쪽으로_돌려버리기()
        elif inp == "L-":
            왼쪽으로_돌려버리기()
            왼쪽앞회전()
            왼쪽앞회전()
            왼쪽앞회전()
            오른쪽으로_돌려버리기()
        elif inp == "R+":
            오른쪽으로_돌려버리기()
            왼쪽앞회전()
            왼쪽으로_돌려버리기()
        elif inp == "R-":
            오른쪽으로_돌려버리기()
            왼쪽앞회전()
            왼쪽앞회전()
            왼쪽앞회전()
            왼쪽으로_돌려버리기()
        # elif inp == "돌리기테스트":
        #     오른쪽으로_돌려버리기()

    # print(arr)
    for i in arr[0]:
        for j in i:
            print(end=f"{j}")
        print()
