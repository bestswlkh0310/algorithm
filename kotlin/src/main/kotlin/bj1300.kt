fun main() {
    val nn = readln().toInt()
    val k = readln().toInt()
    val n = nn * nn

    println((k % n) * (k / n))
}