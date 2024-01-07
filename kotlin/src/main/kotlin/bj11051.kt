import java.math.BigInteger

fun main() {
    val (b, a) = readln().split(" ").map { it.toInt() }

    val arr = Array( b + 1 ) { Array (b + 1) { BigInteger.ONE } }

    for (i in 0 until b + 1) {
        arr[0][i] = BigInteger.ONE
        arr[i][0] = BigInteger.ONE
    }
    for (i in 0 .. b + 1) {
        for (j in 0 .. (b - i) + 1) {
            if (i == 0 || j == 0) continue
            arr[i][j] = (arr[i - 1][j] + arr[i][j - 1]) % BigInteger("10007")
        }
    }
    println(arr[b - a][a])
}