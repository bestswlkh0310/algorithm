import java.lang.Integer.min

fun main() {
    val n = readln().toInt()
    var sum = 0
    var cnt = 0
    var minCnt = Int.MAX_VALUE
    var isss = false
    for (i in 1 .. n / 3 + 1) {
        for (j in i until n / 3 + 1) {
            if (sum <= n - 5) {
                sum += 5
                cnt++
            }
        }
        for (j in 0 .. n / 3 + 1) {
            if (sum <= n - 3) {
                sum += 3
                cnt++
            }
        }
        if (sum == n) {
            isss = true
            minCnt = min(minCnt, cnt)
        }
        sum = 0
        cnt = 0
    }
    if (isss) {
        println(minCnt)
    } else println(-1)
}