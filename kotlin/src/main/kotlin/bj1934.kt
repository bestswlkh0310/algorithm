fun main() {
    val n = readln().toInt()

    for (i in 0 until n) {
        val (a, b) = readln().split(" ").map { it.toInt() }
        println(a * b / gcd(a, b))
    }
}

private fun gcd(a: Int, b: Int): Int = if (b != 0) gcd(b, a % b) else a