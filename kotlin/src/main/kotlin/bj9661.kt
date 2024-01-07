fun main() {
    val n = readln().toLong()
    if (n % 2 == 1L) {
        println("SK")
    } else {
        if (n % 4 == 0L) println("SK")
        else println("CY")
    }
}