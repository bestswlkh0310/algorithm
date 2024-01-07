fun main() {
    val n = readln().toInt()

    for (i in 0 until n) {
        if (i % 2 == 1) print(" ")
        for (j in 0 until n) print("* ")
        println()
    }
}