import java.lang.Integer.*

fun main() {
    val n = readln().toInt()

    for (i in 1 .. n) {
        val (a, b, c) = readln().split(" ").map { it.toInt() }
        val min = min(a, min(b, c))
        val max = max(a, max(b, c))
        val mid = a + b + c - min - max
        val bool = max * max == min * min + mid * mid

        if (bool) {
            println("Scenario #$i:")
            println("yes\n")
        }
        else {
            println("Scenario #$i:")
            println("no\n")

        }
    }
}