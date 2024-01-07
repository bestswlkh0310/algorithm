fun main() {
    val (y, x) = readln().split(" ").map { it.toInt() }
    val arr = Array ( y ) { Array ( x ) { 0 } }
    for (i in 0 until y) {
        val a = readln().split(" ").map { it.toInt() }
        for (j in 0 until x) {
            arr[i][j] = a[j]
        }
    }
}