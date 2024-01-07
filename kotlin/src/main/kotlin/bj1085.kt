import java.lang.Integer.min

fun main() {
    val (x, y, w, h) = readln().split(" ").map { it.toInt() }
    println(min(min(x, w - x), min(y, h - y)))
}