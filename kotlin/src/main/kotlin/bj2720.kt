fun main() {
    val n = readln().toInt()
    val arr = arrayListOf(25, 10, 5, 1)
    repeat(n) {
        val result = arrayListOf(0, 0, 0, 0)
        var m = readln().toInt()
        while (m != 0) {
            for ((i, j) in arr.withIndex()) {
                if (m - j >= 0) {
                    m -= j
                    result[i]++
                    break
                }
            }
        }
        result.forEach { print("$it ") }
        println()
    }
}