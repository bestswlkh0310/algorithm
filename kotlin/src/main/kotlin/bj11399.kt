fun main() {
    val n = readln().toInt()
    val arr = readln().split(" ").map { it.toInt() }.sorted()
    var sum = 0
    for (i in 0 until n) {
        sum += arr[i] * (n - i)
    }
    println(sum)
}

// 1 2 3 3 4
// 1 3 6 9 13
// 32