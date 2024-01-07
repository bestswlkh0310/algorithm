fun main() {
    val n = readln().toInt()
    var arr = ArrayDeque<Pair<Int, Int>>()

    for (i in 0 until n) {
        val (a, b) = readln().split(" ").map { it.toInt() }
        arr.add(Pair(a, b))
    }
    arr.sortWith(compareBy<Pair<Int, Int>> { it.second }.thenBy { it.first })
    for (i in 0 until n) {
        println("${arr[i].first} ${arr[i].second}")
    }
}