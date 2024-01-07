fun main() {
    val n = readln().toInt()

    for (i in 0 until n) {
        val str = readln()

        println("${str[0]}${str[str.length - 1]}")
    }
}