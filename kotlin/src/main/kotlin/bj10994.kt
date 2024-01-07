fun main() {
    val n = readln().toInt()
    val len = 4 * (n - 1) + 1

    var arr = Array (len) {Array(len) {' '} }


    for (i in 0 until n) {
        val centerPos = len / 2
        for (j in 0 .. (4 * i + 1) / 2) {
            arr[centerPos + j][centerPos + i * 2] = '*'
            arr[centerPos - j][centerPos + i * 2] = '*'
            arr[centerPos + j][centerPos - i * 2] = '*'
            arr[centerPos - j][centerPos - i * 2] = '*'

            arr[centerPos + i * 2][centerPos + j] = '*'
            arr[centerPos - i * 2][centerPos + j] = '*'
            arr[centerPos + i * 2][centerPos - j] = '*'
            arr[centerPos - i * 2][centerPos - j] = '*'
        }
    }
    for (i in 0 until len) {
        for (j in 0 until len) {
            print(arr[i][j])
        }
        println()
    }
}
//2 * 2 * 0 + 1 => 1
//2 * 2 * 1 + 1 => 5
//2 * 2 * 2 + 1 => 9
//2 * 2 * 3 + 1 => 13