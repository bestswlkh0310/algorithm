fun main() {
    val (a, x) = readln().split(" ").map { it.toInt() }
    println(x * 2 - a)
}