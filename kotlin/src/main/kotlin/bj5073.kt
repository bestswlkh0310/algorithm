import kotlin.math.max

fun main() {
    while (true) {
        val (a, b, c) = readln().split(" ").map { it.toInt() }
        if (a == 0 && b == 0 && c == 0) break
        val max = max(a, max(b, c))
        if (max < a + b + c - max) {
            if (a == b && b == c) println("Equilateral")
            else if (a == b || b == c || a == c) println("Isosceles")
            else println("Scalene")
        } else {
            println("Invalid")
        }
    }
}