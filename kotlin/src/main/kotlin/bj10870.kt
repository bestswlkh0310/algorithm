fun main() {
    val n = readln().toInt()
    println(fb(n))
}

private fun fb (n: Int): Int {
    if (n == 0) return 0
    if (n <= 2) return 1
    return fb(n - 1) + fb(n - 2)
}