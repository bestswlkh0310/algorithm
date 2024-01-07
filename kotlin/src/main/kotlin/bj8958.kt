fun main() {
    val testCase = readln().toInt()

    for (i in 0 until testCase) {
        val str = readln().toCharArray()

        var sum = 0
        var t = 0
        for (j in str) {
            if (j == 'O') t++
            if (j == 'X') {
                for (k in 1 .. t) {
                    sum += k
                }
                t = 0
            }
        }
        for (j in 1 .. t) {
            sum += j
        }
        println(sum)
    }
}