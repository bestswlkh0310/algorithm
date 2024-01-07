import java.lang.Integer.*

fun main() {
    val n = readln().toInt()
    var minX = Int.MAX_VALUE
    var maxX = Int.MIN_VALUE
    var minY = Int.MAX_VALUE
    var maxY = Int.MIN_VALUE

    for (i in 0 until n) {
        val (a, b) = readln().split(" ").map { it.toInt() }
        minX = min(minX, a)
        maxX = max(maxX, a)
        minY = min(minY, b)
        maxY = max(maxY, b)
    }

    println((maxX - minX) * (maxY - minY))
}