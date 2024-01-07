fun main() {
    val (n, mx) = readln().split(" ").map { it.toInt() }
    val arr = readln().split(" ").map { it.toInt() }

    var best = 0
    for (i in 0 until arr.size) {
        for (j in i + 1 until arr.size) {
            for (k in j + 1 until arr.size) {
                val t = arr[i] + arr[j] + arr[k]
                if (t > best && t <= mx) best = t
            }
        }
    }
    println(best)
}