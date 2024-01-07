fun main() {
    try {
        val (a, b) = readln().split(" ").map { it.toInt() }
        for (i in 0 until a)
            println(readln().reversed())
    } catch (e: Exception) {}
}