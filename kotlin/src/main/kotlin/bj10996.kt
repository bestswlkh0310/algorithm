fun main() {
    val n = readln().toInt()

    for (i in 0 until n * 2) {
        if (i % 2 == 1) print(" ")
        for (j in 0 until n / 2) print("* ")
        if (i % 2 == 0 && n % 2 == 1) print("*")
        println()
    }
}