fun main() {
    val (a, b, c) = readln().split(" ").map { it.toInt() }
    var sum = 0
    var cnt = 0
    if (b < c) {
        while (sum <= a) {
            sum += c - b
            cnt++
        }
        println(cnt)
    } else {
        println(-1)
    }
}