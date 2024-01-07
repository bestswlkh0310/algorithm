import java.lang.Integer.*

fun main() {
    val n = readln().toLong()

    for (i in 0 until n) {
        val (a, b) = readln().split(" ").map { it.toInt() }
        if (a == 0 || b == 0) {
            println(0)
            continue
        }

        val mx = max(a, b)
        val mn = min(a, b)
        val arr = Array( mx + 1 ) { Array (mx + 1) { 0 } }

        for (i in 0 until mx + 1) {
            arr[0][i] = 1
            arr[i][0] = 1
        }
        for (i in 0 .. mx + 1) {
            for (j in 0 .. (mx - i) + 1) {
                if (i == 0 || j == 0) continue
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
            }
        }
        println(arr[mx - mn][mn])
    }
}