fun main() {
    val inp = readln().toInt()
    var i = 6
    var sum = 1
    var n = 1
    while ((inp - 2) / i != 0) {
        n++
        sum += n
        i = 6 * sum
    }
    if (inp == 1) return println(1)
    println(n + 1)
}

// -2후 6 ( 1 ), 6 ( 1 + 2 ), 6 ( 1 + 2 + 3 ) 으로 나눈 값 출력