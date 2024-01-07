import kotlin.math.max

fun main() {
    val (a, b, c) = readln().split(" ").map { it.toInt() }

    if (a == b && a == c) println(10000 + a * 1000)
    else if (a == b) println(1000 + a * 100)
    else if (a == c) println(1000 + a * 100)
    else if (b == c) println(1000 + b * 100)
    else println(max(a,max(b, c)) * 100)
}