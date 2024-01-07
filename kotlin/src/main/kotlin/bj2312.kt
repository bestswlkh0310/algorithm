fun main() {
    val c = readln().toInt()
    for (k in 0 until c) {
        var n = readln().toInt()
        val arr = Array (100001) { 0 }
        for (i in 0 .. n / 2) {
            for (j in 2 .. n) {
                if (n % j == 0) {
                    n /= j
                    arr[j]++
                    break
                }
            }
        }
        for ((i, j) in arr.withIndex()) {
            if (j != 0) {
                println("$i $j")
            }
        }
    }
}