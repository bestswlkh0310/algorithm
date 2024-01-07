fun main() {
    val (k, n) = readln().split(" ").map { it.toLong() }
    var arr = Array (k.toInt()) { 0L }
    var max = -1L
    for (i in 0 until k) {
        arr[i.toInt()] = readln().toLong()
        if (max < arr[i.toInt()]) max = arr[i.toInt()]
    }

    var sum: Long
    var result = 0L
    for (i in 1 .. max) {
        sum = arr.sumOf { it / i }
        result = i
        if (sum < n) break
    }
    if (n == 1L) return println(result)
    println(result - 1)
}