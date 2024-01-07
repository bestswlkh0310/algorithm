fun main() {
    val n = readln().toInt()
    var arr = readln().split(" ").map { it.toLong() }.toMutableList()

    println(arr.min() * arr.max())
}