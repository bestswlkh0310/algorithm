fun main() {
    val str = readln().toCharArray()
    for ((i, j) in str.withIndex()) {
        print(j)
        if ((i + 1) % 10 == 0) {
            println()
        }
    }
}