fun main() {
    val n = readln().toInt()

    for (i in 0 until n) {
        for (j in i until n - 1) {
            print(" ")
        }
        for (j in 0 .. i) {
            print("*")
        }
        println()
    }
}