fun main() {
    val n = readln().toInt()

    for (i in 0 .. n) {
        var sum = 0
        sum += i + i.toString().toCharArray().map { it.toString().toInt() }.sum()
        if (n == sum) return println(i)
    }
    println(0)
}