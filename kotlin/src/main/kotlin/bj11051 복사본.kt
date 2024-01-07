fun main() {
    val (a, b) = readln().split(" ").map { it.toInt() }
    val c = fac(a) / fac(b) / fac(a - b)
    println(c)
}

private fun fac(n: Int): Int {
    var sum = 1
    for (i in 1 .. n) {
        sum *= i
    }
    return sum
}