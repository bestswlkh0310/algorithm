import kotlin.math.abs

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()

    val n = br.readLine()
    val inp = br.readLine().split(" ").map { it.toInt() }

    var sum = Int.MAX_VALUE
    var best: MutableList<Int> = arrayListOf()
    for (i in inp) {
        var tmpSum = 0
        for (j in inp) {
            tmpSum += abs(i - j)
        }
        if (tmpSum == sum) {
            sum = tmpSum
            best.add(i)
        }
        if (tmpSum < sum) {
            sum = tmpSum
            best.clear()
            best.add(i)
        }
    }

    println(best.min())
}