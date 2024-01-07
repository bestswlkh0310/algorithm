fun main() {
    val n = readln().toInt()
    var sum = 0
    for (i in 0 until n) {
        val (a, b) = readln().split(" ").map { it.toInt() }
        sum += b % a
    }
    println(sum)
}