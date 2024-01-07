fun main() {
    val n = readln().toInt()

    for (i in 1 until n) {
        for (j in i until n) print(" ")
        for (j in 0 until i) print("*")
        println()
    }
    for (i in 1 .. n) {
        for (j in 1 until i) print(" ")
        for (j in i .. n) print("*")
        println()
    }
}