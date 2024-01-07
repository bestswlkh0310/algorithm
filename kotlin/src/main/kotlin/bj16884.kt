fun main() {
    val n = readln().toInt()
    for (i in 0 until n) {
        val inp = readln().toInt()
        if (inp % 2 == 1) {
            println("koosaga")
        } else {
            println("cubelover")
        }
    }
}