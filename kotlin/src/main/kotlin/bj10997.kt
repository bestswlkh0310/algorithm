fun main() {
    val n = readln().toInt()
    if (n == 1) return println("*")
    var w = 4 * n - 3
    var h = 4 * n - 1

    var arr = Array (h) { Array (w) { '*' } }
    for (i in 0 until h / 2) {
        if (i % 2 == 0) continue
        for (j in 0 .. w - i * 2) {
            arr[i][i + j] = ' '
        }
        for (j in 0 until w - i * 2) {
            arr[h - i - 1][i + j] = ' '
        }
    }
    for (i in 0 until w / 2) {
        if (i % 2 == 0) continue
        for (j in 0 until h - i * 2) {
            arr[h - i - j - 1][i] = ' '
        }
        for (j in 0 until h - i * 2 - 2) {
            arr[h - i - j - 1][w - i - 1] = ' '
        }
    }
    for (i in 0 until h) {
        if (i == 1) {
            println("*")
            continue
        }
        for (j in 0 until w) {
            print(arr[i][j])
        }
        println()
    }
}