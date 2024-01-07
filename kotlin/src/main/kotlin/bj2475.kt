fun main() {
    val inp = readln().split(" ").map { it.toInt() }
    var sum = 0
    for (i in inp) {
        sum += i * i
    }
    println(sum % 10)
}