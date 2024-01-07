import java.lang.Integer.*

fun main() {
    while (true) {
        val (a, b, c) = readln().split(" ").map { it.toInt() }
        if (a == 0) return
        val min = min(a, min(b, c))
        val max = max(a, max(b, c))
        val mid = a + b + c - min - max
        if (max * max == min * min + mid * mid) {
            println("right")
        } else {
            println("wrong")
        }
    }
}