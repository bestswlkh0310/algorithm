import kotlin.math.max

fun main() {
    val br = System.`in`.bufferedReader()
    val (n, c) = br.readLine().split(" ").map { it.toInt() } // 집 개수, 공유기 수
    val arr = Array(n) { br.readLine().toLong() }

    arr.sort()
    br.close()
    var l = 1L
    var r = arr[n - 1] - arr[0]

    var maxDistance = 0L

    // 이진 탐색
    while (l <= r) {
        val target = (l + r) / 2

        // 설치할 수 있는 공유기 개수 계산
        var installableCnt = 1
        var prev = arr[0]

        for (i in 1 until n) {
            if (arr[i] - prev >= target) {
                installableCnt++
                prev = arr[i]
            }
        }

        if (installableCnt >= c) {
            // 설치한 공유기가 설치해야 하는 공유기보다 많을 때
            l = target + 1
            maxDistance = max(maxDistance, target)
        } else {
            // 설치한 공유기가 설치해야 하는 공유기보다 적을 때
            l = target - 1
        }
    }

    println(maxDistance)
}