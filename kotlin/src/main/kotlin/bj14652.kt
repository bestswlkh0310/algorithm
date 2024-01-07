fun main() {
    val (a, b, c) = readln().split(" ").map { it.toInt() }
    println("${c / b} ${c % b}")
}