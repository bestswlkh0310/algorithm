fun main() {
    val n = readln().toInt()
    var s = 2
    for (i in 0 until n) {
        s = s * 2 -1
    }
    println(s * s)
}