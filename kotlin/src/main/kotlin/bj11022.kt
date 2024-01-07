fun main() {
    val n = readln().toInt()

    for (i in 0 until n) {
        val (a, b) = readln().split(" ").map { it.toInt() }
        println("Case #${i + 1}: $a + $b = ${a + b}")
    }
}