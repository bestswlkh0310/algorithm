import java.lang.Integer.min

fun main() {
    val (a, b) = readln().split(" ").map { it.toInt() }
    var arr = ArrayList<CharArray>()

    for (i in 0 until a) {
        arr.add(readln().toCharArray())
    }
    var v = 9999

    for (i in 0 .. a - 8) {
        for (j in 0 .. b - 8) {
            v = min(check(arr, j, i), v)
        }
    }
    println(v)
}

private fun check(arr: ArrayList<CharArray>, x1: Int, y1: Int): Int {
    var sum1 = 64
    var sum2 = 64
    for (i in 0 until 8) {
        for (j in 0 until 8) {
            if (i % 2 == 0) {
                if ((arr[i + y1][j + x1] == 'W') && ((i * 8 + j + 1) % 2 == 0)) sum1--
                if ((arr[i + y1][j + x1] == 'B') && ((i * 8 + j + 1) % 2 == 1)) sum1--
            } else {
                if ((arr[i + y1][j + x1] == 'W') && ((i * 8 + j + 1) % 2 == 1)) sum1--
                if ((arr[i + y1][j + x1] == 'B') && ((i * 8 + j + 1) % 2 == 0)) sum1--
            }
        }
    }
    for (i in 0 until 8) {
        for (j in 0 until 8) {
            if (i % 2 == 0) {
                if ((arr[i + y1][j + x1] == 'W') && ((i * 8 + j + 1) % 2 == 1)) sum2--
                if ((arr[i + y1][j + x1] == 'B') && ((i * 8 + j + 1) % 2 == 0)) sum2--
            } else {
                if ((arr[i + y1][j + x1] == 'W') && ((i * 8 + j + 1) % 2 == 0)) sum2--
                if ((arr[i + y1][j + x1] == 'B') && ((i * 8 + j + 1) % 2 == 1)) sum2--
            }
        }
    }
    return min(sum1, sum2)
}