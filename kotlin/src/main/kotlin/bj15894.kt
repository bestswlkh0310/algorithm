// 음수 포함으로 수정하기

fun main() {
    val inp = readln().toInt()
    for (k in 0 until inp) {
        var (a, b) = readln().split(" ").map { it.toInt() }
        val n = a
        var sum = 0
        for (i in 1 until n) {
            for (j in 3 .. n / 2 step 2) {
                if (a % 2 == 0) {
                    a /= 2
                    sum += 2
                }
                if (a % j == 0) {
                    a /= j
                    sum += j
                }
            }
        }
        if (sum == b) {
            println("yes")
        } else {
            println("no")
        }
    }
}