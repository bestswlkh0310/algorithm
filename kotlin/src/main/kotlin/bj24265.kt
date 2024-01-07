fun main() {
    val inp = readln().toLong()

    var sum = 0L
    for (i in 1L until inp) {
        sum += i
    }
    println(sum)
    println(2)
}