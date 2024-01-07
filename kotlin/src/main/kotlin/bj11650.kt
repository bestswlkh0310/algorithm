fun main() {
    val n = readln().toInt()

    var arr: MutableList<MutableList<Int>> = Array (n) { Array(2){ 0 }.toMutableList() }.toMutableList()

    for (i in 0 until n) {
        val (a, b) = readln().split(" ").map { it.toInt() }
        arr[i][0] = a
        arr[i][1] = b
    }
    arr.sortWith(compareBy<MutableList<Int>> { it[0] }.thenBy { it[1] } )
    arr.forEach { println("${it[0]} ${it[1]}") }
}