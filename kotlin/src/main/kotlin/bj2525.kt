fun main() {
    val (h, m) = readln().split(" ").map { it.toInt() }
    val plus = readln().toInt()
    val sum = (h * 60 + m + + plus + 24 * 60) % (24 * 60)
    val hh = sum / 60
    val mm = sum % 60
    println("$hh $mm")
}