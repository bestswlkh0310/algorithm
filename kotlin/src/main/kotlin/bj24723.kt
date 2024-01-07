fun main() {
    val n = readln().toInt()

    var sum = 1
    repeat(n) {
        sum *= 2
    }
    println(sum)
}
