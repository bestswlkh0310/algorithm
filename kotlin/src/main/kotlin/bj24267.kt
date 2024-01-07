fun main() {
    val n = readln().toLong()

    var sum = 0L
    for (i in 1 .. n - 2) {
        sum += (n-1 - i) * i
    }
    println(sum)
    println(3)
}