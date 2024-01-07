fun main() {
    val testCase = readln().toInt()

    for (i in 0 until testCase) {
        val (a, str) = readln().split(" ")
        val n = a.toInt()
        val chrArr = str.toCharArray()

        for (j in 0 until chrArr.size) {
            for (k in 0 until n) {
                print(chrArr[j])
            }
        }
        println()
    }
}