fun main() {
    val n = readln().toInt()

    var j = 0
    for (i in 1 .. n) {
        if (i * i > n) break
        j = i
    }
    println(j)
}