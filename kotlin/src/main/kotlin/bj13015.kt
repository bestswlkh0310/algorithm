fun main() {
    val n = readln().toInt()
    val h = n * 2 - 1
    val w = 4 * n - 3
    val arr = Array(h) { Array(w) { " " } }

    for (i in 0 until n) {
        arr[0][i] = "*"
        arr[0][w - i - 1] = "*"
        arr[h - 1][i] = "*"
        arr[h - 1][w - i - 1] = "*"
    }
    for (i in 1 .. h - 2) {
        arr[i][n + i - 1] = "*"
        arr[i][w - n - i] = "*"
        if (i <= h / 2) {
            arr[i][i] = "*"
            arr[i][w - i - 1] = "*"
        } else {
            arr[i][h - 1 - i] = "*"
            arr[i][w - h + i] = "*"
        }
    }
    s@
    for (y in 0 until h) {
        for (x in 0 until w) {
            if (y > 0 && y < h / 2) {
                if (x >= w - y) {
                    println()
                    continue@s
                }
            } else if (y >= h / 2 && y < h){
                if (x >= w + y - n * 2 + 2) {
                    println()
                    continue@s
                }
            }
            print(arr[y][x])
        }
        println()
    }
}