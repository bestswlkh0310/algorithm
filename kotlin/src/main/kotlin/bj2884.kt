fun main() {
    val (h, m) = readln().split(" ").map { it.toInt() }
    val sum = (h * 60 + m + 1440 - 45) % 1440
    println("${sum / 60} ${sum % 60}")
}