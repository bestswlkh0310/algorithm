fun main() {
    val n = readln().toInt()

    for (i in 0 until n) {
        for (j in i until n) {
            print("*")
        }
        println()
    }
}