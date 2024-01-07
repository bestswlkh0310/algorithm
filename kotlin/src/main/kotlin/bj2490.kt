fun main() {
    repeat(3) {
        val lst = readln().split(" ").map { it.toInt() }
        when (lst.sum()) {
            0 -> println("D")
            1 -> println("C")
            2 -> println("B")
            3 -> println("A")
            4 -> println("E")
        }
    }
}