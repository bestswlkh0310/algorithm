fun main() {
    var s = 0
    var sum = 0
    val n = readln().toInt()
    while (true) {
        s++
        if (s.toString().contains("666")) sum++
        if (sum == n) break
    }
    println(s)
}