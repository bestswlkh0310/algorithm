fun main() {
    val n = readln().toInt()

    for (i in 0 until n) {
        for (j in 0 until i) {
            print(" ")
        }
        for (j in i * 2 until n * 2 - 1) {
            print("*")
        }
        println()
    }
}