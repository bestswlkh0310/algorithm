fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    var arr = Array(n) { it + 1 }
    for (i in 0 until m) {
        val (a, b) = readln().split(" ").map { it.toInt() }
        arr[a - 1] = arr[b - 1].also { arr[b - 1] = arr[a - 1] }
    }

    for (i in 0 until n) {
        print("${arr[i]} ")
    }
}
