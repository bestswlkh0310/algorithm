fun main() {
    // 100 * 100 리스트 생성
    // 좌표 입력 -> 리스트에 저장
    // 1 초과x
    // 리스트에 1의 개수 구하기
    //https://www.acmicpc.net/problem/2669

    val array = Array(100) { Array(100) { 0 } }

    for (i in 0 until 4) {
        val inp = readln().split(" ").map { it.toInt() }
        val x1 = inp[0]
        val y1 = inp[1]
        val x2 = inp[2]
        val y2 = inp[3]
        for (x in x1 until x2) {
            for (y in y1 until y2) {
                array[x - 1][y - 1] = 1
            }
        }
    }
    print(array.flatten().count { it == 1 })
}