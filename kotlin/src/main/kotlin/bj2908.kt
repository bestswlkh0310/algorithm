import kotlin.math.max

fun main() {
    val (a, b) = readln().split(" ").map { it.toCharArray() }
    a.reverse()
    b.reverse()
    val aa = a.joinToString("").toInt()
    val bb = b.joinToString("").toInt()

    println(max(aa, bb))
}